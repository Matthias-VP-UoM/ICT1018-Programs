# Import q1 program to use data for q2 - runs q1 program at start of execution
import q1 as question1Program

def main():
    # Retrieve data from arrays A and B after q1 program finishes running
    arrayA = question1Program.array_A
    arrayB = question1Program.array_B

    # Perform merge sort on both arrays
    mergeSort(arrayA, arrayB)

    
# Function which takes two arrays, merges them into one signle array and sorts it
def mergeSort(arrayA, arrayB):

    # Array used to store all the elements of arrays A and B in a sorted manner
    arrayC = []

    # Declare two variables used as the index points for arrays A and B respectively
    i = j = 0

    # Declare two variables for the size of the two individual arrays
    sizeA = len(arrayA)
    sizeB = len(arrayB)

    # Compare the two elements pointed by the indexes i and j (for array A and array B respectively)
    # Add the smallest element of the two into the new array C
    while (i < sizeA) and (j < sizeB):
        if arrayA[i] <= arrayB[j]:
            arrayC.append(arrayA[i])
            i += 1
        else:
            arrayC.append(arrayB[j])
            j += 1
        
    
    # Checking if any element was left after exitting first while loop
    while i < sizeA:
        arrayC.append(arrayA[i])
        i += 1

    while j < sizeB:
        arrayC.append(arrayB[j])
        j += 1

    # Print out contents of array C after sorting
    print("\nArray C:", arrayC)


# Call main() function to start execution
main()