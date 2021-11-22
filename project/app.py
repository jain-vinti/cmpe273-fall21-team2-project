from flask import Flask, request
import os
from werkzeug.datastructures import FileStorage

app = Flask(__name__)

fileId = 1


@app.route("/", methods=['POST'])
def upload_file():
    # print(request.headers)
    global fileId
    filename = 'request' + str(fileId) + '.py'
    FileStorage(request.stream).save(
        os.path.join('./', filename))
    otp = os.popen('python ' + filename).read()
    fileId += 1
    # print(otp)
    return otp, 200
