from flask import Blueprint, jsonify, session, request, redirect
from util.objectdict import ObjectView
import requests
from petsy.api import Api
from ..providers import ApiProvider
from petsy.auth.api import EtsyAuth

blueprint = Blueprint('auth', __name__)
provider = ApiProvider()

# variables that relate to the etsy oauth auth flow
callback_uri = 'http://localhost:5000/authorize'
etsy_auth = EtsyAuth(['email_r', 'listings_r', 'transactions_r', 'profile_r'])
etsy_config = provider.get_config()

# Login route
# If the user doesn't have a session, this route can be called
# to log the user in and store a session
@blueprint.route('/login', methods=['GET'])
def login():
    auth_url = etsy_auth.fetch_authorization_url(
        etsy_config.consumer_key,
        etsy_config.consumer_secret,
        callback_uri,
        session
    )
    return redirect(auth_url, code=302)

# Authorize route
# This route handles the callback from etsy authorize
@blueprint.route('/authorize', methods=['GET'])
def authorize():
    etsy_auth.handle_authorization(
        etsy_config.consumer_key, 
        etsy_config.consumer_secret, 
        request, 
        session
    )
    return jsonify(**{ 'ok': True })