class A:
    def __init__(self):
        print("this is class A")
    def fun1(self):
        print("this is Parent class")
class B(A):
    def __init__(self):
        print("this is Class B")
        super().__init__()
    def fun2(self):
        print("this is Child class")
obj=B()

