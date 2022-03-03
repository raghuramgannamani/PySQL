#Gannamani Raghu Ram
#W0466140
#PROG 1007 Assignment 2

#Auto Insurance

def main():
        #Input Details of customer
    Gender = input("Are you 'Male' or 'Female':")
    Age = int(input("Enter your age:"))
    Price = float(input("Enter thr purchase price of the Vehicle:"))

    #if Male respective to age

    if Gender == 'Male' and Age >=15 and Age <25 :
            print("Your monthly insurance will be: ${0:.2f}".format((Price*(0.25))/12))
    elif Gender == 'Male' and Age >=25 and Age <40 :
            print("Your monthly insurance will be: ${0:.2f}".format((Price*(0.17))/12))
    elif Gender == 'Male' and Age >=40 and Age <70 :
            print("Your monthly insurance will be: ${0:.2f}".format((Price*(0.10))/12))

            #if female respective to age
    elif Gender == 'Female' and Age >=15 and Age <25 :
            print("Your monthly insurance will be: ${0:.2f}".format((Price*(0.20))/12))
    elif Gender == 'Female' and Age >=25 and Age <40 :
            print("Your monthly insurance will be: ${0:.2f}".format((Price*(0.15))/12))
    elif Gender == 'Female' and Age >=40 and Age <70 :
            print("Your monthly insurance will be: ${0:.2f}".format((Price*(0.10))/12))

            #if other gender is entered
    else: print("Gender Error: Restart by entering right Gender, Thank you")
main()