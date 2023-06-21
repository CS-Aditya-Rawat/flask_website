from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)
@auth.route('login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)

@auth.route('logout')
def logout():
    return "<h1>LOGOUT</h1>"


@auth.route('sign-up', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        name= request.form.get('name')
        password= request.form.get('password')
        password1= request.form.get('confirm-password')

        if len(email) < 4:
            flash("Email must be greater than 4 characters", category='error')
        elif len(name) < 2:
            flash("First name must be greater than 1  character.", category='error')
        elif password != password1:
            flash("Passwords don\'t match.", category='error')
        elif len(password) < 7:
            flash("Password must be atleast 7 characters", category='error')
        else:
            flash("Account Created", category='success')
    return render_template("signUp.html")

