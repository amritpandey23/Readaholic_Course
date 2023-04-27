from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from readaholic import app, db, bcrypt
from readaholic.forms import AdminLoginForm, AdminRegisterationForm, AddBookForm
from readaholic.models import User, Book


# root route (directs to root directory of project)
@app.route("/")
@login_required
def home():
    book_data = Book.query.all()
    return render_template("home.html", data=book_data)


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
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for('home'))

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
                login_user(user)
                flash("Successfully log in!", "success")
                return redirect(url_for("home"))
            else:
                flash("You've entered wrong password, please try again!", "danger")
    return render_template("login.html", form=form)


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    flash("You've successfully logged out", "success")
    return redirect(url_for("login"))


@app.route("/add_book", methods=["GET", "POST"])
@login_required
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        print(form.data)
        _book_title = form.data['book_title']
        _author_name = form.data['author_name']
        _isbn = form.data['isbn']
        _genre = form.data['genre']
        _shop_link = form.data['shop_link']
        _rating = form.data['rating']
        _cover_image_file = form.data['cover_image_file']
        _tiny_summary = form.data['tiny_summary']
        book = Book(
            title = _book_title,
            author = _author_name,
            isbn = _isbn,
            genre = _genre,
            shop_link = _shop_link,
            rating = _rating,
            tiny_summary = _tiny_summary
        )
        try:
            db.session.add(book)
            db.session.commit()
            flash("Successfully added the book", "success")
        except:
            flash("Something went wrong while adding book!", "danger")
    return render_template("add_book.html", form=form)
