from flask import Blueprint, jsonify, request
from ..models import Sponsor, User
from ..extensions import db
# user_bp = Blueprint('user', __name__, url_prefix='/api/v1/user')
spon_bp = Blueprint('sponsor', __name__, url_prefix='/api/v1/spon')

@spon_bp.post('/add')
def add_detail():
  # get data
  data = request.get_json()
  print(data)

  # find sponsor
  spon = Sponsor.query.filter_by(user_id=data["user_id"]).first()
  if(not spon):
    return jsonify({"message": "spon does not exist"}), 400
  
  # update info
  spon["company_name"] = data["company_name"]
  spon["industry"] = data["industry"]
  spon["budget"] = data["budget"]

  # save changes
  db.session.add(spon)
  db.session.commit()

  return jsonify({"message": "spon updated successfully"}), 200

@spon_bp.get('/u/<int:user_id>')
def get_spon(user_id):
  # get spon
  spon = Sponsor.query.filter_by(user_id=user_id).first()
  if(not spon):
    return jsonify({"message": "spon does not exist"}), 400
  
  return jsonify({"message": True, "data": spon}), 200


@spon_bp.delete('/del/<int:user_id>')
def delete_spon(user_id):
  user = User.query.filter_by(user_id=user_id).first()

  if(not user):
    return jsonify({"message": "spon does not exist"}), 404
  
  db.session.delete(user)
  db.session.commit()
  
  return jsonify({"message": "spon deleted"}), 200