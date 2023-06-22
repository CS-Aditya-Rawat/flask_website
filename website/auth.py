from flask import Blueprint, redirect, render_template, request, flash, url_for
from .models import User
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)
@auth.route('login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password= request.form.get('password')

        user = User.query.filter_by(email=email).first()
        print("RECENTLY LOGING USER: ", user.name)
        if user:
            if check_password_hash(user.password, password):
                flash(f"Welcome Back {user.name}", category="success")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect Password", category="error")
        else:
            flash("Email doesn't exist", category="error")
    return render_template("login.html",user=current_user)

@auth.route('logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('sign-up', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        name= request.form.get('name')
        password= request.form.get('password')
        password1= request.form.get('confirm-password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exist", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category='error')
        elif len(name) < 2:
            flash("First name must be greater than 1 character.", category='error')
        elif password != password1:
            flash("Passwords don\'t match.", category='error')
        elif len(password) < 7:
            flash("Password must be atleast 7 characters.", category='error')
        else:
            new_user = User(name=name, email=email, password=generate_password_hash(password, method="scrypt"))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created!", category='success')
            login_user(new_user, remember=True)
            return redirect(url_for("views.home"))

    return render_template("signUp.html", user=current_user)

