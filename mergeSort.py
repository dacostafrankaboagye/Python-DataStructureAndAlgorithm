

def mergeSort(myArray):
  if len(myArray) > 1:
    midPoint = len(myArray) // 2
    leftArray = myArray[:midPoint]
    rightArray = myArray[midPoint:]
    mergeSort(leftArray)
    mergeSort(rightArray)
    leftIdx = 0
    rightIdx = 0
    arrayIdx = 0
    while(leftIdx<len(leftArray) and rightIdx<len(rightArray)):
      if(leftArray[leftIdx] < rightArray[rightIdx]):
        myArray[arrayIdx] = leftArray[leftIdx]
        leftIdx +=1
      else:
        myArray[arrayIdx] = rightArray[rightIdx]
        rightIdx +=1
      arrayIdx +=1
    while(leftIdx <len(leftArray)):
      myArray[arrayIdx] = leftArray[leftIdx]
      leftIdx +=1
      arrayIdx +=1
    while(rightIdx<len(rightArray)):
      myArray[arrayIdx] = rightArray[rightIdx]
      rightIdx +=1
      arrayIdx +=1


array = [16, 5, 12, 10, 9, 12,1, 3]
print(array)
mergeSort(array)
print(array)










  
  
