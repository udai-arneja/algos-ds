
def exchange(array, index1, index2):
    tmpEleValue = array[index1]
    array[index1] = array[index2]
    array[index2] = tmpEleValue

def quicksort(inputArray):
    if len(inputArray) <= 1:
        return inputArray

    pivotIndex = len(inputArray)-1
    largerArrayStart = 0

    for element in range(0,pivotIndex):
        if inputArray[element] < inputArray[pivotIndex]:
            exchange(inputArray, largerArrayStart, element)
            largerArrayStart += 1
    
    exchange(inputArray, largerArrayStart, pivotIndex)

    smaller = quicksort(inputArray[0:largerArrayStart])
    larger = quicksort(inputArray[largerArrayStart:len(inputArray)])

    outputArray = smaller + larger
    return outputArray

print(quicksort([1,2,3,4,5,7,8,9,5]))
print(quicksort([1,2,3,5,4,7,8,9]))
print(quicksort([1,4,9,5,7,8,2,3]))