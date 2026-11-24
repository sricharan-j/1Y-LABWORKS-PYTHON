# Menu-Driven Student Information Management

students = {}

def add_student():
    roll_no = input("Enter Roll Number: ")
    if roll_no in students:
        print("Student already exists!")
        return
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    cgpa = float(input("Enter CGPA: "))
    students[roll_no] = {"Name": name, "Dept": dept, "CGPA": cgpa}
    print("Student added successfully!")

def display_students():
    if not students:
        print("No student records found!")
        return
    print("\n--- Student Records ---")
    for roll_no, details in students.items():
        print(f"Roll No: {roll_no} | Name: {details['Name']} | Dept: {details['Dept']} | CGPA: {details['CGPA']}")

def search_student():
    roll_no = input("Enter Roll Number to search: ")
    if roll_no in students:
        details = students[roll_no]
        print(f"Found - Name: {details['Name']}, Dept: {details['Dept']}, CGPA: {details['CGPA']}")
    else:
        print("Student not found!")

def update_student():
    roll_no = input("Enter Roll Number to update: ")
    if roll_no in students:
        name = input("Enter new Name: ")
        dept = input("Enter new Department: ")
        cgpa = float(input("Enter new CGPA: "))
        students[roll_no] = {"Name": name, "Dept": dept, "CGPA": cgpa}
        print("Student record updated successfully!")
    else:
        print("Student not found!")

def delete_student():
    roll_no = input("Enter Roll Number to delete: ")
    if roll_no in students:
        del students[roll_no]
        print("Student record deleted successfully!")
    else:
        print("Student not found!")

while True:
    print("\n--- Student Information System ---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")