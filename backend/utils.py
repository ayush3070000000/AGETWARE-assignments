# 📁 backend/utils.py
import json
import os

data_file = os.path.join(os.path.dirname(__file__), 'data.json')

# Load data
if os.path.exists(data_file):
    with open(data_file, 'r') as f:
        loans = json.load(f)
else:
    loans = []

def save_loans():
    with open(data_file, 'w') as f:
        json.dump(loans, f, indent=2)

def lend_money(data):
    customer_id = data['customer_id']
    P = float(data['loan_amount'])
    N = float(data['loan_period'])
    R = float(data['interest_rate'])
    loan_id = "L" + str(len(loans) + 1)

    interest = P * N * (R / 100)
    total = P + interest
    emi = total / (N * 12)

    loan = {
        "loan_id": loan_id,
        "customer_id": customer_id,
        "principal": P,
        "period": N,
        "rate": R,
        "interest": interest,
        "total": total,
        "emi": round(emi, 2),
        "paid": 0,
        "transactions": []
    }

    loans.append(loan)
    save_loans()

    return {
        "message": "Loan created successfully.",
        "loan_id": loan_id,
        "total_amount": total,
        "monthly_emi": round(emi, 2)
    }

def make_payment(data):
    loan_id = data['loan_id']
    amount = float(data['amount'])
    pay_type = data.get('type', 'EMI')

    loan = next((l for l in loans if l['loan_id'] == loan_id), None)

    if not loan:
        return {"error": "Loan not found."}, 404

    loan['paid'] += amount
    loan['transactions'].append({
        "amount": amount,
        "type": pay_type,
        "date": data.get("date", "now")
    })

    save_loans()
    return {"message": "Payment recorded successfully."}

def get_ledger(loan_id):
    loan = next((l for l in loans if l['loan_id'] == loan_id), None)

    if not loan:
        return {"error": "Loan not found."}, 404

    balance = loan['total'] - loan['paid']
    emi_left = int((balance + loan['emi'] - 1) // loan['emi'])  # Ceiling

    return {
        "loan_id": loan['loan_id'],
        "remaining_balance": round(balance, 2),
        "monthly_emi": loan['emi'],
        "emi_left": emi_left,
        "transactions": loan['transactions']
    }

def get_account_overview(customer_id):
    customer_loans = [l for l in loans if l['customer_id'] == customer_id]

    if not customer_loans:
        return {"error": "No loans found for this customer."}, 404

    overview = []
    for loan in customer_loans:
        balance = loan['total'] - loan['paid']
        emi_left = int((balance + loan['emi'] - 1) // loan['emi'])

        overview.append({
            "loan_id": loan['loan_id'],
            "loan_amount": loan['principal'],
            "total_amount": loan['total'],
            "interest": loan['interest'],
            "emi": loan['emi'],
            "paid": loan['paid'],
            "emi_left": emi_left
        })

    return {"customer_id": customer_id, "loans": overview}
