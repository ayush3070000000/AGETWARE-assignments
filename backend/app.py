from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import lend_money, make_payment, get_ledger, get_account_overview

app = Flask(__name__)
CORS(app)  # 🔴 This is critical to allow frontend to talk to backend

@app.route('/')
def home():
    return "✅ Bank Loan System API is running!"

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
  