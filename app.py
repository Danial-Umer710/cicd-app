from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

def get_version():
    return os.getenv("APP_VERSION", "unknown")

def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_message():
    return os.getenv("BUILD_MESSAGE", "First deployment 🚀")

@app.route("/")
def home():
    return render_template(
        "index.html",
        version=get_version(),
        time=get_time(),
        message=get_message()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
