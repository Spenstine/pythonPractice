'''
this is an inefficient way to implement quicksort
because it has O(n^2)

there is a better way to improve the efficiency
by making worste case O(nlog(n))
'''

def quicksort(array):
    less = []
    greater = []
    if len(array) < 2:
        return array
    pivot = array.pop() #choosing and removing pivot from array can be done better
    for item in array:
        if item < pivot + 1:
            less.append(item)
        else:
            greater.append(item)
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([4, 2,45,5,2, 4, 4, 1, 6, 10]))