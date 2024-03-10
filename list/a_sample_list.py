list = [2, 2, 2]
other_list = [3, 4, 5]

list.append(0)
list.append(1)
list.append(2)

# print(list)
# print(other_list)

# list.pop()
# print(list)

# list.extend(other_list)
# print(list)

# list.insert(6, "hello")

# print(list)

# other_list.remove(5)
# print(other_list)

# other_list.pop(1)
# other_list.clear()
# print(other_list)


# list.reverse()
# print(list)


# list.index(1)
# print(list)

# list[::3]

# print(list[::-2])
print(list)

x = list.count(2)
print(x)

copy_list = list.copy()
print(copy_list)
print(id(list))
print(id(copy_list))

list.append(34)
print(list)

list.sort()
print(list)
