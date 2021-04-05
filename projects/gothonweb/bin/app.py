from flask import Flask
from flask import render_template # this function knows how to read html files
from flask import request

app = Flask(__name__, template_folder = r'C:\Users\Kitty\Desktop\learnpy\projects\gothonweb\templates')

@app.route("/hello") # this refers to 'index' mapping, flask will use 'def index'
def index():
    name = request.args.get('name', 'Nobody')
    
    if name:
        greeting = f"Hello {name}"
    else:
        greeting = "Hello World"
    
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run()