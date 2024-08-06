students = {}

while True:
    name = input("Enter student name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    score = float(input(f"Enter score for {name}: "))
    students[name] = score

if students:
    average_score = sum(students.values()) / len(students)
    print("\nStudent Scores:")
    for name, score in students.items():
        print(f"{name}: {score}")

    print(f"\nAverage score: {average_score:.2f}")
else:
    print("No students entered.")
