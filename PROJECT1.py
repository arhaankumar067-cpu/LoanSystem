import math
def calculate_emi(principal, annual_rate, tenure_years):
    """Calculates the Equated Monthly Installment (EMI) for a loan."""
    if annual_rate == 0:
        return principal / (tenure_years * 12)

    monthly_rate = (annual_rate / 12) / 100
    n_payments = tenure_years * 12
    emi = principal * monthly_rate * (1 + monthly_rate)**n_payments / ((1 + monthly_rate)**n_payments - 1)
    return emi

def assess_loan_capability():
    """Asks user for details, calculates loan capability, and provides EMI for different tenures."""
    print("Welcome to the Simplified Loan Capability Assessor!")
    name = input("1. Please enter your full name: ").strip()

    while True:
        try:
            money = float(input("2. Enter your personal savings/money (in local currency): "))
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for your savings.")

    while True:
        try:
            household_income = float(input("3. Enter your total *annual* household income (in local currency): "))
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for annual income.")

    collateral_offered = input("4. Are you offering any collateral (e.g., property, gold)? (yes/no): ").strip().lower()
    collateral_value = 0
    if collateral_offered == 'yes':
        while True:
            try:
                collateral_value = float(input("5. Enter the assessed value of your collateral: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value for collateral value.")
    ANNUAL_INTEREST_RATE = 8.5 
    MAX_DEBT_TO_INCOME_RATIO = 0.45 
    INCOME_MULTIPLIER = 5 
    monthly_income = household_income / 12
    max_affordable_emi = monthly_income * MAX_DEBT_TO_INCOME_RATIO
    collateral_loan_limit = collateral_value * 0.80
    income_loan_limit = household_income * INCOME_MULTIPLIER
    max_loan_pre_emi = min(collateral_loan_limit, income_loan_limit)
    if max_loan_pre_emi > 0:
        emi_stress_test = calculate_emi(max_loan_pre_emi, ANNUAL_INTEREST_RATE, 5)
    else:
        emi_stress_test = 0
    if emi_stress_test > max_affordable_emi:
        monthly_rate = (ANNUAL_INTEREST_RATE / 12) / 100
        n_payments = 5 * 12
        factor = ((1 + monthly_rate)**n_payments - 1) / (monthly_rate * (1 + monthly_rate)**n_payments)
        
        calculated_loan_amount = max_affordable_emi * factor
    else:
        calculated_loan_amount = max_loan_pre_emi
    final_loan_amount = math.floor(calculated_loan_amount / 1000) * 1000
    if final_loan_amount < 0:
        final_loan_amount = 0
    print("\n" + "="*50)
    print(f"Loan Assessment Summary for {name}")
    print("="*50)
    if final_loan_amount <= 0:
        print("Based on the simplified model, a loan is not currently possible.")
        print("   Consider increasing your income or providing valuable collateral.")
        print("="*50)
        return

    print(f"Maximum Loan Capability: **{final_loan_amount:,.2f}**")
    print(f"   (Annual Interest Rate: {ANNUAL_INTEREST_RATE}%)")
    print("-" * 50)
    print(f"   Max Affordable Monthly EMI: {max_affordable_emi:,.2f}")
    print(f"   Collateral Loan Limit (80% LTV): {collateral_loan_limit:,.2f}")
    print(f"   Income Loan Limit (5x Annual Income): {income_loan_limit:,.2f}")
    print("-" * 50)
    tenures = [5, 10, 20]
    print("Equated Monthly Installments (EMI) for different tenures:")

    for tenure in tenures:
        emi = calculate_emi(final_loan_amount, ANNUAL_INTEREST_RATE, tenure)
        print(f"   - **{tenure} Years:** EMI = **{emi:,.2f}** per month")

    print("="*50)
if __name__ == "__main__":
    assess_loan_capability()