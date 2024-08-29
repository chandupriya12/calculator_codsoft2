def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if the choice is valid
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the calculation based on the user's choice
        if choice == '1':
            result = num1 + num2
            operation = "+"
        elif choice == '2':
            result = num1 - num2
            operation = "-"
        elif choice == '3':
            result = num1 * num2
            operation = "*"
        elif choice == '4':
            if num2 != 0:  # Check to avoid division by zero
                result = num1 / num2
                operation = "/"
            else:
                print("Error: Division by zero is not allowed.")
                return
        else:
            result = None

        # Display the result
        print(f"The result of {num1} {operation} {num2} is: {result}")
    else:
        print("Invalid input. Please select a valid operation.")

# Run the calculator function
calculator()
