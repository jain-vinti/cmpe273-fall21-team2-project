from flask import Flask, Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json
import os
import requests 

views = Blueprint('views', __name__)



@views.route('/', methods=['GET', 'POST'])

def home():
    current_user="munjal"
    app = Flask(__name__) 
    UPLOAD_FOLDER = '/Users/shreynadiadwala/Desktop/SJSU_Shrey/CMPE 273/Client to server'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if request.method == 'POST':
        

        print("Inside / Hello world")
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        if file:
            print("file found success->", file)
            
        
        #name = file.filename
        
        url = 'http://127.0.0.1:5000'

        with open(file.filename, 'rb') as f:
            output = requests.post(url, data=f) 

        print(output)
        print("done")


        

    return render_template("home.html", user=current_user)




    
