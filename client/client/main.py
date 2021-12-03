from website import create_app
self_host, self_port  =  "0.0.0.0", 5000
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host=self_host, port=self_port)
