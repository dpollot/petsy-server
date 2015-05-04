from flask import Blueprint, jsonify
from ..providers import ApiProvider

blueprint = Blueprint('listings', __name__)

provider = ApiProvider()

# Get - Shop listings
@blueprint.route('/shops/<shop_id>/listings', methods=['GET'])
def __get_listings(shop_id):
    api = provider.factory()
    r = api.listings.get_listings(shop_id, status='active')
    return jsonify(**r)

# Get - Listing
@blueprint.route('/shops/<shop_id>/listings/<listing_id>', methods=['GET'])
def __get_listing(shop_id, listing_id):
    api = provider.factory()
    r = api.listings.get_listing(listing_id)
    return jsonify(**r)