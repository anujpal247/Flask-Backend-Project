from flask import Blueprint, jsonify, request
from ..models import AdRequest
from ..extensions import db

ad_req_bp = Blueprint('ad_requests', __name__, url_prefix='/api/v1/ad-req')

# create ad_req   /create
# update ad_req   /update/id
# delete ad_req   /del/id
# get ad_req    /me/id

@ad_req_bp.post('/create')
def add_ad_req():
  # get data 
  data = request.get_json()
  
  # validtae data
  if(not data["campaign_id"]):
    return jsonify({"message": "campaign_id required", "status": False}), 400
  
  if(not data["influencer_id"]):
    return jsonify({"message": "influencer_id required", "status": False}), 400
  
  if(not data["payment_amount"]):
    return jsonify({"message": "payment_amount required", "status": False}), 400
  
  if(not data["status"]):
    return jsonify({"message": "status required", "status": False}), 400
  
  # create instance
  ad_req = AdRequest(
    campaign_id=data["campaign_id"],
    influencer_id=data["influencer_id"],
    message=data["message"],
    requirements=data["requirements"],
    payment_amount=data["payment_amount"],
    status=data["status"],
  )

  if(not ad_req):
    return jsonify({"message": "some thing wrong while creating ad request instacve", "status": False}), 400
  
  # save it
  db.session.add(ad_req)
  db.session.commit()

  return jsonify({"message": "ad_req created successfully", "status": True}), 201

@ad_req_bp.get('/me/<int:ad_req_id>')
def get_ad_req(ad_req_id):
  # find ad_req
  req = AdRequest.query.filter_by(ad_request_id=ad_req_id).first()
  
  # if ad_req not exist
  if (not req):
    return jsonify({"status": False, "message": "Ad request not exist"}), 404
  # send res
  return jsonify({"status": True, "message": "Ad req found", "data": req.json()}), 200

@ad_req_bp.put('/update/<int:ad_req_id>')
def update_ad_req(ad_req_id):
  # find ad_req
  req = AdRequest.query.filter_by(ad_request_id=ad_req_id).first()

  # if ad_req not exist
  if (not req):
    return jsonify({"status": False, "message": "Ad request not exist"}), 404
  # get data
  data = request.get_json()

  # update info
  if(not data["payment_amount"]):
    req.payment_amount = req.payment_amount
  else:
    req.payment_amount = data["payment_amount"]

  if(not data["status"]):
    req.status = req.status
  else:
    req.status = data["status"]

  if(data["message"]):
    req.message = data["message"]

  if(data["requirements"]):
    req.requirements = data["requirements"]
    
  # save changes
  db.session.add(req)
  db.session.commit()
  
  # send res
  return jsonify({"status": True, "message": "Ad req found", "data": req.json()}), 200

@ad_req_bp.delete('/del/<int:ad_req_id>')
def delete_ad_req(ad_req_id):
  # find ad_req
  req = AdRequest.query.filter_by(ad_request_id=ad_req_id).first()

  # if ad_req not exist
  if (not req):
    return jsonify({"status": False, "message": "Ad request not exist"}), 404
  
  # delete ad_req
  db.session.delete(req)
  db.session.commit()

  # send res
  return jsonify({"status": True, "message": "Ad req deleted"}), 200