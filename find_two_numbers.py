
# Solution #1: Brute Force - time complexity O(n2)
def find_sum(lst, k):
    # iterate lst with i
    for i in range(len(lst)):
        # iterate lst with j
        for j in range(len(lst)):
            # if sum of two iterators is k
            # and i is not equal to j
            # then we have our answer
            if(lst[i]+lst[j] is k and i is not j):
                return [lst[i], lst[j]]


print(find_sum([1, 2, 3, 4], 5))


# Solution #2: Sorting the List - time complexity O(log n)
def binary_search(a, item):
    first = 0
    last = len(a) - 1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last) // 2
        if a[mid] == item:
            index = mid
            found = True
        else:
            if item < a[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return index
    else:
        return -1

#Solution #3: Moving indices - 

"""
Time Complexity#
The linear scan takes O(n)
O(n)
 and sort takes O(n log n)
O(nlogn)
. The time complexity becomes O(n log n) + O(n)
O(nlogn)+O(n)
 because the sort and the linear scan are done one after the other. The overall would be O(n log n)
O(nlogn)
 in the worst case.
 
 """

def find_sum(lst, k):
    lst.sort()
    for j in range(len(lst)):
        # find the difference in list through binary search
        # return the only if we find an index
        index = binary_search(lst, k -lst[j])
        if index != 1 and index is not j:
            return [lst[j], k -lst[j]]
    


print(find_sum([1, 5, 3], 2))
print(find_sum([1, 2, 3, 4], 5))