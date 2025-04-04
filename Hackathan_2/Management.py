class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}Age: {self.age}Gender: {self.gender}"


class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)  
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def get_details(self):
        person_details = super().get_details()  
        return (
            f"{person_details}Employee ID: {self.emp_id}"
            f"Department: {self.department}Salary: {self.salary}"
        )

    def is_eligible_for_bonus(self):
        return self.salary < 50000

    @classmethod
    def from_string(cls, data_string):
        name, age, gender, emp_id, department, salary = data_string.split(",")
        return cls(name, int(age), gender, emp_id, department, float(salary))

    @staticmethod
    def bonus_policy():
        print("Bonus Policy: Employees earning less than 50000 are eligible for a bonus.")


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = [] 

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_average_salary(self):
        if self.employees:  
            total_salary = sum(emp.salary for emp in self.employees)
            return total_salary / len(self.employees)
        return 0

    def get_all_employees(self):
        return [emp.get_details() for emp in self.employees]


import json


def save_to_json(employees, filename="employees.json"):
    with open(filename, 'w') as file:
        employees_data = [emp.__dict__ for emp in employees]
        json.dump(employees_data, file, indent=4)


def load_from_json(filename="employees.json"):
    with open(filename, 'r') as file:
        employees_data = json.load(file)
        employees = []
        for data in employees_data:
            emp = Employee(
                data['name'], data['age'], data['gender'], data['emp_id'], data['department'], data['salary']
            )
            employees.append(emp)
        return employees