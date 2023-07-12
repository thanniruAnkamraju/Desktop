
# #  single inheritance : inherite the properties from the parent to child###
# class Parent:
#     def fun1(self):
#         print("this is parent class")
        
# class Child(Parent):
#     def fun2(self):
#         print("this is the child class")
# ob=Child()
# ob.fun1()
# ob.fun2()
 
 ##example 2
# class Dad:
#     def fun1(self,height,width):
#         area=height*width
#         print("Area of rectangle:",area)
# class Son(Dad):
#     def fun2(self,side):
#         area=side*side
#         print("Area of square:",area)
# obj=Son()
# obj.fun2(10)
# obj.fun1(12,4)

# ###Multi level inheritance:allows a class to inherit properties and methods
# from a class that is already inherited from another class.  ###

# class Parent:
#     def fun1(self):
#         print("hii raju")
# class Child(Parent):
#     def fun2(self):
#         print("I like car")
# class Grandchild(Child):
#     def fun3(self):
#         print("I like driving car")
# obj=Grandchild()
# obj.fun3()
# obj.fun2()
# obj.fun1()
## Ex:2 multilevel inheritance
class Dad:
    def fun1(self,length,bredth,height):
      area=length*bredth*height
      print("area of rectangle=",area)
      
class Parent(Dad):
     def fun2(self,side):
      area=side*side
      print("area of square=",area)
class Grandchild(Parent):
    def fun3(self,length,bredth):
        area=(length+bredth)
        print("area of rectangle=",area)
ob = Grandchild()
ob.fun3(23,34)
ob.fun2(2)
ob.fun1 (10,3,3) 
    
    