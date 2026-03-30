src=open("nothing.txt", "r")
data=src.read()
src.close()

dst=open("mergedd.txt", "w")
dst.write(data)
dst.close()
print("File copied successfully.")