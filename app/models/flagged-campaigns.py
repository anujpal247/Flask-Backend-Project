from datetime import datetime
from ..extensions import db


class FlaggedCampaign(db.Model):
    __tablename__ = 'flagged_campaigns'
    
    flag_id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.campaign_id', ondelete='CASCADE'), nullable=False)
    flagged_by = db.Column(db.Integer, db.ForeignKey('admins.admin_id'), nullable=False)
    reason = db.Column(db.Text, nullable=True)
    flagged_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships to access related Campaign and Admin objects
    campaign = db.relationship('Campaign', backref=db.backref('flagged_campaigns', cascade="all, delete"))
    admin = db.relationship('Admin', backref=db.backref('flagged_campaigns', cascade="all, delete"))

    def __repr__(self):
        return f'<FlaggedCampaign {self.flag_id} - Campaign ID: {self.campaign_id}>'
