class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list):
  # Sort the list of students based on CGPA in descending order
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Test the function with different input lists of students
students1 = [
  Student("Alice", "101", 3.9),
  Student("Bob", "102", 3.7),
  Student("Charlie", "103", 4.0),
]

students2 = [
  Student("David", "104", 3.5),
  Student("Eve", "105", 3.8),
  Student("Frank", "106", 3.6),
]

sorted_students1 = sort_students(students1)
sorted_students2 = sort_students(students2)

# Print the sorted student lists
print("Sorted Students 1 (CGPA descending order):")
for student in sorted_students1:
  print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

print("\nSorted Students 2 (CGPA descending order):")
for student in sorted_students2:
  print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
