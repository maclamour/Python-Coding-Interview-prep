# Solution #1: Using a nested loop 

"""
This solution iterates over the list and calculates the product of all the numbers to the right of the current element as on lines 7 and 8. Then it calculates the product of all the elements to the left of the current element line 10. It then multiplies the two products and returns the result line 14.

Time Complexity
This algorithm is in O(n^2)
O(n 
2
 )
 because the list is iterated over n(n-1)/2
n(n−1)/2
 times.

"""

def find_product(lst):
    result = []
    left = 1  # To store product of all previous values from currentIndex
    for i in range(len(lst)):
        currentproduct = 1  # To store current product for index i
        # compute product of values to the right of i index of list
        for ele in lst[i+1:]:
            currentproduct = currentproduct * ele
        # currentproduct * product of all values to the left of i index
        result.append(currentproduct * left)
        # Updating `left`
        left = left * lst[i]

    return result


print(find_product([1, 2, 3, 4]))


# Solution #2: Optimizing the number of multiplications

"""
The algorithm for this solution is to first create a new list with products of all elements to the left of each element as done on lines 4-6. Then multiply each element in that list to the product of all the elements to the right of the list by traversing it in reverse as done on lines 9-11

Time Complexity
Since this algorithm only traverses over the list twice, it’s in linear time, O(n)
O(n)
.
"""

def find_product(lst):
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product


print(find_product([0, 1, 2, 3]))

