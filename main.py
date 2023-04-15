from flask import Flask, render_template

app = Flask(__name__)

# msg = "Hello, Amrit"
website_name = "Readaholic"
data = {
    "website_name": "Readaholic",
    "author": "Amrit"
}

# root route (directs to root directory of project)
@app.route("/")
def home():
    # rendering(returning) HTML file
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

# grouping of routes together
# @app.route("/route1")
# @app.route("/route2")
# @app.route("/route3")
# def route1():
#     return f"<h1>{msg}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
