# Importing math package - used to calculate xRadians and for Maclaurin's series
import math


def main():
    xRadians = 0
    n = 0

    # Repeat until user chooses to exit the program
    option = 0
    while(option != 3):
        # Boolean variable to check for numerical overflow
        valid = False

        # Print menu to user and ask user to enter an option
        option = input("1. Compute sine\n2. Compute cosine\n3. Exit\nChoose an option: ")
        print("\n")

        # Check if option is an integer
        if option.isdigit():
            option = int(option)
            # If user does not exit, ask the user to enter angle and number of iterations
            if (option == 1) or (option == 2):
                # Check if number of iterations entered by user is valid
                while not valid:
                    x = input("Enter number for x (in degrees): ")

                    # Check if x is an integer
                    if x.lstrip('+-').replace(".","").isdigit():
                        index = x.find(".")
                        if index == -1: # if integer, convert current item into int
                            x = int(x)
                        else:   # if float, convert current item into float
                            x = float(x)

                        # Converting user input to radians since Maclaurin's expansion works with radians
                        xRadians = (x*math.pi)/180

                        # Ask user to input number of iterations
                        n = input("Enter number for n: ")

                        # Check if n is an integer
                        if n.lstrip('+-').isdigit():
                            n = int(n)
                            if option == 1:     # sin
                                if n >= 86: # numerical overflow
                                    print("Error! Entering such a high number can induce errors in calculation!\n")
                                    print("Please enter a value less than 86!")
                                elif n <= 0:    # negative number or 0
                                    print("Error! Cannot perform calculation for negative number of iterations!\n")
                                    print("Please enter a value greater than 0!")
                                else:   # valid
                                    valid = True
                            elif option == 2:   # cos
                                if n >= 87: # numerical overflow
                                    print("Error! Entering such a high number can induce errors in calculation!\n")
                                    print("Please enter a value less than 87!")
                                elif n <= 0:    # negative number or 0
                                    print("Error! Cannot perform calculation for negative number of iterations!\n")
                                    print("Please enter a value greater than 0!")
                                else:   # valid
                                    valid = True
                        else:
                            print("Please enter a number!")
                    else:
                        print("Please enter a number!")

                print("\n")

                # Call computeMaclaurins() function to compute sin() or cos()
                computeMacluarins(n, xRadians, option, x)

                print("\n")

            elif option == 3:   # Exit program
                print("Thanks for using this program!")
            else:   # Invalid option
                print("Invalid option!\n")
        else:
            print("Please enter a number!\n")


# Function which computes cosine or sine using Maclaurin's series expansion
def computeMacluarins(n, xRad, option, xDeg):
        ans = 0

        # Perform operation based on user's choice of option
        if option == 1:     # Calculate approximation of sin(x) using Maclaurin's series
            for r in range(0,n):
                ans += ((-1)**r)*((xRad**((2*r)+1))/math.factorial(((2*r)+1)))
            print("sin("+str(xDeg)+") = ",round(ans,2))
        elif option == 2:   # Calculate approximation of cos(x) using Maclaurin's series
            for r in range(0,n):
                ans += ((-1)**r)*((xRad**(2*r))/math.factorial(2*r))
            print("cos("+str(xDeg)+") = ",round(ans,2))
    

# Call main() function to start execution
main()
