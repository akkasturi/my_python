# find 2 numbers from given array, whose sum is equal to given target
# return the indecies both the number. Assume, there is always a such 
# valid pair in the array.

#arr = [1,3,4,5,6,8,3]
arr = [-1,13,14,5,6,10]
indexDict = {}
target = 9
resultList = []

for index, element in enumerate(arr):
  remainder = target - element
  foundElementIndex = indexDict.get(remainder)

  if(foundElementIndex != None):
    print(f"Target {target}:: num1:{element},index:{index} + num2:{remainder},index:{foundElementIndex}")
    resultList.append(index)
    resultList.append(foundElementIndex)
    break
  else:
    indexDict[element] = index

print(resultList)
