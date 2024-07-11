#абстракция 
from abc import ABC,abstractmethod

#абстрактный класс 
class Payment(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass
#конкретный класс для обработки платежей
class  CreditCardPayment(Payment):
    def process_payment(self, amount):
            return print(f"Оплата произведена по  Кредитной карте, на сумму {amount}$")
    
class PauPalPayment(Payment):
    def process_payment(self, amount):
        return print(f"Оплата произведена по  Кредитной карте, на сумму {amount}$")

#функция для принятия платежей   
def make_payment(payment_method,amount):
     payment_method.process_payment(amount)

#создаем обьект разных видов платежей
credit_card_payment=CreditCardPayment()
paypal=PauPalPayment()

make_payment(credit_card_payment,100)
make_payment(paypal,200)


class Pet(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Pet):
    def make_sound(self):
       print("Woof")


class Cat(Pet):
    def make_sound(self):
        print("Meow")

def play_with_pet(pet):
    pet.make_sound()

dog=Dog()
cat=Cat()
print("Играть с собакой: ")
play_with_pet(dog)

print("Играть с кощкой : ")
play_with_pet(cat)


полиморфизм 

class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        

    def info(self):
        print(f"I'm cat, my name is{self.name},i'm {self.age}years old")

    def make_sound(self):
        print("meaow")
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        

    def info(self):
        print(f"I'm dog, my name is{self.name},i'm {self.age}years old")

    def make_sound(self):
        print("woof")

cat1=Cat("murka",6)
dog1=Dog("alabay",2)

for animal in (cat1,dog1):
    animal.make_sound
    animal.info()
    # animal.make_sound
    # animal.info()
    

from math import pi

class Shape:
    def _init__(self,name):
        self.name=name

    def area(self):
        pass

    def fack(self):
        return "я двуменная фигура"
    
    def __str__(self):
        return self.name
    
class Square(Shape):
    def __init__(self,lenght):
        super().__init__("Square")
        self.lenght=lenght

    def area(self):
        pass

    def fack(self):
        return "У квадрата каждый унгол равен 90 гр"
    
class Circle(Shape):
    def __init__(self,radius):
        super().__init__("Circle")
        self.radius=radius


    def area(self):
        return pi*self.radius**2
    
a=Square(4)
b=Circle(7)
print(b)
print(b.fack())
print(a.fack())
print(b.area())
    

    
