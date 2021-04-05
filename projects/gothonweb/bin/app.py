from flask import Flask
from flask import render_template # this function knows how to read html files

app = Flask(__name__, template_folder = r'C:\Users\Kitty\Desktop\learnpy\projects\gothonweb\templates')

@app.route("/") # this refers to 'index' mapping, flask will use 'def index'
def index():
    greeting = "Hello World"
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run()