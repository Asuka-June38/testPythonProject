from flask import Flask, send_file


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/json/")
def show_json():
    return send_file('convertcsv.json')


@app.route("/db/")
def show_db():
    pass


if __name__ == "__main__":
    app.debug = True
    app.run()
