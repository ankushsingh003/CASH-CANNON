class SalesAgent:
    def __init__(self):
        self.name = "Sales Agent"

    def negotiate_loan(self, customer_need_amount, credit_score):
        """
        Simulates negotiation based on amount and credit score.
        In a real scenario, this would use RAG or a lookup table.
        """
        base_rate = 10.99
        if credit_score < 750:
            offered_rate = base_rate + 2.0
        else:
            offered_rate = base_rate
            
        print(f"[{self.name}] Negotiating for amount: ₹{customer_need_amount}")
        
        return {
            "offered_rate": f"{offered_rate}%",
            "tenure": "60 months",
            "message": f"Based on your requirements, we can offer an interest rate of {offered_rate}% for a tenure of 60 months."
        }

if __name__ == "__main__":
    # Test Sales Agent
    agent = SalesAgent()
    result = agent.negotiate_loan(500000, 760)
    print(f"Result: {result}")
