from ..extensions import db
from datetime import datetime

class Campaign(db.Model):
    __tablename__ = 'campaigns'
    
    campaign_id = db.Column(db.Integer, primary_key=True)
    sponsor_id = db.Column(db.Integer, db.ForeignKey('sponsors.sponsor_id', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    budget = db.Column(db.Numeric(15, 2), nullable=False)
    visibility = db.Column(db.Enum('public', 'private', name='visibility_types'), nullable=False)
    goals = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship to access the Sponsor object directly
    sponsor = db.relationship('Sponsor', backref=db.backref('campaigns', cascade="all, delete"))

    def __repr__(self):
        return f'<Campaign {self.name}>'
