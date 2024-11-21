
from flask import Blueprint, jsonify, request

user_bp = Blueprint('user', __name__, url_prefix='/api/users')

@user_bp.route('/', methods=['GET'])
def get_users():
    return jsonify({"message": "List of users"})


# @user_bp.route('/', methods=['POST'])
# def create_user():
#     user = request.get_json()
#     print(user)
#     return jsonify({"data": user})

@user_bp.post('/')
def create_user():
    user = request.get_json()
    print(user)
    return jsonify({"data": user}), 200
