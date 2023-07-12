print("hello rajukumar")

print("hello nag")

a=10
b=13
if a>b:
    print("a is greater than b")
else:
    print("b is greate than a")
###variables####
name="tom"
rollno="123"
marks=56.4
print("Name:",name)
print("rollno:",rollno)
print("marks:",marks) 

####single value multiple variable

a=b=c=90
print("a:",a)
print("b:",b)
print("c",c)


#### multiple values and multiple variables##

a,b,c=70,80,90
print("a:",a)
print("b:",b)
print("c:",c)

###local variable###
#inside the body is called   local variable

def add():
    x=10
    y=20
    z=x+y
    print("add=",z)
add()
####  global variable : the function is calling outside the body
x=34
y=45
def add():
    print("inside the function =",x+y)
    
    add()
    print("outside the function =",x+y)
        