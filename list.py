l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l)
print(l[0])
print(l[1])
print(l[2])

l1 =l[0:3]
l2 = l[1:3]
l3 = l[2:3]

print(l1)
print(l2)
print(l3)

list2 =['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(list2[0:])

print ([1,2]+[3,4])

l5 = [1,2,4,8,10]
for val in l5:
    print(val)

def remove_even(lst):
    odds = []  # Create a new empty list
    for number in lst:  # Iterate over input list
        # Check if the item in the list is NOT even
        # ('%' is the modulus symbol!)
        if number % 2 != 0:
            odds.append(number)  # If it isn't even append it to the empty list
    return odds  # Return the new list


print(remove_even([3, 2, 41, 3, 34]))