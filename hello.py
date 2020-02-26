from flask import Flask, send_file, render_template

import db_sqlite

app = Flask(__name__)


@app.route("/")
def home_text():
    return render_template('pathes.html')


@app.route("/hw/")
def hello():
    return "Hello World!"


@app.route("/json/")
def show_json():
    return send_file('convertcsv.json')


@app.route("/db/")
def show_db():
    return db_sqlite.get_some_data()


if __name__ == "__main__":
    app.debug = True
    app.run()
