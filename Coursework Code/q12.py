def main():
    answer = 0

    # Check whether input entered by user is valid
    valid_input = False
    while not valid_input:
        # Asking user to input number of terms to be calculated and added together in fibonacci
        n = input("Enter how many terms you want to add in fibonacci sequence: ")

        # Check if user has entered value for n and that value is an integer
        if len(n) > 0 and n.lstrip('+-').isdigit():
            n = int(n)
            # Check if n is less than or equal to 0
            if n <= 0:  # If True, tell user to input another number
                valid_input = False
                print("Number must be at least 1 or greater than 1!")
            elif n > 20575:
                valid_input = False
                print("Numerical overflow might be possible! Please enter a smaller number!")
            else:   # If False, proceed with calculating answer
                valid_input = True
                answer = sum_fibonacci(n)
        else:
            valid_input = False
            print("Please enter an integer!")
    
    # Printing the answer after function execution
    print("Sum of first", n, "terms of fibonacci sequence =", answer)


# Function which returns the sum of the first n fibonacci terms as stated by the user input
def sum_fibonacci(counter):
    # Check if counter is greater than 1
    if counter == 1:    # If yes, there is only one number, so return 1
        return 1
    else: # Otherwise, perform Fibonacci sequence
        # Set term1 and term2 to be 1
        term1 = term2 = 1

        # Set sum to be equal to the sum of term1 and term2 before start of loop
        sum = term1+term2

        # Calculate nextTerm and add it to sum variable until first n terms are found
        for i in range(2, counter):
            nextTerm = term1 + term2
            term1 = term2
            term2 = nextTerm
            sum += nextTerm
            #print(nextTerm)  -  TESTING PURPOSES
        
        return sum


# Call main() function to start execution
main()
