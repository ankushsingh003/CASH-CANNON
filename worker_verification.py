import json
import os

class VerificationAgent:
    def __init__(self, crm_data_path="dummy_customers.json"):
        self.name = "Verification Agent"
        self.crm_data_path = crm_data_path
        self._load_crm_data()

    def _load_crm_data(self):
        """Mock CRM server: Loads customer data from a JSON file."""
        if os.path.exists(self.crm_data_path):
            with open(self.crm_data_path, "r") as f:
                self.crm_data = json.load(f)
        else:
            self.crm_data = []
            print(f"[{self.name}] Warning: CRM data file not found at {self.crm_data_path}")

    def verify_customer(self, customer_id):
        """
        Simulates KYC verification by checking if the customer exists in the dummy CRM.
        Returns phone and address if found.
        """
        print(f"[{self.name}] Accessing Dummy CRM for Customer ID: {customer_id}...")
        
        customer = next((c for c in self.crm_data if c["customer_id"] == customer_id), None)
        
        if customer:
            return {
                "status": "VERIFIED",
                "details": {
                    "phone": customer["phone"],
                    "address": customer["address"]
                },
                "message": f"Customer {customer['name']} verified. KYC details confirmed."
            }
        else:
            return {
                "status": "NOT_FOUND",
                "message": "Customer ID not found in CRM. Verification failed."
            }

if __name__ == "__main__":
    # Test Verification Agent
    agent = VerificationAgent()
    # Testing with first customer in dummy_customers.json (Arjun Sharma - C001)
    result = agent.verify_customer("C001")
    print(f"Result: {result}")
