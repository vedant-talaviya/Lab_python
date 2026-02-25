"""# 1. Print numbers from 1 to 10
i=1
while i<10:
 print(i)
 i=i+1

# 2. sum of first n natural numbers 
n=int(input("Enter a number :"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
    print("sum = ",sum)

# 3. Table of a number
num=int(input("Enter a number:"))
i=1
while i<=10:
    print(num,"*",i,"=",num*i)
    i=i+1

# 4. Print numbers from 1 to 5
i=1
while i<=5:
 print(i)
 i=i+1

# 5.sum of numbers take user input
n=int(input("Enter a number:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
    print("Sum = ",sum)

# 6. print odd numbers between 1 to 20
i=1
while i<=20:
    if i%2!=0:
        print(i)
    i=i+1

# 7. print table of 4
num=4
i=1
while i<=10:
    print(num,"*",i,"=",num*i)
    i=i+1

# 8. print reverse number of 1 to 10
i=10
while i>=1:
    print(i)
    i=i-1"""

# 9. find largest number in list
numbers = [10,5,8,20,15]
i=0
largest = numbers[0]
while i<len(numbers):
    if numbers[i]>largest:
        largest = numbers[i]
        i=i+1
        print("Largest number is",largest)

"""# 10. print even numbers from 1 to 10
i=1
while i<=10:
    if i%2==0:
        print(i)
        i=i+1"""
