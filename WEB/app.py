import sys
import os
from flask import Flask, render_template, request, jsonify

# Add the parent directory to sys.path so we can import our agents
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from master_agent import MasterAgent
from worker_sales import SalesAgent
from worker_verification import VerificationAgent
from worker_underwriting import UnderwritingAgent
from worker_sanction import SanctionLetterAgent

app = Flask(__name__)

# Initialize agents
master = MasterAgent()
sales = SalesAgent()
verification = VerificationAgent()
underwriting = UnderwritingAgent()
sanction = SanctionLetterAgent()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    
    response = master.handle_user_input(user_input)
    
    # Check if we should transition to the application flow
    start_app = "handing you over to our Sales Agent" in response
    
    return jsonify({
        "response": response,
        "start_app": start_app
    })

@app.route('/api/verify', methods=['POST'])
def verify():
    customer_id = request.json.get('customer_id')
    result = verification.verify_customer(customer_id)
    return jsonify(result)

@app.route('/api/underwrite', methods=['POST'])
def underwrite():
    data = request.json
    customer_id = data.get('customer_id')
    amount = int(data.get('amount'))
    
    # 1. Negotiation (Implicitly handled here to get the rate for the sanction)
    # In a real app, this would be more decoupled
    customer_data = next((c for c in underwriting.customers if c["customer_id"] == customer_id), None)
    s_result = sales.negotiate_loan(amount, customer_data["credit_score"])
    
    # 2. Evaluation
    u_result = underwriting.evaluate_loan(customer_id, amount)
    
    # 3. Sanction if approved
    if u_result["status"] == "APPROVED_INSTANT":
        l_result = sanction.generate_letter(
            customer_data["name"], 
            amount, 
            s_result["offered_rate"], 
            s_result["tenure"]
        )
        u_result["letter_url"] = l_result["file_path"]
        u_result["offered_rate"] = s_result["offered_rate"]
        u_result["name"] = customer_data["name"]

    return jsonify(u_result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
