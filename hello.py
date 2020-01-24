from flask import Flask, send_file

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello 1World!"

def give_json():
    return send_file('convertcsv.json')


if __name__ == "__main__":
    app.run()
