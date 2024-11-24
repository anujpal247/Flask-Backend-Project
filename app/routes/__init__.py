
from .user_routes import user_bp
from .ad_request_routes import ad_req_bp
from .camp_routes import camp_bp
from .infl_routes import infl_bp
from .spon_routes import spon_bp

def register_routes(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(infl_bp)
    app.register_blueprint(spon_bp)
    app.register_blueprint(ad_req_bp)
    app.register_blueprint(camp_bp)
