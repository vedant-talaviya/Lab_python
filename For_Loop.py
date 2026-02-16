# 1 print numbers from 1 to 5
for i in range (1,6):
    print(i)

# 2 print a msg 3 times
for i in range(3):
    print("HELLO")

# 3 print numbers from 1 to 10
for i in range (1,11):
    print(i)

# 4 print even numbers from 1 to 20
for i in range (1,21):
    if(i %2==0):
        print(i)

# 5 print odd numbers from 1 to 15
for i in range (1,16):
    if(i%2==1):
        print(i)

# 6 print table of 5
for i in range (1,11):
    print("5 x ",i,"=",5*i)

# 7 print characters of a string 
name="Vedant"
for letter in name :
    print(letter)

# 8 sum of numbers from 1 to 5
total=0
for i in range(1,6):
    total=total+i
    print("Sum is:",total)

# 9 print list elements
numbers=[10,20,30,40,50]
for n in numbers:
    print(n)