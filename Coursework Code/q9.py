# An array containing list of integers
integers_list = []

# Add user input to list until user chooses to quit
finished_input = False

while not finished_input:
    # Ask the user to enter an item to append to list
    item = input("Enter an item to add to list: ")

    # Check if item to be added is a digit (integer)
    if item.isdigit():  # if True, then append item to list
        item = int(item)
        integers_list.append(item)

        # Check whether user enters a valid option when deciding to continue
        valid_option = False

        while not valid_option:
            # Asks user if he/she wants to continue adding numbers to list
            option = input("Do you want to add more to list? (1 for Yes or 2 for No)\n")

            # Check if option entered by user is a number
            if option.isdigit():    # If True, then proceed with checking of value
                option = int(option)
                if option == 1: # if Yes, then exit current while loop but not whole iteration
                    valid_option = True
                    finished_input = False
                elif option == 2:   # if No, then exit from all while loops
                    valid_option = True
                    finished_input = True
                else:   # Otherwise, invalid option - stay on current loop until user inputs correct option
                    valid_option = False
                    print("Invalid option!")
            else:   # If False, then print error to user
                valid_option = False
                print('Please enter a number, not a string!')
    else:   # if False, print error to user
        print("Please enter a whole number!")

# An empty array used to add any integers that are repeated more than once
repeated_integers_list = []

# Nested for loop which compares the current element with the other elements in the list
# and add element to repeated_integers_list if it exists more than once
for index1 in range(len(integers_list)):
    for index2 in range(index1+1, len(integers_list)):
        # Set currentElement to be the element currently being processed by the loop
        currentElement = integers_list[index1]

        # Checks if the current element exists later on in the list and
        # if it does not already exist in repeated_integers_list
        if currentElement == integers_list[index2] and currentElement not in repeated_integers_list:
            # Add element to list
            repeated_integers_list.append(currentElement)

# Checks if there are any elements in repeated_integer_list after loop execution
# and prints out necessary information to the user
if not repeated_integers_list:
    print("No integers being repeated more than once!")
else:
    print(repeated_integers_list)
