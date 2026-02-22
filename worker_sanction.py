import datetime
import os

class SanctionLetterAgent:
    def __init__(self):
        self.name = "CASH-CANNON"

    def generate_letter(self, customer_name, loan_amount, interest_rate, tenure):
        """
        Simulates the generation of an automated sanction letter.
        In a real app, this would use a library like ReportLab or FPDF to create a real PDF.
        """
        date_today = datetime.datetime.now().strftime("%Y-%m-%d")
        
        letter_content = f"""
====================================================
            CASH-CANNON SANCTION DEPLOYMENT
====================================================
Date: {date_today}

To,
{customer_name}

Subject: Sanction of Personal Loan

Dear {customer_name},

We are pleased to inform you that your application for a personal loan has been approved. 
The terms of the sanction are as follows:

1. Sanctioned Amount  : ₹{loan_amount}
2. Interest Rate      : {interest_rate}
3. Loan Tenure        : {tenure}
4. Processing Fee     : 2% of the loan amount

Terms and Conditions:
- The loan is subject to final document verification.
- Disbursement will occur within 24-48 business hours.

Thank you for choosing Tata Capital.

Digitally Signed,
Tata Capital AI Controller
====================================================
"""
        # Save to a text file for simulation
        filename = f"sanction_letter_{customer_name.replace(' ', '_')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(letter_content)
        
        print(f"[{self.name}] Sanction letter generated successfully: {filename}")
        return {
            "status": "SUCCESS",
            "file_path": filename,
            "message": f"Sanction letter for {customer_name} has been generated."
        }

if __name__ == "__main__":
    # Test Sanction Letter Agent
    agent = SanctionLetterAgent()
    result = agent.generate_letter("Arjun Sharma", 500000, "10.99%", "60 months")
    print(f"Result: {result}")
