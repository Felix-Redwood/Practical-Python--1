import os  # imports os from the standard Python library
import json
# imports the Flask class, the render_template class, the request library and the flash class
from flask import Flask, render_template, request, flash

# creates an instance of the Flask class and stores it in the 'app' variable
app = Flask(__name__)
app.secret_key = 'some_secret'


# this is a decorator - a way of wrapping functions. Decorators start with the @ sign
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []  # sets up 'data' as an empty array
    # opens the company.json file. "r" opens the file for reading (while "a" would open the file for the purpose of appending)
    with open("data/company.json", "r") as json_data:
        # the 'data' array will contain the data in the company.json file
        data = json.load(json_data)
    # when we navigate to about.html, the template will be returned
    return render_template("about.html", page_title="About", company=data)


# whenever we look at our 'about' url, and there is something after it, that will be passed into the about_member function as 'member_name'
@app.route("/about/<member_name>")
def about_member(member_name):  # takes the member_name
    member = {}  # will store the data in

    # opens the company.json file. "r" opens the file for reading (while "a" would open the file for the purpose of appending)
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)  # converts the data into JSON
        for obj in data:  # for each object in the data array
            # if the url is the same as the member_name (the thing after our /about url)
            if obj["url"] == member_name:
                member = obj  # sets the member to the url

    # loads the member.html template and sets the member type to the member
    return render_template("member.html", member=member)


# states that both GET and POST methods are allowed
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}. we have recieved your message!".format(
            request.form["name"]))
    # when we navigate to contact.html, the template will be returned
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    # when we navigate to careers.html, the template will be returned
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":  # __main__ is the name of the default module in python
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", "5000")),
            debug=True)  # allows for easier debugging