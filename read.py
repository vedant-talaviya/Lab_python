#read
f=open("nothing.txt","r")
data = f.read()
print("File content : ",data)
f.close()

#readline
f=open("nothing.txt","r")
line1 = f.readline()
line2 = f.readline()
print("Line 1:",line1)
print("Line 2:",line2)
f.close()

#readlines()
f=open("nothing.txt","r")
lines = f.readlines()
print("List of lines : ",lines)
print("Number of lines",len(lines))
f.close()

#reading specific line
f=open("nothing.txt","r")
lines=f.readlines()
print(lines[1].strip())
f.close()

