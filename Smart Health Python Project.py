import sys
class HealthError(Exception):
    pass
class InvalidAgeError(HealthError):
    pass
class FileError(HealthError):
    pass
class Person:
    def __init__(self, name, age):
        if age <= 0:
            raise InvalidAgeError("Age must be positive!")
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Patient(Person):
    def __init__(self, name, age, weight, height):
        super().__init__(name, age)
        self.weight = weight
        self.height = height
        self.history = []
        self.diseases = set()
    def add_record(self, record):
        self.history.append(record)
    def add_disease(self, disease):
        self.diseases.add(disease)
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)
    def wellness_status(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    def display(self):
        super().display()
        print(f"Weight: {self.weight}, Height: {self.height}")
        print(f"BMI: {self.calculate_bmi():.2f}")
        print(f"Status: {self.wellness_status()}")
        print(f"Diseases: {self.diseases}")
        print(f"History: {self.history}")
def save_to_file(patient):
    try:
        with open("patients.txt", "a") as f:
            f.write(f"{patient.name},{patient.age},{patient.weight},{patient.height}\n")
    except Exception:
        raise FileError("Error saving file")
def load_file():
    try:
        with open("patients.txt", "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []
    except Exception:
        raise FileError("Error reading file")
def search_patient_list(patients, name):
    found = False
    for p in patients:
        if name.lower() in p.name.lower():   # string searching
            print("\nPatient Found:")
            p.display()
            found = True
    if not found:
        print("Patient not found")
def average_age(patients):
    total = 0
    for p in patients:
        total += p.age
    return total / len(patients)
def add_sample_data(patients):
    p1 = Patient("Reena", 25, 70, 5.6)
    p1.add_disease("Diabetes")
    p1.add_record("2025 checkup")
    p2 = Patient("Zara", 30, 60, 5.2)
    p2.add_disease("BP")
    patients.append(p1)
    patients.append(p2)
def main():
    patients = []
    if len(sys.argv) > 1:
        print("Command line argument received:", sys.argv[1])
    add_sample_data(patients)
    while True:
        print("\n--- SHM-WAS MENU ---")
        print("1. Add Patient")
        print("2. Display All")
        print("3. Search Patient")
        print("4. Save to File")
        print("5. Exit")
        choice = input("Enter choice: ")
        try:
            if choice == "1":
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                weight = float(input("Enter weight: "))
                height = float(input("Enter height: "))
                p = Patient(name, age, weight, height)
                while True:
                    d = input("Add disease (or 'no'): ")
                    if d.lower() == "no":
                        break
                    p.add_disease(d)
                patients.append(p)
                print("Patient added successfully!")
            elif choice == "2":
                for p in patients:
                    p.display()
            elif choice == "3":
                name = input("Enter name to search: ")
                search_patient_list(patients,name)
            elif choice == "4":
                for p in patients:
                    save_to_file(p)
                print("Saved successfully!")
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice")
        except InvalidAgeError as e:
            print("Error:", e)
        except ValueError:
            print("Invalid input type!")
        except Exception as e:
            print("Unexpected Error:", e)
if __name__ == "__main__":
    main()