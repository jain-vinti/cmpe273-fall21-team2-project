from flask import Flask
import requests, itertools

app = Flask(__name__)


nodes = itertools.cycle(['http://127.0.0.1:5000','http://127.0.0.1:5001'])
curr_node = next(nodes)
r = requests.get(curr_node)
print(r.content)
curr_node = next(nodes)

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
