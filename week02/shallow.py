import copy

# original = [1, 2, [3, 4]]

# shallow = copy.copy(original)

# shallow.append(5)

# print("Original:", original)
# print("Shallow :", shallow)
# append on the outer list does not affect but append o nthe inner list affects th original
# collection data types outer is not affected but inner are affected in the original

# original = "hello"
# shallow = copy.copy(original)

# shallow = shallow + " world"

# print(original)
# print(shallow)



lst = [[1, 2], [3, 4]]

a = copy.copy(lst)

a[0].append(100)

print(lst)
print(a)