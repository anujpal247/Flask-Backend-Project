from ..extensions import db

class Influencer(db.Model):
    __tablename__ = 'influencers'
    
    influencer_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    category = db.Column(db.String(255))
    niche = db.Column(db.String(255))
    reach = db.Column(db.Integer)
    followers = db.Column(db.Integer)
    engagement_rate = db.Column(db.Numeric(5, 2))

    # Relationship to access the User object directly
    user = db.relationship('User', backref=db.backref('influencer', uselist=False, cascade="all, delete"))

    def __repr__(self):
        return f'<Influencer {self.user_id}>'