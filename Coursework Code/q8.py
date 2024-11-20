def main():
    # Check that user input is an integer
    is_valid = False

    while not is_valid:
        # Asking user for the number to perform the square root on
        y = input("Enter a number you want to perform square root on: ")

        if y.isdigit() and len(y) > 0:
            y = int(y)
            if y > 0:
                is_valid = True
                y = int(y)
            else:
                is_valid = False
                print("Please enter a positive integer!")
        else:
            is_valid = False
            print("Please enter a number!")

    # Calling square_root_approximation() method and assigning final value in variable called ans
    ans = square_root_approximation(y)

    # Printing the answer after function execution
    print("Square root of", y, "=", ans)
    print("Therefore, answer ≈", round(ans, 2))


# Function which calculates approximation to the square root of the parameter num
# using the Newton-Raphson Method
def square_root_approximation(num):
    # Set x0 to num at start of execution
    x0 = num
    count = 0

    # Set nextX to 0 by default before start of while loop
    nextX = 0
    
    # Calculates 5 approximations of the square root of num
    while count < 10:
        # Checks if first approximation has already been found and sets
        # x0 to nextX if condition returns True
        if count >= 1:
            x0 = nextX
            
        nextX = x0 - (((x0*x0)-num)/(2*x0))
        count += 1
        
    return nextX


# Call main() function to start execution
main()
