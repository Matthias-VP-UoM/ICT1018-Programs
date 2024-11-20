def extreme_points():
    # An array containing list of numbers
    array = []

    # An empty array which is used to add any extreme points
    extremePointsArray = []

    # Enter numbers until user decides to stop
    has_stopped = False

    while not has_stopped:
        # Ask user to input an integer
        num = input("Enter an integer: ")

        # Check if user input is an integer
        if num.lstrip('-+').isnumeric():    # If True, add number to list
            array.append(int(num))

            # Check for valid option
            valid_choice = False
            
            while not valid_choice:
                # Ask user to decide whether to continue
                choice = input("Do you want to continue adding more numbers (Y/N)?\n")

                # Check if user entered a value before pressing Enter
                if len(choice) > 0:
                    if choice[0].capitalize() == 'Y':   # valid option, proceeds with entering next number
                        has_stopped = False
                        valid_choice = True
                    elif choice[0].capitalize() == 'N': # valid option, exits entire iteration
                        has_stopped = True
                        valid_choice = True
                    else:   # invalid option, asks user to enter a valid option
                        valid_choice = False
                        print("Please enter Y or N (Yes or No)!")
                else:
                    valid_choice = False
                    print("Please enter a value!")
        else:   # Number not an integer!
            print('Invalid input! Please enter an integer!')

    # Setting variable length to the number of elements in the variable array
    length = len(array)

    # Go through each element by index and check whether it is an extreme point
    for index in range(length):
        # Check whether the current element is not the first or the last element in the list
        if not (index == 0 or index == (length-1)):
            currentElement = array[index]

            # Check whether the current element is an extreme point with the conditions set below
            # If True, then add the element to the extremePointsArray list
            if (array[index-1] > array[index] and array[index] < array[index+1]) or (array[index-1] < array[index] and array[index] > array[index+1]):
                extremePointsArray.append(currentElement)
    
    # Detects if there are any values in extremePointsArray after iteration of original list
    if not extremePointsArray:  # If empty, output to the user that original list was sorted
        print("SORTED")
    else:   # If not empty, print out all the elements from within the extremePointsArray variable
        print(extremePointsArray)


# Call extreme_points() function to start execution
extreme_points()
