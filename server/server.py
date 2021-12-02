from werkzeug.datastructures import FileStorage
import os
from flask import request
from threading import Thread
import flask
import requests
from multiprocessing import Pool, TimeoutError
app, self_host, self_port, nodes = flask.Flask(__name__), "0.0.0.0", 8081, [
    'http://127.0.0.1:8000/', 'http://127.0.0.1:8001/']
# requestQueue = []

fileId = 1000


def requestWorker(workerUrl):
    global fileId
    filename = 'request' + str(fileId) + '.py'
    FileStorage(request.stream).save(
        os.path.join('./', filename))
    with open(filename, 'rb') as f:
        output = requests.post(workerUrl, data=f).text
    # print(output)
    fileId += 1
    # os.remove(filename)
    return output, 200


@app.errorhandler(404)
def route_page(err):
    global nodes
    """ with Pool(processes=2) as pool:
    if nodes != []:
        runningNode = nodes.pop(0)
        ans = pool.apply_async(requestWorker, (runningNode, ))
        otp = ans.get(timeout=1)
        nodes.append(runningNode)
        return otp """

    """ if nodes != []:
        runningNode = nodes.pop(0)
        process = Thread(target=requestWorker, args=[runningNode])
        process.start()
        output = process.join()
        nodes.append(runningNode)
        return output """
    if nodes != []:
        currNode = nodes.pop(0)
        output = requestWorker(currNode)
        nodes.append(currNode)
        return output


if __name__ == "__main__":
    app.run(host=self_host, port=self_port)
