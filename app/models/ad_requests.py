from datetime import datetime
from ..extensions import db

class AdRequest(db.Model):
    __tablename__ = 'ad_requests'
    
    ad_request_id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.campaign_id', ondelete='CASCADE'), nullable=False)
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencers.influencer_id', ondelete='CASCADE'), nullable=False)
    message = db.Column(db.Text)
    requirements = db.Column(db.Text)
    payment_amount = db.Column(db.Numeric(15, 2), nullable=False)
    status = db.Column(db.Enum('Pending', 'Accepted', 'Rejected', name='status_types'), default='Pending', nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships to access related Campaign and Influencer objects
    campaign = db.relationship('Campaign', backref=db.backref('ad_requests', cascade="all, delete"))
    influencer = db.relationship('Influencer', backref=db.backref('ad_requests', cascade="all, delete"))

    def __repr__(self):
        return f'<AdRequest {self.ad_request_id} - Status: {self.status}>'

    def json(self):
        return {
            "campaign_id": self.campaign_id,
            "influencer_id": self.influencer_id,
            "message": self.message,
            "requirements": self.requirements,
            "status": self.status,
            "payment_amount": self.payment_amount,
        }