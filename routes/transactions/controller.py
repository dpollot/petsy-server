from flask import Blueprint, jsonify
from ..providers import ApiProvider

blueprint = Blueprint('transactions', __name__)
provider = ApiProvider()

# Get - Shop transactions
@blueprint.route('/shops/<shop_id>/transactions', methods=['GET'])
def get_transactions(shop_id):
    api = provider.factory()
    r = api.transactions.get_transactions(shop_id)
    return jsonify(**r)