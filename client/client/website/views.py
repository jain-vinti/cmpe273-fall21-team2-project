from flask import Flask, Blueprint, render_template, request, flash, jsonify
import time
import json
import os
import requests 

views = Blueprint('views', __name__)



@views.route('/', methods=['GET', 'POST'])

def home():
    
    app = Flask(__name__) 
    UPLOAD_FOLDER = 'E:/development/pydevlopment/273 project/cmpe273-fall21-team2-project/client/client/website'
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
            
        
        name = file.filename
        print(name)
        url = 'http://127.0.0.1:5000'
        #time.sleep(1)
        with open(file.filename, 'rb') as f:
            output = requests.post(url, data=f) 

        print(output)
        print("done")
    return render_template("home.html")




    
