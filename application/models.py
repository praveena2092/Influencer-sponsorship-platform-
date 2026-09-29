from .database import db
class Admin(db.Model):
    admin_id=db.Column(db.Integer,primary_key=True)
    admin_name=db.Column(db.String)
    admin_password=db.Column(db.String)

class Sponsors(db.Model):
    sponsor_id=db.Column(db.Integer,primary_key=True)
    sponsor_name=db.Column(db.String,nullable=False)
    sponsor_industry=db.Column(db.String)
    sponsor_budget=db.Column(db.String)
    sponsor_password=db.Column(db.String)
    members=db.relationship("Campaign",backref="campaigns",cascade="all,delete")
    ad_request=db.relationship("Influencers",secondary='ad_request',backref="ad_request")
    sponsor_flag=db.Column(db.String ,nullable=True)
    review_admin=db.Column(db.String, nullable=True)
    
class Influencers(db.Model):
    influencer_id=db.Column(db.Integer,primary_key=True)
    influencer_name=db.Column(db.String,nullable=False)
    influencer_category=db.Column(db.String)
    influencer_niche=db.Column(db.String)
    influencer_reach=db.Column(db.String)
    influencer_password=db.Column(db.String)
    influencer_flag=db.Column(db.String ,nullable=True)
    review_admin=db.Column(db.String, nullable=True)
    
class Campaign(db.Model):
    sponsor_id=db.Column(db.Integer,db.ForeignKey("sponsors.sponsor_id"),primary_key=True)
    campaign_id=db.Column(db.Integer,primary_key=True)
    campaign_name=db.Column(db.String)
    campaign_description=db.Column(db.String)
    status=db.Column(db.String)
    start_date=db.Column(db.String)
    end_date=db.Column(db.String)
    campaign_budget=db.Column(db.Integer)
    visibility=db.Column(db.String)
    goals=db.Column(db.String)
    campaign_flag=db.Column(db.String ,nullable=True)
    review_admin=db.Column(db.String, nullable=True)
        
class Ad_request(db.Model):
    sponsor_id=db.Column(db.Integer,db.ForeignKey("sponsors.sponsor_id"),primary_key=True)
    influencer_id=db.Column(db.Integer,db.ForeignKey("influencers.influencer_id"),primary_key=True)
    campaign_id=db.Column(db.Integer,db.ForeignKey("campaign.campaign_id"),primary_key=True)
    message=db.Column(db.String)
    requirements=db.Column(db.String)
    payment_amount=db.Column(db.Integer)
    status=db.Column(db.String)
