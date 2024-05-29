from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! my lovely son yuvaan trilok calling you"
