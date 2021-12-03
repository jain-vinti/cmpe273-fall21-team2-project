from website import create_app
<<<<<<< HEAD
self_host, self_port  =  "0.0.0.0", 5001
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host=self_host, port=self_port)
=======

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 886701015736caea06e4ceca79575de5cb41b5b7
