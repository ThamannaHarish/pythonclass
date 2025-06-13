# 1. LIST (Ordered, Mutable, Allows Duplicates)
print("1. LIST:")
my_list = [1, 2, 3, 2, 4]
print("Original List:", my_list)

my_list.append(5)
print("After Append:", my_list)

my_list.remove(2)  # Removes first occurrence of 2
print("After Remove:", my_list)

my_list[1] = 10
print("After Updating Index 1:", my_list)

print("List Length:", len(my_list))
print("Check if 4 in List:", 4 in my_list)
print("-" * 40)

# 2. TUPLE (Ordered, Immutable, Allows Duplicates)
print("2. TUPLE:")
my_tuple = (10, 20, 30, 20)
print("Original Tuple:", my_tuple)

print("Access Index 1:", my_tuple[1])
print("Count of 20:", my_tuple.count(20))
print("Index of 30:", my_tuple.index(30))
print("Length:", len(my_tuple))
print("-" * 40)

# 3. DICTIONARY (Key-Value Pairs, Unordered, Mutable)
print("3. DICTIONARY:")
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Original Dictionary:", my_dict)

my_dict["age"] = 26  # Update value
print("After Updating Age:", my_dict)

my_dict["country"] = "USA"  # Add new key
print("After Adding Country:", my_dict)

print("Access Name:", my_dict["name"])
print("Keys:", list(my_dict.keys()))
print("Values:", list(my_dict.values()))
print("Items:", list(my_dict.items()))
print("-" * 40)

# 4. SET (Unordered, Mutable, No Duplicates)
print("4. SET:")
my_set = {1, 2, 3, 2, 4}
print("Original Set (duplicates removed):", my_set)

my_set.add(5)
print("After Add:", my_set)

my_set.remove(3)
print("After Remove:", my_set)

print("Check if 2 in Set:", 2 in my_set)
print("Set Length:", len(my_set))

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference (A - B):", set_a.difference(set_b))
print("-" * 40)
