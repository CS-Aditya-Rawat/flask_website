from flask_dance.contrib.github import make_github_blueprint, github
from flask import url_for, render_template, redirect
from dotenv import load_dotenv

envr = load_dotenv(".env")


github_blueprint = make_github_blueprint('github_blueprint', __name__)


@github_blueprint.route("/")
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            print(account_info_json)
            return render_template("home.html")
    return render_template("home.html")
