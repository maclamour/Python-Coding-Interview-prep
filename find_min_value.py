#Solution #1: Sort the list#

def find_minimum(lst):
    if (len(lst) <= 0):
        return None
    lst.sort()  # sort list
    return lst[0]  # return first element


print(find_minimum([9, 2, 3, 6]))


"""

Time Complexity
The build-in sort function sort and the mergeSort are in O(nlogn)
O(nlogn)
. Since we only index and return after that, which are constant time operations, this solution takes O(nlogn)
O(nlogn)
 time.

"""

def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              my_list[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                my_list[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            my_list[k]=right[j]
            j += 1
            k += 1


def find_minimum(lst):
    if (len(lst) <= 0):
        return None
    merge_sort(lst)  # sort list
    return lst[0]  # return first element


print(find_minimum([9, 2, 3, 6]))

#Solution #2: Iterate over the list#

"""
Start with the first element which is 9 in this example and save it as the smallest value. Then, iterate over the rest of the list and whenever an element that is smaller than the number already stored as minimum is come across, set minimum to that number. By the end of the list, the number stored in minimum will be the smallest integer in the whole list.

Time Complexity
Since the entire list is iterated over once, this algorithm is in linear time, O(n)
O(n)
.

"""

def find_minimum(lst):
    if (len(lst) <= 0):
        return None
    minimum = lst[0]
    for ele in lst:
        # update if found a smaller element
        if ele < minimum:
            minimum = ele
    return minimum


print(find_minimum([9, 2, 3, 6]))