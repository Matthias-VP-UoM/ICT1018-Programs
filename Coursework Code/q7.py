# Importation of csv package - used to enter results in a csv file
import csv

def main():
    # Write headers to csv file
    write_header_to_table()

    # Array used to store all generated number from the Collatz sequence
    num_list = [num for num in range(2,513)]

    # Perform Collatz sequence on all numbers in the array
    collatzSequence(num_list)


def collatzSequence(list):
    count = 0
    count_list = []

    # Write original data to csv file
    write_data_to_table(list,0)

    # Keep doing the Collatz sequence until n becomes 1
    size = len(list)

    # Variable used to check if all elements in the array are 1 during calculation
    all_are_1 = False

    while not all_are_1:
        # Check that every element in the array is equal to 1
        for element in list:
            if (element == 1) or (element == ""):   # if True, keep checking every element
                all_are_1 = True
            else:   # if False, exit for loop and perform Collatz sequence on the array
                all_are_1 = False
                count += 1
                count_list.append(count)
                break
        
        if all_are_1:
            break
        else:
            for i in range(size):
                # Set variable currentElement to be equal to the value of the array pointed to by index i
                currentElement = list[i]
                if list[i] == 1 or list[i] == "":   # if currentElement is already equal to 1, then set value as empty since there is no need to print it again
                    list[i] = ""
                else:   # otherwise, perform Collatz on the current element
                    if currentElement%2==0:  # If n is even, divide by 2
                        currentElement //= 2
                    else:   # If n is odd, perform 3n+1
                        currentElement = (3*currentElement)+1
                    
                    # Assign the value of list[i] to currentElement
                    list[i] = currentElement
            
            # Once all elements have been dealt with, write the contents of the list to csv file
            write_data_to_table(list,count)

    print(count_list)

    # Print out contents of array - testing
    print(list)


# Function which writes table headers to csv file
def write_header_to_table():
    header = ['Count']

    # Append another header stating which number is being dealt with in which column
    for i in range(2,513):
        header.append('N = '+str(i))

    # Write contents of header list to csv file
    with open('data/collatz.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)


def write_data_to_table(list_num,count):
    # Array used to store data of list_num and count
    data = []

    # Declare variable called size and assign its value to the length of list_num
    size = len(list_num)

    # Add count and every element in the list to the data array
    data.append(count)
    for index in range(size):
        data.append(list_num[index])

    # Write contents of data array to csv file
    with open('data/collatz.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the data
        writer.writerow(data)


# Call main() function to start execution
main()