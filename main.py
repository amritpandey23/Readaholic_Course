from flask import Flask, render_template
from forms import AdminRegisterationForm, AdminLoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key_33'

# root route (directs to root directory of project)
@app.route("/")
def home():
    # rendering(returning) HTML file
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = AdminRegisterationForm()
    if form.validate_on_submit():
        print(form.data)
    return render_template("register.html", form=form)

@app.route("/login")
def login():
    form = AdminLoginForm()
    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
