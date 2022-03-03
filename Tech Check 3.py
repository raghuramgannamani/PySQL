#W0466140
#Raghu Ram Gannamani
#Tech Check 2
print("Tax Withholding Calculator")
WeeklySalary=float(input('Please enter the full amount of your weekly salary:$'))
NumofDependents=int(input('How many dependents do you have?:'))
def Tax(WS,ND):
    ProvincialTax = 0.06*WS
    FederalTax = 0.25*WS
    DependentTax = 0.02*WS*ND
    print("Provincial Tax Withheld:$",ProvincialTax)
    print("Federal Tax Withheld:$",FederalTax)
    print("Dependent Deduction for",ND,"Dependents:$",DependentTax)
    Total = ProvincialTax+FederalTax-DependentTax
    print("Total Withheld:$",Total)
    print("Total Take-Home Pay:$",WeeklySalary-Total)
Tax(WeeklySalary, NumofDependents)