class StudentResultSystem:
    def __init__(self):
        self.students = {}

    def calculate_grade(self, percentage):
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        else:
            return "Fail"

    def add_student(self):
        name = input("Enter student name: ")

        if name in self.students:
            print("Student already exists")
            return

        try:
            math = float(input("Enter Math marks: "))
            physics = float(input("Enter Physics marks: "))
            chemistry = float(input("Enter Chemistry marks: "))
        except:
            print("Invalid marks")
            return

        total = math + physics + chemistry
        percentage = total / 3
        grade = self.calculate_grade(percentage)

        self.students[name] = {
            "Math": math,
            "Physics": physics,
            "Chemistry": chemistry,
            "Total": total,
            "Percentage": percentage,
            "Grade": grade
        }

        print("Student record added successfully!")

    def view_results(self):
        if len(self.students) == 0:
            print("No student records found")
            return

        print("\n--- Student Records ---")
        for name, data in self.students.items():
            print(f"\nName: {name}")
            print(f"Math: {data['Math']}")
            print(f"Physics: {data['Physics']}")
            print(f"Chemistry: {data['Chemistry']}")
            print(f"Total: {data['Total']}")
            print(f"Percentage: {data['Percentage']:.2f}%")
            print(f"Grade: {data['Grade']}")


system = StudentResultSystem()

while True:
    print("\n--- Student Result Management System ---")
    print("1. Add Student Result")
    print("2. View Results")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.view_results()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")