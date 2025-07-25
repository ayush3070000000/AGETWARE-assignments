from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from utils import lend_money, make_payment, get_ledger, get_account_overview

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

@app.route('/')
def serve_home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

@app.route('/lend', methods=['POST'])
def lend():
    data = request.json
    return jsonify(lend_money(data))

@app.route('/payment', methods=['POST'])
def payment():
    data = request.json
    return jsonify(make_payment(data))

@app.route('/ledger/<loan_id>', methods=['GET'])
def ledger(loan_id):
    return jsonify(get_ledger(loan_id))

@app.route('/overview/<customer_id>', methods=['GET'])
def overview(customer_id):
    return jsonify(get_account_overview(customer_id))

if __name__ == '__main__':
    app.run(debug=True)
