# Declaration of stack array used to evaluate arithmetic expressions in RPN format
stack = []


# Keep on entering elements in stack until user enters 'N'
finished_input = False

while not finished_input:
    # Checks for valid user input for number or operator
    valid_option_1 = False

    while not valid_option_1:
        # Asks the user to enter an item (operator/operand)
        item = input("Enter an operator/operand to append to stack(RPN Format): ")

        # Check if user did not enter a digit and instead entered a string of length larger than 1 or did not enter any value
        if not item.lstrip('-+').replace(".","").isdigit() and len(item) != 1:
            valid_option_1 = False
            print("Please enter a valid number or any of the following operators (+,-,/,*)!")
        else:
            # Check if user input is either a number or any of the operators: +, -, *, /
            if item.lstrip('-+').replace(".","").isdigit() or ord(item) == 43 or ord(item) == 42 or ord(item) == 45 or ord(item) == 47:  # If True, then item is valid, so exit loop
                valid_option_1 = True
            else:   # If False, item is invalid, so ask user to enter a valid item
                valid_option_1 = False
                print("Wrong number or operator! Please re-enter item!")

    # Append item to stack
    stack.append(item)

    # Checks for user choice
    valid_option_2 = False

    while not valid_option_2:
        choice = input("Do you want to append anything else to stack?(Y/N)\n")

        # Check if user enters something before pressing Enter
        if len(choice) > 0:
            if choice[0].capitalize() == 'Y':   # valid option, proceeds with entering next item
                valid_option_2 = True
                finished_input = False
            elif choice[0].capitalize() == 'N': # valid option, exits entire iteration
                valid_option_2 = True
                finished_input = True
            else:   # invalid option, asks user to enter a valid option
                valid_option_2 = False
                print("Please enter Y or N (Yes or No)!")
        else:
            valid_option_2 = False
            print("Please enter a value!")

# Stack pointer
i = 0

# Used to track how many operations have been done until the end
counter = 0

while i in range(len(stack)):
    # Print contents of stack
    print("Operation "+str(counter)+":")
    print(stack)
    print('\n')

    counter += 1

    # Check if current item is a number and contains a decimal point (hence a float)
    if stack[i].lstrip('-+').replace(".","").isdigit():  # if number, convert it accordingly
        index = stack[i].find(".")
        if index == -1: # if integer, convert current item into int
            stack[i] = int(stack[i])
        else:   # if float, convert current item into float
            stack[i] = float(stack[i])
        i += 1
    else:   # if it is an operator, then perform operation
        if ord(stack[i]) == 43:     # addition
            num1 = stack[i-2]
            num2 = stack[i-1]
            j = i-1
            stack.pop(j)
            j -= 1
            stack.pop(j)
            stack[j] = num1+num2
            i -= 1
        elif ord(stack[i]) == 42:   # multiplication
            num1 = stack[i-2]
            num2 = stack[i-1]
            j = i-1
            stack.pop(j)
            j -= 1
            stack.pop(j)
            stack[j] = num1*num2
            i -= 1
        elif ord(stack[i]) == 47:   # division
            num1 = stack[i-2]
            num2 = stack[i-1]
            j = i-1
            stack.pop(j)
            j -= 1
            stack.pop(j)
            stack[j] = num1/num2
            i -= 1
        elif ord(stack[i]) == 45:   # subtraction
            num1 = stack[i-2]
            num2 = stack[i-1]
            j = i-1
            stack.pop(j)
            j -= 1
            stack.pop(j)
            stack[j] = num1-num2
            i -= 1
    
    # Prints out final stack before displaying result in the next line
    if len(stack) == 1:
        print("Final Stack:")
        print(stack)
        print('\n')

# Check whether size of stack at the end of execution is larger than 1
if len(stack) > 1:  # if True, then expression not fully solved - prints out error
    print("Error! Expression not completely solved!")
else:   # if False, then print the result
    print("Final Result:",stack[0])
