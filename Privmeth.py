class myClass:
    __privateVar=420
    def __privMeth(self):
        print("I'm class inside myClass")
    def hello(self):
            print("Private variable value:",myClass.__privateVar)
foo=myClass()
foo.hello()
foo.__privMeth