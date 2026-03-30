try:
    my_list=[1,2,3]
    print(my_list[1])
except IndexError:
    print("Error: Index out of range.")

else:
    print("Element found successfully.")
    
finally:
    print("Program finishes.")