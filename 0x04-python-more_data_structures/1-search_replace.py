#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the results
    new_list = []
    
    # Iterate through each element in the original list
    for item in my_list:
        # If the item matches the search element, append the replace element
        # Otherwise, append the original item
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    
    # Return the new list
    return new_list
