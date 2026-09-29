from flask import current_app as app
import requests
from .models import Admin,Sponsors,Influencers,Campaign,Ad_request
from flask import render_template
from flask import request
from .database import db
from .rest_sponsor import *



@app.route("/create/sponsor",methods=["POST","GET"])
def create_sponsor():
    if(request.method=="POST"):
        s_name=request.form["s_name"]
        s_budget=request.form['s_budget']
        s_industry=request.form['s_industry']
        s_password=request.form['s_password']
    
        spons=Sponsors(
            sponsor_name=s_name,
            sponsor_industry=s_industry,
            sponsor_budget=s_budget,
            sponsor_password=s_password
        )
    
        db.session.add(spons)
        db.session.commit()
        return  render_template("sponsor_page.html",s=spons)
    return render_template("create_sponsors.html")

    
@app.route("/sponsor/login",methods=['POST',"GET"])
def sponsor_login():
    if request.method=="POST":
        s_name=request.form["s_name"]
        s_password=request.form["s_password"]
        s=Sponsors.query.filter_by(sponsor_name=s_name,sponsor_password=s_password).first()
        if(s!=None):
            
            return render_template("sponsor_page.html",s=s)
        else:
            return render_template("error.html")
    return render_template("sponsor_login.html")



@app.route('/create/campagin',methods=["POST","GET"])
def create_campagin():
    r_id=request.args["s"]
    
    if request.method=='POST':
        print(request.args,"this")
        sponsor_id=request.args["s"]
        c_id=request.form['c_id']
        c_name=request.form["c_name"]
        c_description=request.form["c_description"]
        status=request.form["status"]
        s_date=request.form["s_date"]
        e_date=request.form['e_date']
        goals=request.form['goals']
        budget=request.form['budget']
        visibility=request.form['visibility']
        camp=Campaign(
            sponsor_id=request.args["s"],
            campaign_id=c_id,
            campaign_name=c_name,
            campaign_description=c_description,
            status=status,
            start_date=s_date,
            end_date=e_date,
            goals=goals,
            visibility=visibility,
            campaign_budget=budget   
        )
        db.session.add(camp)
        db.session.commit()
        s=Sponsors.query.filter_by(sponsor_id=sponsor_id).first()
        return render_template('sponsor_page.html',s=s)
    sponsor_id=request.args["s"]
    
    return render_template("create_campagin.html",s=sponsor_id)
 
 
 
 
@app.route("/ad/request",methods=['POST',"GET"])
def ad_request():
    if(request.method=="POST"):
        sponsor_id=request.args["s"]
        influencer_id=request.form['influencer_id']
        campaign_id=request.form['campaign_id']
        message=request.form['message']
        requirements=request.form['requirements']
        payment_amount=request.form['payment_amount']
        status=request.form['status']
        ad_request=Ad_request(
            sponsor_id=sponsor_id,
            influencer_id=influencer_id,
            campaign_id=campaign_id,
            message=message,
            requirements=requirements,
            payment_amount=payment_amount,
            status=status,
            
            
        )
        db.session.add(ad_request)
        db.session.commit()
        s=Sponsors.query.filter_by(sponsor_id=sponsor_id).first()
        return render_template('sponsor_page.html',s=s)
    sponsor_id=request.args["s"]
    all=Influencers.query.all()
    cam=Campaign.query.filter_by(sponsor_id=sponsor_id).all()
    return render_template("ad_request.html",sponsor_id=sponsor_id,all=all,cam=cam)


@app.route('/view/influencer/sponsor',methods=['POST',"GET"])
def view_influencer_sponsor():
    if request.method=="POST":
        i=request.args['s']
        flag=request.form['flag']
        review=request.form['review']
        influ=Influencers.query.filter_by(influencer_id=i).first()
        print(influ,flag)
        influ.influencer_flag=flag
        influ.review_admin=review
        db.session.commit()
    all=Influencers.query.all()
    return render_template("view_influencer.html",all=all)



@app.route("/update/campagin",methods=["POST","GET"])
def update_campagin():
    if (request.method=="POST"):
        campaign_name=request.form['campaign_name']
        campaign_description=request.form['campaign_description']
        start_date=request.form['start_date']
        end_date=request.form['end_date']
        visibility=request.form['visibility']
        goals=request.form['goals']
        campaign_budget=request.form['campaign_budget']
        campaign_id=request.form['campaign_id']
       
        s=request.args['s']
        cam=Campaign.query.filter_by(sponsor_id=s,campaign_id=campaign_id).first()
        
        cam.campaign_name=campaign_name
        cam.campaign_description=campaign_description
        cam.start_date=start_date
        cam.end_date=end_date
        cam.visibility=visibility
        cam.goals=goals
        cam.campaign_budget=campaign_budget
        db.session.commit()
        s=Sponsors.query.filter_by(sponsor_id=s).first()
        return render_template('sponsor_page.html',s=s)
        
    s=request.args['s']
    
    cam=Campaign.query.filter_by(sponsor_id=s).all()
    print(cam)
    return render_template("update_campagin.html",s=s,cam=cam)


@app.route("/update/ad/request",methods=['POST',"GET"])
def update_ad():
    if request.method=='POST':
        s=request.args['s']
        message=request.form['message']
        requirements=request.form['requirements']
        payment_amount=request.form['payment_amount']
        status=request.form['status']
        influencer_id=request.form['influencer_id']
        campaign_id=request.form['campaign_id']
       
        ad=Ad_request.query.filter_by(sponsor_id=s,campaign_id=campaign_id).first()
       
        ad.message=message
        ad.requirements=requirements
        ad.payment_amount=payment_amount
        ad.status=status
        ad.influencer_id=influencer_id
        db.session.commit()
        s=Sponsors.query.filter_by(sponsor_id=s).first()
        return render_template('sponsor_page.html',s=s)
    s=request.args['s']
    all=Influencers.query.all()
    cam=Campaign.query.filter_by(sponsor_id=s).all()
    
    return render_template("update_ad_request.html",s=s,all=all,cam=cam)



@app.route("/sponsor/delete",methods=['POST',"GET"])
def sponsor_delete():
    sp=request.args['s']
    
    spons=Sponsors.query.filter_by(sponsor_id=sp).first()
   
    db.session.delete(spons)
    db.session.commit()
    return render_template("index.html")


@app.route("/delete/ad_request",methods=['POST',"GET"])
def delete_ad_request():
    
    spon=request.args['s']
    s=Sponsors.query.filter_by(sponsor_id=spon).first()
    
    ad_request=Ad_request.query.filter_by(sponsor_id=spon).first()
    db.session.delete(ad_request)
    db.session.commit()
    
    return render_template("sponsor_page.html",s=s)

@app.route("/delete/campaign",methods=['POST',"GET"])
def delete_campaign():
    if request.method=='POST':
        spon=request.args['s']
        camp=request.form['campaign_id']
        camp=Campaign.query.filter_by(campaign_id=camp).first()
        db.session.delete(camp)
        db.session.commit()
        s=Sponsors.query.filter_by(sponsor_id=spon).first()
        return render_template ("sponsor_page.html",s=s)
    s=request.args['s']
    all=Campaign.query.filter_by(sponsor_id=s).all()
    return render_template("campaign_delete.html",all=all,s=s)



@app.route("/sponsor/search",methods=['GET','POST'])
def sponsor_search ():
    if request.method=="POST":
        s=request.form['reach']
        all=Influencers.query.filter(Influencers.influencer_reach >= request.form['reach']).all()
        
        return render_template("search_results.html",all=all)
    return render_template("sponsor_search.html")