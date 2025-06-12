# Python Flow Control 

# 1. Conditional Statements
print("1. Conditional Statements:")
age=int(input("Enter the age"))
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult.")
else:
    print("You are an adult.")
    
print("\n")

# 2. For Loop
print("2. For Loop:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

print("\n")

# 3. While Loop
print("3. While Loop:")
count = 0
while count < 3:
    print(f"Count is: {count}")
    count += 1

print("\n")

# 4. Break Statement
print("4. Break Statement:")
for number in range(5):
    if number == 3:
        print("Breaking at 3")
        break
    print(f"Number: {number}")

print("\n")

# 5. Continue Statement
print("5. Continue Statement:")
for number in range(5):
    if number == 2:
        print("Skipping 2")
        continue
    print(f"Number: {number}")

