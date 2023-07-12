###Multiple inheritance:multiple parent inherits to the child class
class Father:
    def fun1(self):
        print("hello father")
class Mother:
    def fun2(self):
       print("hello Mother") 
class Child(Mother,Father):
    def fun3(self):
        print("this is child class")
obj=Child()
obj.fun3()
obj.fun2()
obj.fun1()
