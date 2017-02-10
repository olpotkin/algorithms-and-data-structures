
array = [-4, 56, 1, 3, 5, 63, 12, 4, -11, 234]

for i in range(len(array)-1):
    for j in range(1, len(array)-i):
        if array[j-1] > array[j]:
            temp = array[j-1]
            array[j-1] = array[j]
            array[j] = temp

print array
