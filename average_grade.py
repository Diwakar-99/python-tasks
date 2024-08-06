# Define a dictionary to store student data
students = {
    "001": {"name": "Alice", "grades": [85, 90, 78]},
    "002": {"name": "Bob", "grades": [92, 88, 84]},
    "003": {"name": "Charlie", "grades": [70, 75, 80]}
}

# Add a new grade for a student
student_id_to_add_grade = "001"
new_grade = 95  # Adding a new grade for Alice

if student_id_to_add_grade in students:
    students[student_id_to_add_grade]["grades"].append(new_grade)
else:
    print(f"Student ID {student_id_to_add_grade} not found.")

# Calculate average grades for each student
average_grades = {}
for student_id, data in students.items():
    avg = sum(data["grades"]) / len(data["grades"])
    average_grades[student_id] = avg

# Find the student with the highest average grade
highest_student_id = max(average_grades, key=average_grades.get)
highest_student_name = students[highest_student_id]["name"]
highest_average = average_grades[highest_student_id]

# Print the average grades and the student with the highest average
print("Average Grades:")
for student_id, avg in average_grades.items():
    print(f"Student ID {student_id} ({students[student_id]['name']}): {avg:.2f}")

print(f"\nStudent with the highest average grade: {highest_student_name} (ID: {highest_student_id}) with an average of {highest_average:.2f}")
 
