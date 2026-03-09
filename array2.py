#1. positive indexing
from array import array
a = array('i', [10, 20, 30, 40, 50])
print(a[0])
print(a[2])
print(a[4])

#2. negative indexing
from array import array
a = array('i', [10, 20, 30, 40, 50])
print(a[-1])
print(a[-2])
print(a[-5])

#3. modifying elements using index
from array import array
arr= array('i', [10, 20, 30, 40, 50])
arr[2] = 35
print(arr)

#4. index error
from array import array
arr = array('i', [10, 20, 30])
print(arr[5])