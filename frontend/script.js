let baseUrl = "http://localhost:5000"; // Flask backend

// Lend Money
function lendMoney() {
  let data = {
    customer_id: document.getElementById("lend_customer").value,
    loan_amount: document.getElementById("lend_amount").value,
    loan_period: document.getElementById("lend_years").value,
    interest_rate: document.getElementById("lend_rate").value,
  };

  fetch(baseUrl + "/lend", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })
    .then((res) => res.json())
    .then((result) => {
      document.getElementById("lend_result").textContent = JSON.stringify(result, null, 2);
    })
    .catch((err) => {
      console.error("Lend Error:", err);
      document.getElementById("lend_result").textContent = "❌ Error: " + err;
    });
}

// Make Payment
function makePayment() {
  let data = {
    loan_id: document.getElementById("pay_loan_id").value,
    amount: document.getElementById("pay_amount").value,
    type: document.getElementById("pay_type").value,
  };

  fetch(baseUrl + "/payment", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })
    .then((res) => res.json())
    .then((result) => {
      document.getElementById("pay_result").textContent = JSON.stringify(result, null, 2);
    })
    .catch((err) => {
      console.error("Payment Error:", err);
      document.getElementById("pay_result").textContent = "❌ Error: " + err;
    });
}

// Get Loan Ledger
function getLedger() {
  let loanId = document.getElementById("ledger_loan_id").value;

  fetch(baseUrl + `/ledger/${loanId}`)
    .then((res) => res.json())
    .then((result) => {
      document.getElementById("ledger_result").textContent = JSON.stringify(result, null, 2);
    })
    .catch((err) => {
      console.error("Ledger Error:", err);
      document.getElementById("ledger_result").textContent = "❌ Error: " + err;
    });
}

// Get Customer Overview
function getOverview() {
  let customerId = document.getElementById("overview_customer").value;

  fetch(baseUrl + `/overview/${customerId}`)
    .then((res) => res.json())
    .then((result) => {
      document.getElementById("overview_result").textContent = JSON.stringify(result, null, 2);
    })
    .catch((err) => {
      console.error("Overview Error:", err);
      document.getElementById("overview_result").textContent = "❌ Error: " + err;
    });
}

// Optional: test connection when page loads
window.addEventListener("load", () => {
  fetch(baseUrl)
    .then(res => res.text())
    .then(data => console.log("✅ Connected to Flask:", data))
    .catch(err => console.error("❌ Flask not reachable:", err));
});
