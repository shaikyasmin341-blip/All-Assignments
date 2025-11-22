# ------------------------------------------------------------
# Task #2: Bias Detection in AI-Generated Code
# ------------------------------------------------------------
# Goal:
# AI tools sometimes generate biased logic. This example shows
# how gender bias appears in AI-generated code and how to fix it.
# ------------------------------------------------------------


def approve_loan(applicant_name, applicant_gender):
    if applicant_gender == "male":
        return f"Loan approved for {applicant_name}."
    else:
        return f"Loan denied for {applicant_name}."

def approve_loan_unbiased(applicant_name, applicant_income, applicant_credit_score):
    MIN_INCOME = 50000
    MIN_CREDIT_SCORE = 700

    if applicant_income >= MIN_INCOME and applicant_credit_score >= MIN_CREDIT_SCORE:
        return f"Loan approved for {applicant_name}."
    else:
        return f"Loan denied for {applicant_name}."


print(approve_loan_unbiased("Alice", 60000, 720))   # Loan approved
print(approve_loan_unbiased("Bob", 40000, 680))     # Loan denied
print(approve_loan_unbiased("Charlie", 55000, 710)) # Loan approved
print(approve_loan_unbiased("Diana", 45000, 690))   # Loan denied
