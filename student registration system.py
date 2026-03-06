class Student:
    def __init__(self, student_id, name, age, grade, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.email = email

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Email: {self.email}"

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'age': self.age,
            'grade': self.grade,
            'email': self.email
        }

class StudentRegistrationSystem:
    def __init__(self):
        self.students = {}
        self.next_id = 1

    def add_student(self, name, age, grade, email):
        student_id = self.next_id
        student = Student(student_id, name, age, grade, email)
        self.students[student_id] = student
        self.next_id += 1
        print(f"Student {name} added successfully with ID: {student_id}")
        return student_id

    def remove_student(self, student_id):
        if student_id in self.students:
            removed_student = self.students.pop(student_id)
            print(f"Student {removed_student.name} (ID: {student_id}) removed successfully")
            return True
        else:
            print(f"Student with ID {student_id} not found")
            return False

    def list_students(self):
        if not self.students:
            print("No students registered")
            return

        print("\n--- Student List ---")
        for student in self.students.values():
            print(student)
        print("--------------------\n")

    def view_student_info(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print("\n--- Student Information ---")
            print(f"ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Grade: {student.grade}")
            print(f"Email: {student.email}")
            print("---------------------------\n")
        else:
            print(f"Student with ID {student_id} not found")

    def update_student_info(self, student_id):
        if student_id not in self.students:
            print(f"Student with ID {student_id} not found")
            return False

        student = self.students[student_id]
        print(f"\nUpdating information for {student.name} (ID: {student_id})")
        print("Leave blank to keep current value")

        # Get new values
        name = input(f"Name ({student.name}): ").strip() or student.name
        age_input = input(f"Age ({student.age}): ").strip()
        age = int(age_input) if age_input else student.age
        grade = input(f"Grade ({student.grade}): ").strip() or student.grade
        email = input(f"Email ({student.email}): ").strip() or student.email

        # Update student
        student.name = name
        student.age = age
        student.grade = grade
        student.email = email

        print("Student information updated successfully")
        return True

    def save_to_file(self, filename="students.txt"):
        try:
            with open(filename, 'w') as file:
                for student in self.students.values():
                    file.write(f"{student.student_id},{student.name},{student.age},{student.grade},{student.email}\n")
            print(f"Student data saved to {filename}")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename="students.txt"):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split(',')
                        if len(parts) == 5:
                            student_id, name, age, grade, email = parts
                            student = Student(int(student_id), name, int(age), grade, email)
                            self.students[int(student_id)] = student
                            if int(student_id) >= self.next_id:
                                self.next_id = int(student_id) + 1
            print(f"Student data loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with empty system.")
        except Exception as e:
            print(f"Error loading from file: {e}")

def main():
    system = StudentRegistrationSystem()
    system.load_from_file()  # Load existing data if available

    while True:
        print("\n=== Student Registration System ===")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. List All Students")
        print("4. View Student Information")
        print("5. Update Student Information")
        print("6. Save Data")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            # Add student
            name = input("Enter student name: ").strip()
            if not name:
                print("Name cannot be empty")
                continue

            age_input = input("Enter student age: ").strip()
            try:
                age = int(age_input)
                if age < 1 or age > 120:
                    print("Please enter a valid age (1-120)")
                    continue
            except ValueError:
                print("Please enter a valid age")
                continue

            grade = input("Enter student grade: ").strip()
            if not grade:
                print("Grade cannot be empty")
                continue

            email = input("Enter student email: ").strip()
            if not email:
                print("Email cannot be empty")
                continue

            system.add_student(name, age, grade, email)

        elif choice == '2':
            # Remove student
            id_input = input("Enter student ID to remove: ").strip()
            try:
                student_id = int(id_input)
                system.remove_student(student_id)
            except ValueError:
                print("Please enter a valid student ID")

        elif choice == '3':
            # List students
            system.list_students()

        elif choice == '4':
            # View student info
            id_input = input("Enter student ID to view: ").strip()
            try:
                student_id = int(id_input)
                system.view_student_info(student_id)
            except ValueError:
                print("Please enter a valid student ID")

        elif choice == '5':
            # Update student info
            id_input = input("Enter student ID to update: ").strip()
            try:
                student_id = int(id_input)
                system.update_student_info(student_id)
            except ValueError:
                print("Please enter a valid student ID")

        elif choice == '6':
            # Save data
            system.save_to_file()

        elif choice == '7':
            # Exit
            system.save_to_file()  # Auto-save before exit
            print("Thank you for using the Student Registration System!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
