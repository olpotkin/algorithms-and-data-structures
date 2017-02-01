# One-dimensional array (actually, List)
numbers = [1, 2, 3, 4, 5]

# Random indexing --> O(1) - constant time complexity, get items if we know index !!!
print numbers[0]


print 'Update value with index 1:'
numbers[1] = 'Some name'
print numbers[1]


print 'Iterate all elements of array:'
for num in numbers:
    print num


print 'Iterate array using indexes:'
for i in range(len(numbers)):
    print numbers[i]


print 'Print range of numbers:'
print numbers[0:2]

print 'Print range of numbers except last 2:'
print numbers[:-2]


print 'Find the maximum:'
# O(N) search runtime  - linear time complexity
numbers[1] = 100
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print 'maximum = {0}'.format(maximum)

