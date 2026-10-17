# Create a student record manager that saves to a file	
# Dictionaries, file handling, exceptions


def student_manager(records):
    try:
        with open("student_records.txt", "a") as file:
            file.write(str(records) + "\n")
        print("Student record saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving the record: {e}")

def display_records():
    try:
        with open("student_records.txt", "r") as file:
            print("\nStudent Records:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No records found. The file does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the records: {e}")

def search_student(name):
    try:
        with open("student_records.txt", "r") as file:
            for line in file:
                record = eval(line.strip())
                if record["name"] == name:
                    print(f"Record found: {record}")
                    return
    except FileNotFoundError:
        print("No records found. The file does not exist.")

while True:
    print("\n1. Add Student Record")
    print("2. Display Student Records")
    print("3. Search Student Record")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")    
        age = int(input("Enter student age: "))
        grades = list(map(int, input("Enter student grades (comma-separated): ").split(',')))
        student_records = {"name": name, "age": age, "grades": grades}
        student_manager(student_records)
    elif choice == '2':
        display_records()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")