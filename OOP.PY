class fruit:
    taste="sweet"
    def __init__ (self,name,color):
        self.name=name
        self.color=color
apple=fruit('Apple','Red')
Banana=fruit('Banana','Yellow')
grapes=fruit('Grapes','Green')
print(apple.taste)
print(apple.name,apple.color)
print(Banana.name,Banana.color)
print(grapes.name,grapes.color)