from flask import current_app as app
import requests
from .models import Admin,Sponsors,Influencers,Campaign,Ad_request
from flask import render_template
from flask import request
from .database import db
from .rest_influencer import *

BASEURL="http://127.0.0.1:5000"


@app.route("/create/influencer",methods=["POST","GET"])
def create_influencer():
    if(request.method=="POST"):
        i_name=request.form["i_name"]
        i_niche=request.form['i_niche']
        i_reach=request.form['i_reach']
        i_category=request.form['i_category']
        i_password=request.form['i_password']
    
        influ=Influencers(
            influencer_name=i_name,
            influencer_category=i_category,
            influencer_niche=i_niche,
            influencer_reach=i_reach,
            influencer_password=i_password,
            
        )
    
        db.session.add(influ)
        db.session.commit()
        return render_template("influencers_page.html",i=influ)
    return render_template("create_influencers.html")


@app.route("/influencers/login",methods=['POST',"GET"])
def influencers_login():
    if request.method=="POST":
        i_name=request.form["i_name"]
        i_password=request.form["i_password"]
        i=Influencers.query.filter_by(influencer_name=i_name,influencer_password=i_password).first()
        if(i!=None):
            return render_template("influencers_page.html",i=i)
        else:
            return render_template("error.html")
    return render_template("influencers_login.html")
        
        
@app.route('/influencers/page',methods=["POST","GET"])
def influencer_page():
    return render_template("influencers_page.html")


@app.route("/delete/influencer",methods=['POST',"GET"])
def delete_influencer():
    i=request.args['i']
    influ=Influencers.query.filter_by(influencer_id=i).first()
    db.session.delete(influ)
    db.session.commit()
    get_r=requests.delete(BASEURL+"/influencer_api")
    return get_r.text
    


@app.route("/update/profile/influencer",methods=['POST',"GET"])
def update_profile_influ():
    if request.method=="POST":
        i1=request.args['i']
        
        
        i=Influencers.query.filter_by(influencer_id=i1).first()
        influencer_category=request.form['category']
        influencer_niche=request.form['niche']
        influencer_reach=request.form['reach']
        i.influencer_category=influencer_category
        i.influencer_niche=influencer_niche
        i.influencer_reach=influencer_reach
        db.session.commit()
        return render_template("influencers_page.html",i=i)
    i=request.args['i']
    i=Influencers.query.filter_by(influencer_id=i).first()
    return render_template("update.html",i=i)



@app.route("/campaign/search",methods=['GET','POST'])
def campaign_search ():
    if request.method=="POST":
        
        all=Campaign.query.filter_by(visibility=request.form['visibility']).all()
        
        return render_template("search_campaign_results.html",all=all)
    return render_template("campaign_search.html")



@app.route("/view/ad_request",methods=['POST',"GET"])
def view_ad_request():
    i=request.args['i']
    all=Ad_request.query.filter_by(influencer_id=i).all()
    return render_template("view_ad_request.html",all=all)


@app.route("/view/campaign",methods=['POST',"GET"])
def view_campaign():
    all=Campaign.query.all()
    return render_template("view_campaign.html",all=all)



@app.route("/campaign/search/update",methods=['GET',"POST"])
def cam_update():
    if request.method=="POST":
        x=Campaign.query.filter_by(campaign_id=request.args['c']).first()
        x.status=request.form['status']
        db.session.commit()
        return render_template("campaign_search.html")
    return render_template("campaign_search.html")