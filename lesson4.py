  #Инкапсуляция

class PublicExemple:
    def __init__(self,value):
        self.value=value  #публичный атрибут
        
    def info(self):
        return self.value # Публичный метод
    
public=PublicExemple(42)
print(public.info())  # Вызов публичный 
print(public.value) # Доступ к публичному атрибуту
        

class ProtectedExample:
    def __init__(self,value):
        self._value=value # Защищенный атрибут
    
    def _info(self):
        return self._value # Защищенный метод
    
protected=ProtectedExample(43)
print(protected._value)
print(protected._info())  



Приватный 

class PrivateExample:
    def __init__(self,value):
        self.__value=value # Приватным атрибут
        
    def __info(self):
        return self.__value # Приватный метод
    
    def access_private(self):
        return self.__info() # Публичный метод, где мы получаем доступ к атрибуту
    
private=PrivateExample(77)
# print(private.__value)
print(private.__info())
print(private.access_private())   
print(private._PrivateExample__value)    



class Example(PrivateExample):
    def __init__(self,value,current):
        super().__init__(value)
        self._current=current
        
    def public(self):
        print(f"Приватный - {self.access_private()}, Защищенный {self._current}")
        
example=Example(3,5)
print(example.public())
        
   
  
print(private.access_private())
print(private._PrivateExample__value)













