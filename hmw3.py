class Computer:
    def __init__(self,cpu,memory):
        self.__cpu=cpu
        self.__memory=memory

    def __make_computations(self):
        result=(f'Сумма: {self.__cpu+self.__memory}',
                f'Вычисление: {self.__cpu-self.__memory}',
                f'Умножение: {self.__cpu*self.__memory}',
                f'Деление: {self.__cpu*self.__memory}')
        
        return result
    
    def access_private(self):
        return self.__make_computations()
# comp=Computer(10,128)
# print(comp.access_private())
    
class Laptop(Computer):
    def __init__(self, cpu, memory,memory_card=256):
        super().__init__(cpu, memory)
        self.memory_card=memory_card

    def info(self):
        self.access_private()
        res=(f"Карта памяти: {self.memory_card}")
        return res
   
laptop=Laptop(10,3)
print(laptop.access_private())
print(laptop.info())
# laptop.info(256)
# print(laptop.memory_card)