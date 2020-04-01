import os #imports os from the standard Python library
import json
from flask import Flask, render_template #imports the Flask class and the render_template class

app = Flask(__name__) #creates an instance of the Flask class and stores it in the 'app' variable

@app.route("/") #this is a decorator - a way of wrapping functions. Decorators start with the @ sign
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    data = [] #sets up 'data' as an empty array
    with open("data/company.json", "r") as json_data: #opens the company.json file. "r" opens the file for reading (while "a" would open the file for the purpose of appending)
        data = json.load(json_data) #the 'data' array will comtain the data in the company.json file
    return render_template("about.html", page_title="About", company=data) #when we navigate to about.html, the template will be returned

@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact") #when we navigate to contact.html, the template will be returned

@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers") #when we navigate to careers.html, the template will be returned

if __name__ == "__main__": #__main__ is the name of the default module in python
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", "5000")),
            debug=True) #allows for easier debugging

