import json
import os

class UnderwritingAgent:
    def __init__(self, crm_data_path="dummy_customers.json"):
        self.name = "Underwriting Agent"
        self.crm_data_path = crm_data_path
        self._load_customer_data()

    def _load_customer_data(self):
        """Mock Bureau API: Loads customer financial data."""
        if os.path.exists(self.crm_data_path):
            with open(self.crm_data_path, "r") as f:
                self.customers = json.load(f)
        else:
            self.customers = []

    def evaluate_loan(self, customer_id, requested_amount, tenure_months=60):
        """
        Implements the core underwriting logic from the challenge.
        """
        print(f"[{self.name}] Evaluating Loan for Customer: {customer_id}...")
        
        customer = next((c for c in self.customers if c["customer_id"] == customer_id), None)
        if not customer:
            return {"status": "REJECTED", "reason": "Customer not found in Credit Bureau database."}

        credit_score = customer["credit_score"]
        pre_approved_limit = customer["pre_approved_limit"]
        monthly_income = customer["monthly_income"]

        # 1. Credit Score Check
        if credit_score < 700:
            return {
                "status": "REJECTED",
                "reason": f"Credit score {credit_score} is below the minimum threshold of 700."
            }

        # 2. Amount vs Limit Logic
        if requested_amount > 2 * pre_approved_limit:
            return {
                "status": "REJECTED",
                "reason": f"Requested amount ₹{requested_amount} exceeds 2x the pre-approved limit (₹{pre_approved_limit})."
            }

        if requested_amount <= pre_approved_limit:
            return {
                "status": "APPROVED_INSTANT",
                "message": f"Loan of ₹{requested_amount} approved instantly! (Amount <= Pre-approved limit)."
            }

        # 3. Request Salary Slip & EMI Check (Amount > Limit but <= 2x Limit)
        # Assuming simple interest for EMI calculation demo purposes: (P + (P*R*T))/T
        # Approx 12% annual rate = 1% monthly
        estimated_monthly_emi = (requested_amount * 1.6) / tenure_months # Simplified multiplier for 60m @ 12%
        
        emi_to_income_ratio = estimated_monthly_emi / monthly_income

        if emi_to_income_ratio <= 0.5:
            return {
                "status": "CONDITIONALLY_APPROVED",
                "action_required": "SALARY_SLIP_UPLOAD",
                "message": f"Loan of ₹{requested_amount} conditionally approved. Please upload your salary slip for final verification (EMI is {int(emi_to_income_ratio*100)}% of income)."
            }
        else:
            return {
                "status": "REJECTED",
                "reason": f"EMI (₹{int(estimated_monthly_emi)}) exceeds 50% of your monthly income (₹{monthly_income})."
            }

if __name__ == "__main__":
    # Test Underwriting Agent
    agent = UnderwritingAgent()
    
    # Test Case 1: Instant Approval (Arjun Sharma, Limit 500k, Score 750, Request 400k)
    print("\nTest Case 1: ", agent.evaluate_loan("C001", 400000))
    
    # Test Case 2: Conditional Approval (Ananya Reddy, Limit 400k, Score 720, Request 700k)
    print("\nTest Case 2: ", agent.evaluate_loan("C004", 700000))
    
    # Test Case 3: Rejection - Low Credit Score (Rohan Gupta, Score 650)
    print("\nTest Case 3: ", agent.evaluate_loan("C005", 200000))
