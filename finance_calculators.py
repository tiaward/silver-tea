
# user inputs bond or investment, 'if' statements will recognise different forms of either word due to 'or' function
# inputs are recognised as integers because of the 'int' extention
# the 'r' is divided by 100 for the formula and converted into 'v'
# formulas for compound and simple interest will output either answer.
# elif funtion used for the bond option
# same process as investment option with inputs as integers and the formula to output
# else function used to display error message if non valid answer is inputted


import math

choose=str(input("""
investment - to calculate the amount of interest you'll earn on your investment
bond -       to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' to proceed:"""))
             


if choose == "investment" or choose == "Investment" or choose == "INVESTMENT":
    P=int(input("How much money are you depositing?"))
    r=int(input("What is your interest rate?(enter without percentage sign)"))
    t=int(input("How many years do you plan on investing?"))
    interest=input("Would you like simple or compound interest?")
    v=r/100
    if interest=="compound"or interest=="Compound"or interest=="COMPOUND":
        A=P * math.pow((1+v),t)
        print(A)
    elif interest=="simple"or interest=="Simple"or interest=="SIMPLE":
        A=P*(1+v*t)
        print(A)


elif choose == "bond" or choose == "Bond" or choose == "BOND":
    p=int(input("What is the present value of the house?"))
    i=int(input("What is your interest rate?"))
    n=int(input("How many months do you plan to take to repay the bond?"))
    k=i/100/12
    repayment=(k*p)/(1-(1+k)**(-n))
    print(repayment)

else:
    print("Invalid answer. Please try again.")