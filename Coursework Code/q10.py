# Import sys package - used when calling findLargestNum() from main method (to retrieve smallest integer number available)
# This helps deal with negative numbers
import sys

def main():
    # An array containing a list of numbers
    numbers_list = []

    has_stopped = False

    while not has_stopped:
        # Ask user to input an integer
        num = input("Enter an integer: ")

        # Check if user input is an integer
        if num.lstrip('-+').isnumeric():    # If True, add number to list
            numbers_list.append(int(num))

            # Check for valid option
            valid_choice = False
            
            while not valid_choice:
                # Ask user to decide whether to continue
                choice = input("Do you want to continue adding more numbers (Y/N)?\n")

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

    # Find largest number and store in variable called largestNum
    largestNum = findLargestNum(numbers_list, -sys.maxsize-1)

    # Printing the answer after function execution
    print("Largest Number =", largestNum)


# Function which finds the largest number from the given list in a recursive manner
def findLargestNum(array, ans):
    # Checks if list is empty
    if not array:   # if True, return ans
        return ans
    else:   # if False, check if current element is larger than the number set in ans
        if array[0] > ans:
            ans = array[0]
        
        # Remove first element from list (with index 0)
        array.pop(0)
        
        # Call findLargestNum() function - recursion
        return findLargestNum(array, ans)



# Call main() function to start execution
main()
