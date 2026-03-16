#1. Basic positional arguements
def add(a,b):
    print("A = ",a)
    print("B =",b)
    return a+b
result = add(2,5)
print("sum = ",result)

#2. Student information
def student_info(name,roll,marks):
    print("Name : ",name)
    print("Roll : ",roll)
    print("Marks",marks)
student_info ("Vedant",101,89)

#3. Simple interest
def simple_interest (p,r,n):
    si=(p*r*n)/100
    print("Simple interest : ",si)
simple_interest(1000,2,2)
simple_interest(5000,1.2,3)

#4. Area of circle
def ar_circle(r):
    a_circle=3.14*r*r
    print("Area of circle : ",a_circle)
ar_circle(1.5)
ar_circle(4)

#5. Check number positive,negative or zero
def check_value(no):
    if(no>0):
        print("positive")
    elif(no<0):
        print("negative")
    else:
        print("Zero")
check_value(0)
check_value(18)
check_value(-18)

#6. Odd or even
def odd_even(no):
    if(no%2==0):
        print(f"value {no} id EVEN")
    else:
        print(f"value {no} is ODD")
odd_even(17)
odd_even(18)

#7. Arithmetic operation
def addition(a,b):
    add=a+b
    print("Addition of two values:",add)
addition(50,10.5)
addition(100,200)

#8. Basic keyword arguements
def simple_interest(p:float,t:float,r:float):
    si=(p*r*t)/100
    print("Simple interest : ",si)
simple_interest (p=10000,t=2.5,r=3.5)

#9. Default arguements ex1
def sqr(num,exp=2):
    return num**exp
print(sqr(3))
print(sqr(3,3))
print(sqr(2,4))

#10. Default arguements ex2
def greet(name="Guest"):
    print("Hello",name)
greet("Vedant")
greet()

#11. Default arguements ex3
def add(a,b=5):
    print("Sum : ",a+b)
add(10,20)
add(10)