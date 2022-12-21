def remove_even(lst):
    odds = []  # Create a new empty list
    for number in lst:  # Iterate over input list
        # Check if the item in the list is NOT even
        # ('%' is the modulus symbol!)
        if number % 2 != 0:
            odds.append(number)  # If it isn't even append it to the empty list
    return odds  # Return the new list


print(remove_even([3, 2, 41, 3, 34]))

# or 

def remove_even(lst):
    # List comprehension to iter aover List and add to new list if not even
    return [number for number in lst if number % 2 != 0]


print(remove_even([3, 2, 41, 3, 34,57,83]))