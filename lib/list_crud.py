# Create an empty list and return it
def create_an_empty_list():
    return []

# Create a list with four elements and return it
def create_a_list():
    return [1, 2, 3, 4]

# Add an element to the end of the list and return the modified list
def add_element_to_end_of_list(lst, element):
    lst.append(element)
    return lst

# Add an element to the start of the list and return the modified list
def add_element_to_start_of_list(lst, element):
    lst.insert(0, element)
    return lst

# Remove the last element from the list and return the modified list
def remove_element_from_end_of_list(lst):
    lst.pop()
    return lst

# Remove the first element from the list and return the modified list
def remove_element_from_start_of_list(lst):
    del lst[0]
    return lst

# Retrieve the first element from the list
def retrieve_first_element_from_list(lst):
    return lst[0]

# Retrieve an element from the list at the specified index
def retrieve_element_from_index(lst, index):
    return lst[index]

# Retrieve the last element from the list
def retrieve_last_element_from_list(lst):
    return lst[-1]
