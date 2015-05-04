from flask import Flask, jsonify

app = Flask(__name__)
# session key
app.secret_key = 'd041beec-c42b-425a-b138-69c5ca58169d'

# Status route
# Just a quick status endpoint
@app.route('/status')
def status():
    return jsonify(**{'ok': True})

# Register auth routes
from routes.auth.controller import blueprint as auth_module
app.register_blueprint(auth_module)

# Register listings routes
from routes.listings.controller import blueprint as listings_module
app.register_blueprint(listings_module)

# Register shops routes
from routes.shops.controller import blueprint as shops_module
app.register_blueprint(shops_module)

# Register shops routes
from routes.transactions.controller import blueprint as transactions_module
app.register_blueprint(transactions_module)

if __name__ == "__main__":
    app.run(debug=True)
