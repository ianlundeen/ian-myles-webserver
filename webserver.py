# Url is http://127.0.0.1:5000/
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/page2')
def page2():
    return render_template('page2.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
