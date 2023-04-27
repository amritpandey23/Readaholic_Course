from flask import render_template, flash, redirect, url_for
from readaholic import app, db, bcrypt
from readaholic.forms import AdminLoginForm, AdminRegisterationForm
from readaholic.models import User

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
        _email = form.data['email']
        _password = form.data['password']
        _password = bcrypt.generate_password_hash(_password).decode("utf-8")
        user = User(email=_email, password=_password)
        try:
            db.session.add(user)
            db.session.commit()
            flash("Account successfully created, you may now login", "success")
            return redirect(url_for("login"))
        except:
            flash("Something went wrong with database", "warning")
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        _email = form.data['email']
        _password = form.data['password']
        user = User.query.filter_by(email=_email).first()
        if not user:
            flash(f"No user with email {_email} found! Register today.", "danger")
            return redirect(url_for("register"))
        else:
            if bcrypt.check_password_hash(user.password, _password):
                flash("Successfully log in!", "success")
                return redirect(url_for("home"))
            else:
                flash("You've entered wrong password, please try again!")
    return render_template("login.html", form=form)
