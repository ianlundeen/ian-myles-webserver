## Url is http://127.0.0.1:5000/
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Myles' Flask Page!"

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0")