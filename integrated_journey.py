from master_agent import MasterAgent
from worker_sales import SalesAgent
from worker_verification import VerificationAgent
from worker_underwriting import UnderwritingAgent
from worker_sanction import SanctionLetterAgent
import time

class IntegratedLoanJourney:
    def __init__(self):
        self.master = MasterAgent()
        self.sales = SalesAgent()
        self.verification = VerificationAgent()
        self.underwriting = UnderwritingAgent()
        self.sanction = SanctionLetterAgent()
        self.current_customer = None

    def run(self):
        print("\n" + "="*50)
        print("   CASH-CANNON: THE HIGH-VELOCITY LOAN SWARM")
        print("="*50)
        print("\nWelcome! You can ask about our loans or say 'Apply' to start.")

        while True:
            user_input = input("\nYou: ").strip()
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Thank you for visiting Tata Capital!")
                break

            # 1. Master Agent identifies intent
            response = self.master.handle_user_input(user_input)
            
            # If Master Agent hands over to Sales
            if "handing you over to our Sales Agent" in response:
                print(f"\nAI: {response}")
                self.start_application_flow()
            else:
                # Default RAG or general information
                print(f"\nAI: {response}")

    def start_application_flow(self):
        print("\n" + "-"*30)
        print("STEP 1: CUSTOMER IDENTIFICATION")
        custom_name = input("[Identification] Please enter your Full Name: ").strip()
        customer_id = input("[Verification] Please enter your Customer ID (e.g., C001 to C010): ").strip().upper()
        
        v_result = self.verification.verify_customer(customer_id)
        if v_result["status"] != "VERIFIED":
            print(f"\nAI: {v_result['message']}")
            return

        print(f"\nAI: Customer profile verified. Proceeding with name: {custom_name}")
        time.sleep(1)

        print("\n" + "-"*30)
        print("STEP 2: SALES & NEGOTIATION")
        try:
            amount = int(input("[Sales] How much loan amount do you require? (₹): ").strip())
        except ValueError:
            print("\nAI: Invalid amount entered. Cancelling process.")
            return

        # Fetch customer credit score for negotiation logic
        # In a real app, this would be passed via shared state
        customer_data = next((c for c in self.underwriting.customers if c["customer_id"] == customer_id), None)
        s_result = self.sales.negotiate_loan(amount, customer_data["credit_score"])
        print(f"\nAI: {s_result['message']}")
        
        time.sleep(1)

        print("\n" + "-"*30)
        print("STEP 3: UNDERWRITING DECISION")
        print("[Underwriting] Evaluating your eligibility based on Tata Capital policies...")
        u_result = self.underwriting.evaluate_loan(customer_id, amount)
        
        if u_result["status"] == "REJECTED":
            print(f"\n" + "!"*40)
            print("LOAN APPLICATION REJECTED")
            print(f"Reason: {u_result['reason']}")
            print("!"*40)
        
        elif u_result["status"] == "CONDITIONALLY_APPROVED":
            print(f"\n" + "?"*40)
            print("CONDITIONAL APPROVAL")
            print(f"Status: {u_result['message']}")
            print("Please upload your salary slip at our nearest branch or portal.")
            print("?"*40)

        elif u_result["status"] == "APPROVED_INSTANT":
            print(f"\n" + "*"*40)
            print("CONGRATULATIONS! LOAN APPROVED INSTANTLY")
            print(u_result["message"])
            print("*"*40)
            
            print("\n" + "-"*30)
            print("STEP 4: FIRING THE CASH-CANNON")
            l_result = self.sanction.generate_letter(
                custom_name, 
                amount, 
                s_result["offered_rate"], 
                s_result["tenure"]
            )
            print(f"\nAI: {l_result['message']}")
            print(f"You can find your letter here: {l_result['file_path']}")

if __name__ == "__main__":
    journey = IntegratedLoanJourney()
    journey.run()
