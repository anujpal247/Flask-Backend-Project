
from ..extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Enum('admin', 'sponsor', 'influencer', name='role_types'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    # profile_image = db.Column(db.String(255))
    # created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, role, name, email, password):
        self.role = role
        self.name = name
        self.email = email
        self.password = password
        
        

    def __repr__(self):
        return f'<User {self.name}>'
    

