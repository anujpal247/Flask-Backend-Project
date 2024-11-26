from flask import Blueprint, jsonify, request
from ..models import Sponsor, User
from ..extensions import db
# user_bp = Blueprint('user', __name__, url_prefix='/api/v1/user')
spon_bp = Blueprint('sponsor', __name__, url_prefix='/api/v1/spon')

@spon_bp.post('/create')
def add_detail():
  # get data
  data = request.get_json()

  # find sponsor
  spon = Sponsor.query.filter_by(user_id=data["user_id"]).first()
  if(not spon):
    return jsonify({"message": "spon does not exist", "status": False}), 400
  
  # update info
  spon.company_name = data["company_name"]
  spon.industry = data["industry"]
  spon.budget = data["budget"]

  # save changes
  db.session.add(spon)
  db.session.commit()

  return jsonify({"message": "spon updated successfully", "status": True}), 200

@spon_bp.get('/me/<int:user_id>')
def get_spon(user_id):
  # get spon
  spon = Sponsor.query.filter_by(user_id=user_id).first()
  if(not spon):
    return jsonify({"message": "spon does not exist", "status": False}), 400
  
  return jsonify({"message": "sponsor found", "data": spon.json(), "status": True}), 200


@spon_bp.delete('/del/<int:user_id>')
def delete_spon(user_id):
  user = User.query.filter_by(user_id=user_id).first()

  if(not user):
    return jsonify({"message": "spon does not exist", "status": False}), 404
  
  db.session.delete(user)
  db.session.commit()
  
  return jsonify({"message": "spon deleted", "status": True}), 200