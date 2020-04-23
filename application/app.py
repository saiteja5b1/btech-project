from flask import Flask,render_template,url_for,request
from flask_login import login_required
import json
from db_connect import connect
from db_user import user_details
from panda_data import data


app=Flask(__name__)
# login = LoginManager(app)

""" creating different routes for different webpages """
@app.route('/')
def home():
    data={'Name': 'yesu babu', 'Age': '21', 'PhNo': '9849643914', 'Address': 'kankipadu', 'District': 'krishna', 'Mandal': 'kankipadu', 'place': 'kankipadu', 'identity': 'ownland','landarea':'30','culture':'Monoculture','cropkind':'cash', 'crop_select': 'rice', 'date1': '16/04/2020', 'crop1': 'tobacco', 'pro1': '40', 'date2': '17/04/2020', 'crop2': 'ragi', 'Pro2': '30', 'date3': '18/04/2020', 'crop3': 'wheat', 'pro3': '20'}
    user_details(data)
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/about')
def aboutus():
    return render_template('aboutus.html')

@app.route('/services')
def services():
    with open('datasets/dat.json','r') as f:
        datalist=json.load(f)
    dist=list(datalist.keys()) 
    # with open('datasets/crops.json','r') as g:
    #     crops=json.load(g)
    crop=data()
    crops=crop['crop'].unique()
    return render_template('farmersearch.html',datalist=datalist,districts=dist,crops=list(crops))
    
@app.route('/hello',methods=['POST'])
def hello():
    start=request.form['start']
    end=request.form['end']
    district=request.form['District']
    mandal=request.form['Mandal']
    crops=request.form['crops']
    select=request.form['select']
    c=request.form
    print(c,list(c),dict(c))
    return render_template('hello.html',start=start,end=end,district=district,mandal=mandal,crops=crops,select=select)

@app.route('/registersubmit',methods=['POST'])
def registersubmit():
    start=request.form['Name']
    end=request.form['Age']
    district=request.form['PhNo']
    mandal=request.form['Mandal']
    crops=request.form['Address']
    select=request.form['District']
    c=request.form
    print(dict(c))
    return render_template('hello.html',start=start,end=end,district=district,mandal=mandal,crops=crops,select=select)

@app.route('/contact')
def contactus():
    return render_template('contactus.html')
# @app.login('/login',methid)

@app.route('/register',methods=['GET'])
def register():
    with open('datasets/dat.json','r') as f:
        datalist=json.load(f)
    dist=list(datalist.keys())    
    return render_template('register1.html',datalist=datalist,districts=dist)

# @app.route('/register',methods=['POST'])
# def getvalue():
#     name=request.form['Name']
#     age=request.form['Age']
#     phone=request.form['PhnNo']
#     address=request.form['Address']
#     district=request.form['District']
#     mandal=request.form['Mandal']
#     connect('yesu4658',[name,age,phone,address,'andhrapradesh',district,mandal])
#     return render_template('hello.html',name=name,age=age,phno=phone,address=address,district=district,mandal=mandal)

@app.route('/arable',methods=['GET','POST'])
def arable():
    with open('datasets/arable.json') as f:
        crops=json.load(f)
    return render_template('arable.html',datalist=crops)

@app.route('/view')
@login_required
def viewProfile():
    return render_template('login.html')


""" main app calling """
if __name__=="__main__":
    app.run(debug=True)