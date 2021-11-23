import flask, requests, itertools
app = flask.Flask(__name__)
self_host = "0.0.0.0"
self_port = 5000
nodes = itertools.cycle(['http://127.0.0.1:5000','http://127.0.0.1:5001'])
print(nodes)

for node in nodes:
    r = requests.get(node)
    print(r.content)
@app.errorhandler(404)
def route_page(err):
    curr_node = next(nodes)
    return getattr(requests, flask.request.method.lower())(f"{curr_node}{flask.request.path}").text
if __name__ == "__main__": app.run(host=self_host, port=self_port)
