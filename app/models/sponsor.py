from ..extensions import db

class Sponsor(db.Model):
    __tablename__ = 'sponsors'
    
    sponsor_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    company_name = db.Column(db.String(255))
    industry = db.Column(db.String(255))
    budget = db.Column(db.Numeric(15, 2), default=0.00)

    # Relationship to access the User object directly
    user = db.relationship('User', backref=db.backref('sponsor', uselist=False, cascade="all, delete"))

    def __repr__(self):
        return f'<Sponsor {self.company_name}>'