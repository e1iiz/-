# class Car:
#     def __init__(self,brend,model,year):
#         self.brend=brend
#         self.model=model
#         self.year=year

#     def display_info(self):
#         print(f"Марка: {self.brend},Модель: {self.model},Год выпуска: {self.year}")

# car=Car("Toyota","Camry",2021)
# car.display_info()


# class ElectricCar(Car):
#     def __init__(self, brend, model, year,battery_capacity):
#         super().__init__(brend, model, year,battery_capacity)
#         self.battery_capacity=battery_capacity

#     def display_battery_info(self):
#         print(f"Емкость батареи: {self.battery_capacity} kWh")
        

# # car2=Car("Honda","Jazz",2020)
# # car2.display_info()
# bater=ElectricCar("Toyota","Camry",2020, 100)
# bater.display_info()
# bater.display_battery_info()


# class Car:
#     def __init__(self,brend,model,year):
#         self.brend=brend
#         self.model=model
#         self.year=year
#         self.__mileage=0

#     def display_info(self):
#         print(f"Марка: {self.brend},Модель: {self.model},Год выпуска: {self.year}")

#     def set_mileage(self,mileage):
#         self.__mileage=mileage

#     def get_mileage(self):
#         return self.__mileage
    
# car=Car("Toyota","Camry",2021)
# car.set_mileage(1500)   
# print(f"пробег{car.get_mileage()}км")


class Dog:
    def make_sound(self):
        print("woof")

class Cat:
    def make_sound(self):
        print("meow")

animals=[Dog(),Cat()]
for animal in animals:
    animal.make_sound()




