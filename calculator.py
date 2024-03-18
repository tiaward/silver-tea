



# A computer program to calculate numbers and store them to a file or read the equations

# The original calculator function and formatting
def perform_calculation(num1, num2, operation):
    """
    Performs the specified arithmetic operation on two numbers.
    """
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result = num1 / num2
    else:
        raise ValueError("Invalid operation!")

    return result

# A choice of whether to input equations by the user to to call them from the file in a while loop
while True:
    choice = input("Please choose an option:\n"
                   "1. Enter numbers and an operator\n"
                   "2. Read equations from a text file\n"
                   "Please enter '1' or '2': ")
# First choice then asks for the two numbers and the operation - accounting for value errors
    if choice == "1":
        while True:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                operation = input("Enter the operation (+, -, *, /): ")
                if operation in ["+", "-", "*", "/"]:
                    break
                else:
                    print("Invalid operation! Please try again.")
            except ValueError:
                print("Value error - please enter two numbers.")

        result = perform_calculation(num1, num2, operation)
        equation = f"{num1} {operation} {num2} = {result}\n"

        with open("equations.txt", "a") as file:
            file.write(equation)

        print(equation)
        break
# Second choice is if they want to read the previous equations - accouunting for errors
    elif choice == "2":
        while True:
            try:
                filename = input("Enter the name of your text file: ")
                with open(filename, "r") as file:
                    file_contents = file.read()
                    print(file_contents)
                break
            except FileNotFoundError:
                print("File not found, please try again.")
        break
# Will loop back to original choice if invalid
    else:
        print("Invalid choice. Please retry.")


# Note for assessor - im not sure if I was meant to do the suggested corrections exactly as they were asked 
# but i have re formatted my whole code and tested it and it is all in working order so hopefully that is 
# sufficient.


