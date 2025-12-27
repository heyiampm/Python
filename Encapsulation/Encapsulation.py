class parent:
        def __init__(self,name,age,boy,girl):
                
                self.__name = name   #// this is private
                self.__age = age
                self.__boy = boy
                self.__girl = girl
                print(self.__name)


p1 = parent("pranta", "20" , "man", "not women")
print(p1.name, p1.age, p1.boy, p1.girl)