from flask import Flask, send_file, Response, render_template

app = Flask(__name__)


@app.route("/")
def home_text():
    # with open('pathes', 'r') as text:
    #     content = text.read()
    # return render_template('pathes.html', content=content)

    return render_template('pathes.html')


@app.route("/hw/")
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
