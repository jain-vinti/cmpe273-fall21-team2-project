from werkzeug.datastructures import FileStorage
import os
from flask import request
import flask
import requests
import time
app, self_host, self_port, nodes = flask.Flask(__name__), "0.0.0.0", 8081, [
    'http://127.0.0.1:8000/', 'http://127.0.0.1:8001/']
requestQueue = []

fileId = 1000


def requestWorker(req, workerUrl):
    global fileId
    fileId += 1
    filename = 'request' + str(fileId) + '.py'
    FileStorage(req.stream).save(
        os.path.join('./', filename))
    with open(filename, 'rb') as f:
        output = requests.post(workerUrl + str(fileId), data=f).text
    # print(output)
    os.remove(filename)
    return output, 200


@app.errorhandler(404)
def route_page(err):
    global nodes
    global requestQueue
    requestQueue.append(request)
    print(nodes, requestQueue)
    while nodes == []:
        continue
    currNode = nodes.pop(0)
    currReq = requestQueue.pop(0)
    output = requestWorker(currReq, currNode)
    nodes.append(currNode)
    return output


if __name__ == "__main__":
    app.run(host=self_host, port=self_port)
