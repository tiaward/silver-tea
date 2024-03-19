


# a program to ask a user for thier name, while checking the input is valid.




# asking for the full name 
full_name = input("Please enter your full name: ")

# if statements to specify that the name that has been entered is valid
# e.g. under 25 letters, over 4 letters and that they have entered a value
# elif statement to check if it two words using the length and split functions on line 23

if len(full_name) == 0:

    print("You havent entered anything, please enter your full name.")
elif len(full_name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif len(full_name) > 25:
    print("You have entered more than 25 characters, please make sure that you have only entered your full name. ")
elif len(full_name.split()) == 1:
    print("Please enter your first and last name with a space between them.")

else:
    print("Thank you for entering your name, " + full_name)

# a print statement to notify the user that the process is finished.

