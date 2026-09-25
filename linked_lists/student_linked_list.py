class Student:
    def __init__(self, name, roll_number, department):
        self.name = name
        self.roll_number = roll_number
        self.department = department
        self.next = None


ali = Student("Ali", 101, "Computer Science")
sara = Student("Sara", 102, "Software Engineering")
ahmed = Student("Ahmed", 103, "Information Technology")

ali.next = sara
sara.next = ahmed

print(ali.name, ali.roll_number, ali.department)
print(sara.name, sara.roll_number, sara.department)
print(ahmed.name, ahmed.roll_number, ahmed.department)
