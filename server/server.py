from werkzeug.datastructures import FileStorage
import os
from flask import request
import flask
import requests
import itertools
app, self_host, self_port, nodes = flask.Flask(_name_), "0.0.0.0", 5000, itertools.cycle(['http://127.0.0.1:8000/', 'http://127.0.0.1:8001/'])


fileId = 1000


@app.errorhandler(404)
def route_page(err):
    curr_node = next(nodes)
    global fileId
    filename = 'request' + str(fileId) + '.py'
    FileStorage(request.stream).save(
        os.path.join('./', filename))
    with open(filename, 'rb') as f:
        output = requests.post(f"{curr_node}{flask.request.path}", data=f).text
    # print(output)
    fileId += 1
    return output, 200


if _name_ == "_main_":
    app.run(host=self_host, port=self_port)