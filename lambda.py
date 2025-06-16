students = [("Alice", 88), ("Bob", 72), ("Charlie", 95), ("David", 85)]

sorted_students = sorted(students, key=lambda x: x[1])

print("Sorted by marks (ascending):")
for student in sorted_students:
    print(student)
