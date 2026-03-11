"""#1. Basic positional arguements
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
check_value(-18)"""

#6. Odd or even
def odd_even(no):
    if(no%2==0):
        print(f"value {no} id EVEN")
    else:
        print(f"value {no} is ODD")
odd_even(17)
odd_even(18)
