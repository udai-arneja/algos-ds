import math

# Binary Search in Python - version two not using recursion

# Input
input1 = []
target = 8

input2 = [1,2,3,5,7,9,10]
target2 = 8

input3 = [1,2,3,5,7,9,10]
target3 = 5

def binarySearch(startIndex, endIndex, numArray, number):

    if len(numArray) == 0:
        return -1

    while endIndex >= startIndex:
        
        middleIndex = int(math.floor((startIndex+endIndex)/2))

        if numArray[middleIndex] == number:
            return middleIndex
        elif numArray[middleIndex] > number:
            endIndex = middleIndex-1
        else: 
            startIndex = middleIndex+1

    return -1


length = len(input1)
index = binarySearch(0, length-1, input1, target)
print(index)

length = len(input2)
index2 = binarySearch(0, length-1, input2, target2)
print(index2)

length = len(input3)
index3 = binarySearch(0, length-1, input3, target3)
print(index3)
