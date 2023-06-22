from flask import Flask, url_for, redirect
from flask_dance.contrib.github import make_github_blueprint, github
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "1234KEY"
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
GITHUB_CLIENT_ID = "c22bcb448fe425add386"
GITHUB_CLIENT_SECRET = "b813d96f548d9117d64f3742cf5e32ba2f1d14eb"

github_blueprint = make_github_blueprint(client_id=GITHUB_CLIENT_ID,
                                         client_secret=GITHUB_CLIENT_SECRET)

app.register_blueprint(github_blueprint, url_prefix='/github_login')


@app.route('/')
def github_login():

    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            print(account_info_json)
            return f'Your Github name is {account_info_json}'

    return '<h1>Request failed!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
