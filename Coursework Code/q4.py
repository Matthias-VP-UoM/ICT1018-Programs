# Declare a list which takes in values inputted by the user
numbers_list = []

# Check whether input is integer (a whole number)
has_stopped = False

while not has_stopped:
    num_input = input("Enter number to add to list: ")
    
    if num_input.lstrip('+-').isnumeric():   # If input in string is a numerical value, then exit loop
        num_input = int(num_input)

        # Check that number does not exist in numbers_list
        if num_input in numbers_list:
            valid_input = False
            print("Element already exists in list! Please try again!")
        else:
            # Check that number entered by user is between 1 and 1024
            if num_input < 1 or num_input > 1024:
                valid_input = False
                print("Number is not between 1 and 1024! Please try again!")
            else:
                valid_input = True
                numbers_list.append(num_input)

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

    else:   # If not, ask the user to try again
        valid_input = False
        print("Input has to be a number! Please try again!")

# Print out generated list to user
print("\nList of numbers:")
print(numbers_list)

# Declare a list which stores any distinct pairs of integers found
pairs_list = []

# Check for distinct pairs of integers
for a in range(len(numbers_list)):
    for b in range(a,len(numbers_list)):
        for c in range(a+1,len(numbers_list)):
            for d in range(c,len(numbers_list)):
                # If conditions below are True, then add number to their own distinct pair and add them to pairs_list
                if (numbers_list[a]*numbers_list[b] == numbers_list[c]*numbers_list[d] and numbers_list[a]!=numbers_list[b] and numbers_list[a]!=numbers_list[c] and numbers_list[a]!=numbers_list[d] and numbers_list[b]!=numbers_list[c] and numbers_list[b]!=numbers_list[d] and numbers_list[c]!=numbers_list[d]):
                    pair_1 = (numbers_list[a],numbers_list[b])
                    pair_2 = (numbers_list[c],numbers_list[d])
                    pair_val = [pair_1,pair_2]
                    pairs_list.append(pair_val)

print('\n')

# After exitting loop, program checks if there were any distinct pairs of integers
if not pairs_list:  # If pairs_list is empty, then there were no distinct pairs of integers
    print("No distinct pairs of integers!")
else:   # Otherwise, there were distinct pairs of integers
    # Print out distinct pairs
    print('Distinct pairs of integers:')
    for i in pairs_list:
        print(i)
    
    print("\nNo more distinct factors!\nThank you for using this program!")
