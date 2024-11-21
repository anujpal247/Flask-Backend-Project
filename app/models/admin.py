from ..extensions import db

class Admin(db.Model):
    __tablename__ = 'admins'
    
    admin_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)

    # Relationship to access the User object directly
    user = db.relationship('User', backref=db.backref('admin', uselist=False, cascade="all, delete"))

    def __repr__(self):
        return f'<Admin {self.admin_id}>'
    
    def __init__(self, user_id):
        self.user_id = user_id