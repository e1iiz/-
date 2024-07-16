class Book:
    def __init__(self,name,author,year_publishing):
        self.name=name
        self.author=author
        self.year_publishing=year_publishing

    def __str__(self):
        return f'Название книг: {self.name} \nАвтор: {self.author} \nГод издания: {self.year_publishing}'

    def __lt__(self,other):
        return (self.year_publishing) < (other.year_publishing)
    
    def __le__(self,other):
        return (self.year_publishing) <= (other.year_publishing)
    
    def __gt__(self,other):
        return self.year_publishing > other.year_publishing
    
    def __ge__(self,other):
        return self.year_publishing >= other.year_publishing
    
    def __eq__(self,other):
        return self.year_publishing == other.year_publishing
    
    def __ne__(self,other):
        return self.year_publishing != other.year_publishing
    
p=Book("Мастер и Маргарита","Михаил Булгаков",2006)

print(p)
print(p<p)
print(p<=p)
print(p>p)
print(p>=p)
print(p==p)
print(p!=p)




