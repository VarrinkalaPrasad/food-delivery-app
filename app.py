from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "application":"Food Delivery",
        "status":"Running",
        "host":socket.gethostname()
    }

@app.route("/health")
def health():
    return "Healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
