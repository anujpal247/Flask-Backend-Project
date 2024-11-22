from flask import Blueprint, jsonify, request

ad_req_bp = Blueprint('ad_requests', __name__, url_prefix='/api/v1/ad-req')

@ad_req_bp.post('/add')
def add_ad_req():
  pass