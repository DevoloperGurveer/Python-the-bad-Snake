from abc import ABC,abstractmethod
class Animals(ABC):
    def move(self):
        pass
class Human(Animals):
    def move(self):
        print ("I can walk and run")
class Snake(Animals):
    def move(self):
        print ("I can bite you")
class Lion(Animals):
    def move(self):
        print ("I will kill you")
class RCB(Animals):
    def move(self):
        print ("We will never win the IPL")
R=Human()
R.move()
S=Snake()
S.move()
L=Lion()
L.move()
H=RCB()
H.move()