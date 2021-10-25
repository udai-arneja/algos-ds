import math

# Binary Search in Python - version one recursion

# Input
input1 = []
target = 8

input2 = [1,2,3,5,7,9,10]
target2 = 8

input3 = [1,2,3,5,7,9,10]
target3 = 5

def binarySearchRecursion(startIndex, endIndex, numArray, number):

    if len(numArray) == 0:
        return -1
    if startIndex > endIndex:
        return -1

    middleIndex = int(math.floor((startIndex+endIndex)/2))

    if numArray[middleIndex] == number:
        return middleIndex
    elif numArray[middleIndex] > number:
        endIndex = middleIndex-1
        return binarySearchRecursion(startIndex, endIndex, numArray, number)
    else: 
        startIndex = middleIndex+1
        return binarySearchRecursion(startIndex, endIndex, numArray, number)


length = len(input1)
index = binarySearchRecursion(0, length-1, input1, target)
print(index)

length = len(input2)
index2 = binarySearchRecursion(0, length-1, input2, target2)
print(index2)

length = len(input3)
index3 = binarySearchRecursion(0, length-1, input3, target3)
print(index3)