from werkzeug.datastructures import FileStorage
import os
from flask import request
import flask
import requests
import time
# app, self_host, self_port, nodes = flask.Flask(__name__), "0.0.0.0", 8081, [
#     'http://127.0.0.1:8000/', 'http://127.0.0.1:8001/']

# Setting up flask server
# Acting as a proxy between the worker nodes and client
# The server will recieve files from the clients

app = flask.Flask(__name__)
self_host = "0.0.0.0"
self_port = 8081

# Instantiating the worker nodes in a array.
# Two nodes running on 8000, 8001 ports 

nodes = ['http://127.0.0.1:8000/', 'http://127.0.0.1:8001/']

requestQueue = []

#File Id to create unique files based on requests
fileId = 1000

# RequestWorker function sends the file data to worker nodes
# Parameters: request object and hosted worker URL
def requestWorker(req, workerUrl):
    global fileId
    fileId += 1
    filename = 'request' + str(fileId) + '.py'

    # Saving the file in local dir of server

    FileStorage(req.stream).save(
        os.path.join('./', filename))
    with open(filename, 'rb') as f:

        # Send the POST request to workerUrl
        # recieve the output ones done.
        output = requests.post(workerUrl + str(fileId), data=f).text
    # print(output)

    #remove the temporary created file.
    os.remove(filename)
    # Return back to calling route function
    return output, 200

# Route function: recieves the requests from client
# Function servers as main component of the architecture
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
