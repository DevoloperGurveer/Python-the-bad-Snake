class dad:
    def __init__(self,eyes,aggressive):
        self.eyes=eyes
        self.aggressive=aggressive
    def display(self):
        print("Your eye colour is",self.eyes)
        print("You are aggressive",self.aggressive)
class son (dad):
    def __init__(self,name,age,eyes,aggressive):
        self.name=name
        self.age=age
        super().__init__(eyes,aggressive)
obj=son("Penguin",8,"blue",True)
obj.display()