import uuid

class Employee():
    def __init__(self, name, email):
         self.name = name
         self.email = email
         self.generate_id()
    
    def generate_id(self):
        self.id = uuid.uuid4()
        print("Employee id: " + str(self.id))

    def print_atributes(self):
        print("Name: " + self.name)
        print("Email: " + self.email)

class Company():
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self):
        name = input("Enter name: ")
        email = input("Enter email: ")
        print()
        self.employees.append(Employee(name, email))
    
    def print_employees(self):
        for i in self.employees:
            i.print_atributes()

petur = Employee("Petur", "petur@gmail.com")
petur.print_atributes()

print()

company = Company("PetroVil")
company.add_employee()
company.print_employees()
