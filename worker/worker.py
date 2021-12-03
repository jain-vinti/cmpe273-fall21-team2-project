from flask import Flask, request
import os
from werkzeug.datastructures import FileStorage

app = Flask(__name__)

#fileId = 1

# Worker node same file hosted on diff ports
@app.route("/<fileId>", methods=['POST'])
def upload_file(fileId):
    # print(request.headers)
    filename = 'request' + str(fileId) + '.py'
    # Save a copy of stream
    FileStorage(request.stream).save(
        os.path.join('./', filename))
    # Run file with popen 
    otp = os.popen('python ' + filename).read()
    os.remove(filename)
    # print(otp)
    # Send output back to server 
    return otp, 200
