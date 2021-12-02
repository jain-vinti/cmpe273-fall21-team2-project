from flask import Flask, request
import os
from werkzeug.datastructures import FileStorage

app = Flask(__name__)

#fileId = 1


@app.route("/<fileId>", methods=['POST'])
def upload_file(fileId):
    # print(request.headers)
    filename = 'request' + str(fileId) + '.py'
    FileStorage(request.stream).save(
        os.path.join('./', filename))
    otp = os.popen('python ' + filename).read()
    os.remove(filename)
    # print(otp)
    return otp, 200
