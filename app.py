# import the Flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# simple route
@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello, World!"

# dynamic route
@app.route("/path/<path:value>")
def path_type(value):
    print value
    return "correct"

# dynamic route with explicit status codes
@app.route("/name/<name>")
def index(name):
    if name.lower() == "efra":
        return "Hello, {}".format(name), 200
    else:
        return "Not Found", 404 

if __name__ == "__main__":
    app.run(host="0.0.0.0")