#Student Marks Manager: stores marks of 3 subjects per student (tuple, set, dict of lists),# with a menu to add, display, and average; uses recursion for total and handles# ValueError, ZeroDivisionError, TypeError, NameError.

 
# Student Marks Management System
 
SUBJECTS = ("Math", "Science", "English")   # tuple of subject names
student_names = set()                        # unique student names
student_marks = {}                           # {name: [marks]}
 
 
def recursive_total(marks, index=0):
    """Recursively calculate the total of a list of marks."""
    if not isinstance(marks, list):
        raise TypeError("Marks must be stored in a list.")
    if index == len(marks):
        return 0
    if not isinstance(marks[index], (int, float)):
        raise TypeError(f"Invalid data type in marks: {marks[index]!r}")
    return marks[index] + recursive_total(marks, index + 1)
 
 
def add_student():
    """Add a student with marks for each subject."""
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name in student_names:
        print("Student already exists. Names must be unique.")
        return
 
    marks = []
    for subject in SUBJECTS:
        value = float(input(f"Enter marks for {subject}: "))   # may raise ValueError
        if value.is_integer():
            value = int(value)                                  # show 80 instead of 80.0
        marks.append(value)
 
    student_names.add(name)
    student_marks[name] = marks
    print("Student added successfully.")
 
 
def display_students():
    """Display all student records."""
    if not student_marks:
        print("No student records found.")
        return
    for name, marks in student_marks.items():
        print(f"{name} : {marks}")
 
 
def calculate_average():
    """Calculate total and average marks of a student."""
    name = input("Enter student name to calculate average: ").strip()
 
    if name not in student_marks:
        raise NameError(f"Student '{name}' does not exist.")
 
    marks = student_marks[name]
    total = recursive_total(marks)          # may raise TypeError
    average = total / len(marks)            # may raise ZeroDivisionError
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average}")
 
 
def main():
    while True:
        print("\n1. Add Student")
        print("2. Display Students")
        print("3. Calculate Average")
        print("4. Exit")
        choice = input("Enter choice: ").strip()
 
        try:
            if choice == "1":
                add_student()
            elif choice == "2":
                display_students()
            elif choice == "3":
                calculate_average()
            elif choice == "4":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1-4.")
        except ValueError:
            print("Error: Marks must be numeric values.")
        except ZeroDivisionError:
            print("Error: Cannot calculate average (no marks available).")
        except TypeError as e:
            print(f"Error: Incorrect data type in marks. {e}")
        except NameError as e:
            print(f"Error: {e}")
 
 
if __name__ == "__main__":
    main()

