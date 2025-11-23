#OVERVIEW:
This project helps users estimate how much loan they may qualify for using:
Household income
Personal savings
Collateral value
EMI affordability
Interest rate and tenure
It follows real-world lending principles like Debt-to-Income ratio, LTV (Loan-to-Value), and income multipliers.

#FEATURES:
 Accurate EMI calculation
 Income and collateral-based loan limits
 EMI stress testing to avoid over-borrowing
 EMI comparisons for 5, 10, and 20 years
 User-friendly command-line prompts
 Input validation and safe error handling
 No external libraries required

 #PROJECT STRUCTURE:

 loan_assessor.py   # Main program with EMI and loan calculations
 README.md          # Documentation

#CODE LOGIC OVERVIEW:

1.EMI Calculation
  EMI = P * r * (1+r)^n / ((1+r)^n - 1)
  where
    p= principal
    r= monthly interest rate
    n= total months

2.Loan Eligibility Calculation
  The tool calculates:
  Income Loan Limit: 5 × annual income
  Collateral Loan Limit: 80% of collateral
  EMI Affordability: 45% of monthly income
  Stress Test: checks EMI of max loan
  Final loan is rounded down to nearest 1,000.

#ERROR HANDLING:
  1.Invalid numeric inputs are caught using try/except
  2.User is re-prompted when entering wrong values
  3.Prevents negative or impossible loan outputs

# EXAMPLE OUTPUT


Loan Assessment Summary for Arhaan Kumar

Maximum Loan Capability: 4,000,000.00
(Annual Interest Rate: 8.5%)

Max Affordable Monthly EMI: 33,750.00
Collateral Loan Limit (80% LTV): 1,200,000.00
Income Loan Limit (5x Annual Income): 4,500,000.00

Equated Monthly Installments (EMI) for different tenures:
 - 5 Years: EMI = 82,121.67 per month
 - 10 Years: EMI = 49,598.21 per month
 - 20 Years: EMI = 34,672.77 per month

