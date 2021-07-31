import os

from flask import Flask, jsonify
from flask import url_for

from dotenv import load_dotenv
load_dotenv()

import requests

from authlib.integrations.flask_client import OAuth

LICHESS_HOST = os.getenv("LICHESS_HOST", "https://lichess.org")

app = Flask(__name__)
app.secret_key = "{8H7HuEmM6fSQCjG7}"

app.config['LICHESS_CLIENT_ID'] =  "lichess-oauth-flask"

app.config['LICHESS_AUTHORIZE_URL'] = f"{LICHESS_HOST}/oauth"
app.config['LICHESS_ACCESS_TOKEN_URL'] = f"{LICHESS_HOST}/api/token"

oauth = OAuth(app)
oauth.register('lichess', client_kwargs={"code_challenge_method": "S256"})

@app.route('/')
def login():
    redirect_uri = url_for("authorize", _external=True)
    """
    If you need to append scopes to your requests, add the `scope=...` named argument
    to the `.authorize_redirect()` method. For admissible values refer to https://lichess.org/api#section/Authentication. 
    Example with scopes for allowing the app to read the user's email address:
    `return oauth.lichess.authorize_redirect(redirect_uri, scope="email:read")`
    """
    
    return oauth.lichess.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    token = oauth.lichess.authorize_access_token()
    bearer = token['access_token']
    headers = {'Authorization': f'Bearer {bearer}'}
    response = requests.get(f"{LICHESS_HOST}/api/account", headers=headers)
    return jsonify(**response.json())

@app.route('/game/<adversaire>' , methods=['POST','GET'])
def create_game(adversaire):
    token = oauth.lichess.authorize_access_token()
    bearer = token['access_token']
    print(bearer)
    headers = {'Authorization': f'Bearer {bearer}'}
    print('hey')
    print(token)
    params = {
        'rated' : False,
        'clock.limit' : 10800,
        'clock.increment' : 60,
        'days' : 15,
    }
    #response = requests.post(f"{LICHESS_HOST}/api/challenge/{adversaire}", headers=headers, params=params)
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)
