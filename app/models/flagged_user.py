from ..extensions import db
from datetime import datetime



class FlaggedUser(db.Model):
    __tablename__ = 'flagged_users'
    
    flag_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    flagged_by = db.Column(db.Integer, db.ForeignKey('admins.admin_id'), nullable=False)
    reason = db.Column(db.Text, nullable=True)
    flagged_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships to access related User and Admin objects
    user = db.relationship('User', backref=db.backref('flagged_users', cascade="all, delete"))
    admin = db.relationship('Admin', backref=db.backref('flagged_users', cascade="all, delete"))

    def __repr__(self):
        return f'<FlaggedUser {self.flag_id} - User ID: {self.user_id}>'
