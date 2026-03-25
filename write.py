#write
f=open("nothing.txt","w")
f.write("Hello Students\n")
f.write("Welcome to Python file handling.\n")
f.write("Learning is fun.\n")
f.close()

#writelines
f=open("nothing.txt","w")
lines=["python programming\n","File handling\n","Error handling\n"]
f.writelines(lines)
f.close()