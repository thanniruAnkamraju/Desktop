## two child class inherits the parent is called  hierachical inheritance
class Parent:
    def fun1(self):
        print("this is parent class")
class Child1(Parent):
    def fun2(self):
        print("this is child class")
class Child2(Parent):
    def fun3(self):
        print("this is child2 class")
ob=Child2()
obj=Child1()
ob.fun3();
obj.fun2();
ob.fun1();