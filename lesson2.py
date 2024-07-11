# ООп _ наследования 

class Transport:

    def __init__(self,model,year,color):
        self.model=model
        self.year=year
        self.color=color

    def info(self):
        print(f"бренд транспорта- {self.model},Год выпуска- {self.year},Цвет -{self.color}")

class Car(Transport):
    def __init__(self, model, year, color,penaltis=2000):
        # Transport.__init__(self,model,year,color) #напоямую к классу
        super().__init__(model, year, color)
        self.penaltis=penaltis

lexus=Car("lx 300",2023,"white")
lexus.info()
print(lexus.penaltis)


# class Animals:
#     def __init__(self,name,bread,age):
#         self.name=name
#         self.bread=bread
#         self.age=age

#     def speak(self):
#         pass

# class Dog(Animals):
#     def __init__(self, name, bread, age):
#         super().__init__(name, bread, age)
    
#     def speak(self):
#         print(f"woff {self.name}-{self.bread}-{self.age}")

# class Cow(Animals):
#     def __init__(self, name, bread, age):
#         super().__init__(name, bread, age)

#     def speak(self):
#         print(f"moo {self.name}-{self.bread}-{self.age}")

# class Cat(Animals):
#     def __init__(self, name, bread, age):
#         super().__init__(name, bread, age)

#     def speak(self):
#         print(f"myew {self.name}-{self.bread}-{self.age}")

# dog=Dog("Актощ","alabay",2)
# cat=Cat("sara","Muska",3)
# cow=Cow("karadaly","Angust",4)

# dog.speak()
# cat.speak()
# cow.speak()
