def min_search(arr): 
  minimum = arr[0]
  minimum_index = 0
  for i in range(1, len(arr)): 
    if arr[i] < minimum:
      minimum = arr[i]
      minimum_index = i
  return minimum_index

def selectionSort(arr): 
  newArray = []
  for i in range(len(arr)):
    minimum = min_search(arr)
    newArray.append(arr.pop(minimum))
  return newArray

print(selectionSort([5, 3, 6, 2, 10]))