from flask import Blueprint, jsonify, request
from ..models import Campaign
from ..extensions import db

camp_bp = Blueprint('campaigns', __name__, url_prefix='/api/v1/camp')

# create camp  /create
# get camp  /me/id
# update camp  /update/id
# delete camp /del/id

@camp_bp.post('/create')
def create_camp():
  # get data
  data = request.get_json()
  print(data)
  # validate data
  if(not data["sponsor_id"]):
    return jsonify({"message": "sponsor_id is required!"}), 400
  
  if (not data["name"]):
    return jsonify({"message": "name is required"}), 400
  
  if (not data["budget"]):
    return jsonify({"message": "budget is required"}), 400
  
  if (not data["visibility"]):
    return jsonify({"message": "visibility is required"}), 400
  
  # create camp instance
  camp = Campaign(
    sponsor_id=data["sponsor_id"],
    name=data["name"],
    description=data["description"],
    budget=data["budget"],
    visibility=data["visibility"],
    goals=data["goals"],
    start_date=data["start_date"],
    end_date=data["end_date"],
  )
  if(not camp):
    return jsonify({"message": "camp instance did not created"}), 400
  # save it
  db.session.add(camp)
  db.session.commit()

  return jsonify({"status": True, "data": data}), 201

@camp_bp.get('/me/<int:camp_id>')
def get_camp(camp_id):
  # find camp
  camp = Campaign.query.filter_by(campaign_id=camp_id).first()

  # check if camp not exist
  if (not camp):
    return jsonify({"message": "campaign does not exist"}), 404
  # send it
  return jsonify({"message": True, "data": camp}), 200

@camp_bp.put('/update/<int:camp_id>')
def update_camp(camp_id):
  # find camp
  camp = Campaign.query.filter_by(campaign_id=camp_id).first()

  # if camp not exist
  if (not camp):
    return jsonify({"message": "campaign does not exist"}), 404
  
  # get data
  data = request.get_json()

  # validate data (not empty)
  
  if (not data["name"]):
    return jsonify({"message": "name is required"}), 400
  
  if (not data["budget"]):
    return jsonify({"message": "budget is required"}), 400
  
  if (not data["visibility"]):
    return jsonify({"message": "visibility is required"}), 400
  
  # update camp info
  camp["name"] = data["name"]
  camp["budget"] = data["budget"]
  camp["visibility"] = data["visibility"]

  if(data["description"]):
    camp["description"] = data["description"]

  if(data["start_date"]):
    camp["start_date"] = data["start_date"]

  if(data["end_date"]):
    camp["end_date"] = data["end_date"]

  if(data["goals"]):
    camp["goals"] = data["goals"]

  # save changes
  db.session.add(camp)
  db.session.commit()

  # send res
  return jsonify({"message": True, "data": camp}), 200

@camp_bp.delete('/del/<int:camp_id>')
def delete_camp(camp_id):
  # find camp
  camp = Campaign.query.filter_by(campaign_id=camp_id).first()

  # if camp not exist
  if (not camp):
    return jsonify({"message": "campaign does not exist"}), 404
  
  # delete it
  db.session.delete(camp)
  db.session.commit()
  
  # send res
  return jsonify({"status": True, "message": "campaign deleted"}), 200