def insertion_sort(arr):
  for i in range(1, len(arr)):
    temp = arr[i]
    position = i - 1

    while position >= 0:
      if arr[position] > temp:
        arr[position + 1] = arr[position]
        position = position - 1
      else:
        break
    arr[position + 1] = temp
  return arr

# result = insertion_sort([5, 1, 2, 3, 10, 1])
# print(result)
