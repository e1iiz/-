#ООП -обьектно ориентированное программирование 

# class Person:
#     def __init__(self,name,lastname,age,nationality): #__init__ это конструктор, self: сам обьект
#         self.name = name
#         self.lastname=lastname
#         self.age=age
#         self.nationality=nationality

#     def info(self):
#         print(f"Имя {self.name},Фамиля {self.lastname},Возраст{self.age},нация{self.nationality}")

# person=Person("eliza","Erkinbek kyzy",18,"kyrgyz")
# person.info


# class People:
#     def __init__(self,logyn,password,email,):
#         self.logyn=logyn
#         self.password=password
#         self.email=email
    
#     def info(self):
#         print(f"Ваш логин:{self.logyn},Пароль:{self.password},Адрес почты(email){self.email}")

# person=People("eliiz","@_e1iizko","telefonr499@gmail.com")
# person.info()



class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def book1(self):
        print(f"Книга:{self.title}, Автор: {self.author}")
book2=Book("Ак кеме ","Ч.Айтматов")
book2.book1()



