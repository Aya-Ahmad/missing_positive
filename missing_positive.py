""" This function finds the smallest positive integer that is missing from a given list."""
def FirstMissingPositive( numbers ):
#first step, we need to sort the list in ascending order
    for i in range ( len (numbers) ):
        for j in range ( i+1 , len(numbers) ):
            if numbers [ i ] > numbers [ j ]:
                numbers[ i ] = numbers[ j ]
                numbers [ j ] = numbers[ i ]
#assigning the value 1 for the first positive missing number
    missing_number = 1
#this loop iterates over the indices of the list, checking if numbers[i] is equal to the missing number
#if yes, it increments the missing number by 1  
    for i in range ( len (numbers) ):
        if numbers [ i ] == missing_number:
            missing_number += 1
    return missing_number
nums = [-1,1,2]
print ( FirstMissingPositive ( nums ) )
