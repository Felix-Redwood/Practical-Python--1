import os #imports os from the standard Python library
from flask import Flask, render_template #imports the Flask class and the render_template class

app = Flask(__name__) #creates an instance of the Flask class and stores it in the 'app' variable

@app.route("/") #this is a decorator - a way of wrapping functions. Decorators start with the @ sign
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html") #when we navigate to about.html, the template will be returned

@app.route("/contact")
def contact():
    return render_template("contact.html") #when we navigate to contact.html, the template will be returned

@app.route("/careers")
def careers():
    return render_template("careers.html") #when we navigate to careers.html, the template will be returned

if __name__ == "__main__": #__main__ is the name of the default module in python
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) #allows for easier debugging
