
from flask import Blueprint, jsonify, request
from ..models import User, Admin, Influencer, Sponsor
from ..extensions import db
user_bp = Blueprint('user', __name__, url_prefix='/api/v1/user')

# @user_bp.route('/', methods=['GET'])
# def get_users():
#     return jsonify({"message": "List of users"})


# @user_bp.route('/', methods=['POST'])
# def create_user():
#     user = request.get_json()
#     print(user)
#     return jsonify({"data": user})

@user_bp.post('/register')
def register_user():
    # get data
    data = request.get_json()
    
    # print(data)
    # validate data (not empty)
    if(not data["name"]):
        return jsonify({"message": "name is required!!"}), 400
    
    if(not data["email"]):
        return jsonify({"message": "email is required!!"}), 400
    
    if(not data["role"]):
        return jsonify({"message": "role is required!!"}), 400
    
    if(not data["password"]):
        return jsonify({"message": "password is required!!"}), 400
    # check for user ( email )
    user = User.query.filter_by(email=data["email"]).first()
    
    if(user):
        return jsonify({"message": "email already exists"}), 400
    
    created_user = User(role=data["role"], name=data["name"], 
                        email=data["email"], password=data["password"])
    

    db.session.add(created_user)

    user = User.query.filter_by(email=data["email"]).first()
    # print(user)
    if(data["role"] == "admin"):
        admin = Admin(user_id=user.user_id)
        db.session.add(admin)

    if (data["role"] == "influencer"):
        infl = Influencer(user_id=user.user_id)
        db.session.add(infl)


    if (data["role"] == "sponsor"):
        spon = Sponsor(user_id=user.user_id)
        db.session.add(spon)


    db.session.commit()

    return jsonify({"data": data, "message": "user registered successfully"}), 200

@user_bp.post('/login')
def login_user():
    pass

@user_bp.get('/me')
def get_user():
    pass


@user_bp.delete('/delete/<int:user_id>')
def delete_user(user_id):
    print(user_id)
    user = User.query.filter_by(user_id=user_id).first()

    if (not user):
        return jsonify({"message": "user does not exist"}), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "user deleted successfully"}), 200