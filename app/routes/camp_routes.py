from flask import Blueprint, jsonify, request

camp_bp = Blueprint('campaigns', __name__, url_prefix='/api/v1/camp')

@camp_bp.post('/add')
def add_camp():
  pass