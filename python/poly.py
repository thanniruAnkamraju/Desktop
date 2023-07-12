### method overloading
##same class name ,same function name and different parameters

class A:
     def sum(self,a,b):
        sum=a+b
        print("Sum=",sum)
     def sum(self,a,b,c,d):
        sum=a+b+c+d
        print("Sum=",sum)
obj=A()
obj.sum(1,12,4)
obj.sum(12,3,4,5)

###Method overriding 
## Different Class name ,differnt parameters,and same function name
class A:
    def func1(self):
        print("hi raju")
class B(A):
    def func1(self):
        print("welcome")
        super().func1() 
obj=B()
obj.func1()

        