from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           captors=["12 : 0", "13 : 1", "14 : 0"])


if __name__ == "__main__":
    app.run()
