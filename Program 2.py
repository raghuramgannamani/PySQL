def main():
    LoanAmount = float(input('Enter the amount of Loan:'))
    InterestRate = float(input('Enter the interest rate(%):'))
    NumOfYears = int(input('Enter the number of Years:'))
    Valuei = InterestRate / 5200
    
    WeeklyPayment = (Valuei / (1-(1+Valuei)**(-52*NumOfYears)) * LoanAmount)
    print("Your Weekly Payment will be: ${0:.2f}". format(WeeklyPayment))

main()