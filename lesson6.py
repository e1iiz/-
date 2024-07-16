"""Магические методы-dunder """

# class Work:
#     def __init__(self,position,graphicks):
#         self.position=position
#         self.graphicks=graphicks

    # def info(self):
    #     return f"Позиция- {self.position}, график- {self.graphicks}"

    # def __repr__(self):
    #     return f"Позиция- {self.position}, график- {self.graphicks}"
    
#     def __call__(self):
#         return "2+2"
    
# work=Work("nuxgalter","8/5")
# print(work)
# work.info()
# print(work)
# print(work)

# math_num1=int(input("Введите первое число: "))
# math_num2=int(input("Введите второе число: "))
class Math:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2

    def __str__(self):
        return f"первое значение {self.number1} \nВторое значение {self.number2}"
    
    def __add__(self):
        print(f'Резултать сложения {self.number1} и {self.number2}')
        return Math(self.number1+self.number2)
    
    def __sub__(self):
        print(f'Резултать вычитание  {self.number1} и {self.number2}')
        return Math(self.number1 -self.number2)
    
    def __truediv__(self):
        print(f'Резултать умножения {self.number1} и {self.number2}')
        return Math(self.number1*self.number2)  
    
    def __mul__(self):
        print(f'Резултать деления  {self.number1} и {self.number2}')
        return Math(self.number1/self.number2)
    
math_num1=int(input("Введите первое число: "))
operator= input("+,-,*,/")
math_num2=int(input("Введите второе число: "))
math=Math(math_num1,math_num2)
if operator=="+":
    print(math.__add__())
elif operator=="-":
    math.__sub__()
elif operator=="*":
    math.__truediv__()
else:
    math.__mul__()

   

    
    


