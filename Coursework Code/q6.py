# Import math package - used to calculate square root of num (line 50)
import math

def main():
    # Check if user input is a numerical value
    is_num = False

    while not is_num:
        # Ask user to input number to act as end of range of numbers to check which numbers are prime
        num = input("Input a max number: ")

        # Check if user input is an integer
        if not num.lstrip('+-').isdigit():   # If False, then prompt user to enter a number
            is_num = False
            print("Please enter a number, preferably an integer!")
        else:   # If True, then exit while loop
            num = int(num)
            if num <= 0:
                is_num = False
                print("Any number less than or equal to 0 is never a prime number! Please enter a positive number!")
            else:
                is_num = True
    
    print('\n')

    # List which is used to store every possible prime number
    numbers_list = []

    # Add every number from 2 to that entered by the user (1 is not prime)
    for i in range(2, num+1):
        numbers_list.append(i)
    
    numbers_list = checkPrimeNumbers(numbers_list, num)

    if num in numbers_list:
        print(str(num) + " is a prime number!\n")
    else:
        print(str(num) + " is not a prime number!\n")

    # Print out list which contains prime numbers
    print("List of prime numbers up to "+str(num)+":")
    print(numbers_list)


# Function which checks which numbers in list are prime numbers and returns list of prime numbers
# Implements the Sieve of Eratosthenes algorithm
def checkPrimeNumbers(list, num):
    i = 2

    while not i > int(math.sqrt(num)):

        for j in range(2, num):
            element_to_remove = i*j
            if element_to_remove in list:
                list.remove(element_to_remove)
                #print(element_to_remove) - TESTING
    
        i += 1

        while i not in list:
            i += 1
        
    
    return list


# Call main() function to start execution
main()