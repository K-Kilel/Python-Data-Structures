# Creating an empty list
my_list = []

# Appending elements
# new_list = [10,20,30,40]
# my_list.append(new_list)
my_list += [10,20,30,40]
print(my_list)

# Inserting value
my_list.insert(1,15)
print(my_list)

# Extend list
another_list = [50,60,70]
my_list.extend(another_list)
print(my_list)

# Remove last element
del my_list[-1]
print(my_list)

# Sorting list
sorted_list = sorted(my_list)
print(sorted_list)

# Printing index of value
index = sorted_list.index(30)
print(index)