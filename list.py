list = [1, 2, 3, 4, 5]
print("The value of list is = ", list)

empty_list = []
empty_list.append(3)
empty_list.append(5)
empty_list.append(7)
print("The modify list is = ", empty_list)
empty_list.remove(5)
print("The list after remove ", empty_list)
sliced_list = list[0:5]
print(sliced_list)


# concatenated

conc_list = list + [8, 9, 10]
print(conc_list)


for item in conc_list:
    print("The value of list = ", item)


list[2] = 10

print("The modify list is = ", list)
