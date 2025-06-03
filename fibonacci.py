# Program to display the Fibonacci sequence up to n terms

n_terms = int(input("How many terms? "))

# First two terms
a, b = 0, 1
count = 0

if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci sequence:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(a)
        a, b = b, a + b
        count += 1
