# Heapsort - development of the functions

def heapify(inputArray, index):
    currIndex = index
    heapsize = len(inputArray)

    while (2*currIndex)+1 < heapsize:
        # children indexes
        left = (2*currIndex)+1
        right = (2*currIndex)+2

        # comparisons to find largest out of current and children nodes
        largest = currIndex
        if inputArray[left] > inputArray[currIndex]:
            largest = left
        if right < heapsize:
            if inputArray[right] > inputArray[largest]:
                largest = right
        elif largest == currIndex: break            # input element is at the correct index (both children have a smaller value)

        # exchange
        tmpEleValue = inputArray[currIndex]
        inputArray[currIndex] = inputArray[largest]
        inputArray[largest] = tmpEleValue

        currIndex = largest
    
    return inputArray

def buildHeap(inputArray):

    halfOfArrayLength = int(len(inputArray)/2)    # start of the build heap

    for x in range(halfOfArrayLength, -1, -1):
        inputArray = heapify(inputArray,x)

    return inputArray

def heapsort(inputArray):
    buildHeap(inputArray)
    heapsize = len(inputArray)-1
    while heapsize > 0:
        # exchange
        tmpRoot = inputArray[0]
        inputArray[0] = inputArray[heapsize]
        inputArray[heapsize] = tmpRoot
        # maintaining max heap property with remaining heap
        inputArray[:heapsize] = heapify(inputArray[:heapsize], 0)
    
        heapsize -= 1
    return inputArray

def insertToHeap(inputArray, element):
    inputArray.append(element)
    misplacedIndex = len(inputArray)-1
    parent = int((misplacedIndex-1)/2)
    while inputArray[parent] < inputArray[misplacedIndex]:
        tmpEleValue = inputArray[parent]
        inputArray[parent] = inputArray[misplacedIndex]
        inputArray[misplacedIndex] = tmpEleValue

        misplacedIndex = parent
        parent = int((misplacedIndex-1)/2)
    return inputArray

heapArray = buildHeap([1,2,3,5,6,7,8,9,10,11,12,13,14,15])
insertedEle = insertToHeap(heapArray, 10)
# sortedArray = heapsort([1,2,3,5,6,7,8,9,10,11,12,13,14,15,5])
print(insertedEle)
# print(sortedArray)