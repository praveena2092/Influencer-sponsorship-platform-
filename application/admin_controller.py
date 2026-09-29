from flask import current_app as app
import requests
from .models import Admin,Sponsors,Influencers,Campaign,Ad_request
from flask import render_template
from flask import request
from .database import db
from .rest import *
BASEURL="http://127.0.0.1:5000"

@app.route("/")
def user():
    return render_template("index.html")
@app.route("/main/login")
def main():
    return render_template("login.html")
@app.route("/main/signup")
def main_signup():
    return render_template("sign_up.html")
@app.route("/create/admin",methods=["POST","GET"])
def create_admin():
    if request.method=="POST":
        a_name=request.form["a_name"]
        a_password=request.form["a_password"]
        admin=Admin(
            admin_name=a_name,
            admin_password=a_password
            
        )
        
        db.session.add(admin)
        db.session.commit()
       
        return render_template("admin_page.html",admin=admin)
    return render_template("create_admin.html")

@app.route("/admin/login",methods=['POST',"GET"])
def admin_login():
    if request.method=="POST":
        a_name=request.form["a_name"]
        a_password=request.form["a_password"]
        admin=Admin.query.filter_by(admin_name=a_name,admin_password=a_password).first()
        if(admin!=None):
            return render_template("admin_page.html",admin=admin)
        else:
            return render_template("error.html")
    return render_template("admin_login.html")


@app.route('/view/sponsor',methods=['POST',"GET"])
def view_sponsor():
    if request.method=="POST":
        flag=request.form['flag']
        review=request.form['review']
        s=request.args['s']
        spon=Sponsors.query.filter_by(sponsor_id=s).first()
        spon.sponsor_flag=flag
        spon.review_admin=review
        db.session.commit()
        get_r=requests.put(BASEURL+"/admin_api")
        return render_template('success_sponsor.html')
        
    all=Sponsors.query.all()
    return render_template("view_sponsors.html",all=all)

@app.route("/view/admin/campaign",methods=["POST","GET"])
def view_admin_camp():
    if request.method=="POST":
        c=request.args['s']
        flag=request.form['flag']
        review=request.form['review']
        camp=Campaign.query.filter_by(campaign_id=c).first()
        print(camp,flag)
        camp.campaign_flag=flag
        camp.review_admin=review
        db.session.commit()
        
        get_r=requests.put(BASEURL+"/admin_api")
        return get_r.text
    all=Campaign.query.all()
    return render_template("admin_campaign_view.html",all=all)
    
@app.route('/view/influencer',methods=['POST',"GET"])
def view_influencer():
    if request.method=="POST":
        i=request.args['s']
        flag=request.form['flag']
        review=request.form['review']
        influ=Influencers.query.filter_by(influencer_id=i).first()
        print(influ,flag)
        influ.influencer_flag=flag
        influ.review_admin=review
        db.session.commit()
        get_r=requests.put(BASEURL+"/admin_api")
        return render_template("success_i.html")
    all=Influencers.query.all()
    return render_template("view_influencer.html",all=all)

@app.route("/view/ad",methods=['POST',"GET"])
def view_ad():
    all=Ad_request.query.all()
    return render_template("view_ad_request.html",all=all)




@app.route("/admin_api")
def delete():
    if request.method=="POST":
        request.delete()
    