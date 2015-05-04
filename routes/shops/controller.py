from flask import Blueprint, jsonify
from ..providers import ApiProvider

blueprint = Blueprint('shops', __name__)
provider = ApiProvider()

# Get - The given shop
@blueprint.route('/shops/<shop_id>', methods=['GET'])
def __get_shop(shop_id):
    api = provider.factory()
    r = api.shops.get_shop(shop_id)
    return jsonify(**r)