arr = [5, 1, 4, 6, 7, 3, 5, 7, 3]
duplicates = []

for i in range(len(arr)):
  current = arr[i]
  if current in arr[i + 1:]:
    if current not in duplicates:
      duplicates.append(current)
print(duplicates)