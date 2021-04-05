from flask import Flask
from flask import render_template # this function knows how to read html files
from flask import request

app = Flask(__name__, template_folder = r'C:\Users\Kitty\Desktop\learnpy\projects\gothonweb\templates')

@app.route("/hello", methods = ['POST', 'GET']) # this refers to 'index' mapping, flask will use 'def index'
def index():
    greeting = "Hello World"

    if request.method == "POST": # See HTML where this statement is satisfied
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting = greeting)
    else:
        return render_template("hello_form.html")
   

if __name__ == "__main__":
    app.run()