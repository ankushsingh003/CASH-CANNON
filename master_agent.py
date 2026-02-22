import os
from rag_tool import query_offer_mart

class MasterAgent:
    def __init__(self):
        self.name = "CASH-CANNON (Orchestrator)"
        self.context = []
        print(f"[{self.name}] Initialized and ready to assist.")

    def handle_user_input(self, user_text):
        """
        Main logic for the orchestrator to decide the next step.
        """
        user_text_lower = user_text.lower()
        
        # 1. Check if the user is asking a general question (RAG candidate)
        if any(word in user_text_lower for word in ["interest", "rate", "tenure", "limit", "eligibility", "document", "kyc", "faq"]):
            print(f"[{self.name}] Consulting knowledge base (RAG)...")
            kb_info = query_offer_mart(user_text)
            response = f"Based on our current policies:\n{kb_info}\n\nWould you like to start your application process?"
            return response
        
        # 2. Check for intent to start a loan process
        if any(word in user_text_lower for word in ["apply", "start", "loan", "process"]):
            return f"[{self.name}] Great! I am now handing you over to our Sales Agent to discuss your requirements (Amount, Tenure, etc.)."
        
        # 3. Default fallback
        return f"[{self.name}] I'm here to help you with Personal Loans. You can ask about our rates, eligibility, or say 'Apply' to get started."

def chat_loop():
    agent = MasterAgent()
    print("\n--- Tata Capital AI Sales Assistant ---")
    print("Type 'exit' or 'quit' to stop.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
            
        response = agent.handle_user_input(user_input)
        print(f"\nAI: {response}\n")

if __name__ == "__main__":
    # For this step, we run a local simulation of the conversation flow
    chat_loop()
