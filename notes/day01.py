
class Zoom:

    def __init__(self,age,name):
        self.__age = age
        self.name = name
    @property
    def eat(self):
        print('hello i am kiko!')

    def set_age(self,age):
        self.__age = age
    def show(self):
        print(" i am %s %d"%(self.name,self.__age))


z1 = Zoom(18,'yuanbao')

z1.show()
z1.set_age(45)
z1.show()