# Import random package - used to populate arrays with random integers between 0 and 1024
import random

def main():
    # Declared as global variables in order to be used in q2 program
    global array_A, array_B

    # Declaration of arrays A and B
    array_A = []
    array_B = []

    # Check whether size of both arrays is valid
    isValid = False

    while not isValid:
        sizeA = input("Enter max length for array A: ")
        sizeB = input("Enter max length for array B: ")

        # Check that user enters integers and not anything else
        if (len(sizeA) > 0 and len(sizeB) > 0) and (sizeA.isdigit() and sizeB.isdigit()):
            sizeA = int(sizeA)
            sizeB = int(sizeB)

            # Check that size of both arrays satisfies the following conditions
            if (sizeA < 256) or (sizeB < 256):  # size of any one of arrays must not be less than 256
                isValid = False
                print("Minimum number of elements in each array must not be smaller than 256!\n")
            elif sizeA == sizeB:    # size of array A must not be equal to that of array B
                isValid = False
                print("Length of array A must not be equal to that of array B!\n")
            else: # size of arrays A and B satisfies the above conditions
                isValid = True
        else:
            isValid = False
            print("Please enter integers!\n")

    # Populate arrays with random integers between 0 and 1024
    for index1 in range(0, sizeA):
        number = random.randint(0, 1024)
        array_A.append(number)

    for index2 in range(0, sizeB):
        number = random.randint(0, 1024)
        array_B.append(number)

    # Perform shell sort on array A
    shellSort(array_A, len(array_A))

    # Perform quick sort on array B
    quickSort(array_B, 0, len(array_B)-1)

    # Print sorted arrays after finishing execution
    print("\nArray A sorted using Shell Sort:",array_A)
    print("\nArray B sorted using Quick Sort:",array_B)
    

# Function which takes an array as a parameter and performs shell sort on it
def shellSort(list, n):
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for index in range(interval, n):
            temp = list[index]
            j = index
            while j >= interval and list[j - interval] > temp:
                list[j] = list[j - interval]
                j -= interval

            list[j] = temp
        interval //= 2


# Function which takes an array as a parameter and performs quick sort on it
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # elements smaller than pivot are on the left
        # elements greater than pivot are on the right
        pivot = partition(array, low, high)
 
        # Recursive call on the left of pivot (elements smaller than pivot element)
        quickSort(array, low, pivot-1)
 
        # Recursive call on the right of pivot (elements larger than pivot element)
        quickSort(array, pivot+1, high)


# Function to find the partition position
def partition(array, low, high):
 
    # Choose the rightmost element as pivot element
    pivot = array[high]
 
    # Index pointer used for greater element
    index1 = low - 1
 
    # Traverse through all elements
    # compare each element with pivot
    for index2 in range(low, high):
        if array[index2] <= pivot:
 
            # If element that is smaller than pivot is found
            # Then swap it with the greater element pointed by i
            index1 += 1
 
            # Swapping element at index i with element at index j
            (array[index1], array[index2]) = (array[index2], array[index1])
 
    # Swap the pivot element with the greater element specified by index i
    (array[index1 + 1], array[high]) = (array[high], array[index1 + 1])
 
    # Return the position from where partition is done
    return index1 + 1


# Call main() function to start execution
main()