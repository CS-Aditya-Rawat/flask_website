from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('login')
def login():
    return render_template("login.html")

@auth.route('logout')
def logout():
    return "<h1>LOGOUT</h1>"

@auth.route('sign-up')
def signup():
    return render_template("signUp.html")

