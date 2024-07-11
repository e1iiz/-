class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Фамилия, имя: '{self.fullname}'")
        print(f"Возраст: '{self.age}'")
        print(f"Женат: '{self.is_married}'")

class Student(Person):
    def average_value(self, grades):
        total = sum(grades.values())
        a = total / len(grades)
        return a

class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience=4, salary=10000):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary

    def money_salary(self):
        b = self.salary + (self.experience * 3000)
        return b

person = Person("Erkinbek k Eliza", 18, "No")
person.introduce_myself()

student = Student("Gulasel Kamalova", 18, "No")
student.introduce_myself()
grades = {"Math": 85, "Physics": 90, "Literature": 78}
print(f"Average grade: {student.average_value(grades)}")

teacher = Teacher("Fatima Zulumova", 24, "Yes")
teacher.introduce_myself()
print(f"Ваша зарплата: {teacher.money_salary()}")











    


    