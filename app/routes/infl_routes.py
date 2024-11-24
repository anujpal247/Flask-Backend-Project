from flask import Blueprint, jsonify, request
from ..models import Influencer, User
from ..extensions import db

infl_bp = Blueprint('influencer', __name__, url_prefix='/api/v1/infl')

@infl_bp.post('/add')
def add_details():
  # get data
  data = request.get_json()
  print(data)

  # find infl
  infl = Influencer.query.filter_by(user_id=data["user_id"]).first()
  if (not infl):
    return jsonify({"message": "infl doest not found"}), 404
  
  # update info
  infl["category"] = data["category"]
  infl["niche"] = data["niche"]
  infl["reach"] = data["reach"]
  infl["followers"] = data["followers"]
  infl["engagement_rate"] = data["engagement_rate"]

  # save it
  db.session.add(infl)
  db.session.commit()

  return jsonify({"message": "infl details added successfully!!", "data": data}), 200

@infl_bp.get('/u/<int:user_id>')
def get_infl(user_id):
  infl = Influencer.query.filter_by(user_id=user_id).first()

  # if infl not found
  if (not infl):
    return jsonify({"message": "infl doest not exist"}), 404
  
  # send infl info
  return jsonify({"message": "infl found", "data": infl}), 200

@infl_bp.delete('/del/<int:user_id>')
def delelte_infl(user_id):
  # find infl
  user = User.query.filter_by(user_id=user_id)
  
  # if infl not found
  if (not user):
    return jsonify({"message": "infl not found"}), 404
  
  # delete it
  db.session.delete(user)
  db.session.commit()
  
  return jsonify({"message": "infl deleted successfully"}), 200