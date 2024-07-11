# class Fruits:
#     def __init__(self,name,color,weight):
#         self.name=name
#         self.color=color
#         self.weight=weight

#     def info(self):
#         print(f"название: {self.name},цвет: {self.color},вес: {self.weight}")

# fruit1=Fruits("apple","red",2)
# fruit1.info()



class Heroes:
    def __init__(self,name,role ,health):
        self.name=name
        self.role=role
        self.health=health

    def info(self):
        print(f"Имя: {self.name},Роль: {self.role},Здоровия: {self.health}")

horse=Heroes("Альтиво","Дорога на Эльдорадо",10)
orse=Heroes("Хан","Мулан",9)
rse=Heroes("Пегас","Геркулес",11)
horse.info()
orse.info()
rse.info()