# finder1 does not work for duplicate numbers

def finder1(arr1,arr2):
    arr1.sort()
    arr2.sort()

    # zip itereates over two lists in parallel:
    for x, y in zip(arr1,arr2):
        if x != y:
            return x


import collections

# finder2 does work with duplicate numbers.
def finder2(arr1, arr2):

    # Using default dict to avoid key errors
    d=collections.defaultdict(int)

    # Add a count for every instance in Array 1
    for num in arr2:
        d[num]+=1

    # Check if num not in dictionary
    for num in arr1:
        if d[num]==0:
            return num

        # Otherwise, subtract a count
        else: d[num]-=1
