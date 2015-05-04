from flask import session
from petsy import errors
from petsy.api import Api
import yaml
from util.objectdict import ObjectView

class ApiProvider(object):
    def __init__(self):
        # configuration for etsy
      config = yaml.load(open('config.yml', 'r').read())
      self.etsy_config = ObjectView(config['etsy'])

    # Factory method
    def factory(self, etsy_config=None):
        if etsy_config == None:
            etsy_config = self.etsy_config

        if session['access_token_secret'] == None:
            raise InvalidSessionException('There must be a valid session to access this resource.')

        return Api(
            consumer_key=etsy_config.consumer_key,
            consumer_secret=etsy_config.consumer_secret,
            access_token=session['access_token'],
            access_token_secret=session['access_token_secret']
        )

    # Get config
    def get_config(self):
        return self.etsy_config