class Myclass:
    __privateVar = 27


    def __privMeth(self):
        print('i am inside class my class')

    def hello(self):
        print('private varieable Vale = ', Myclass.__privateVar)

foo = Myclass()
foo.hello()
foo.__privMeth
