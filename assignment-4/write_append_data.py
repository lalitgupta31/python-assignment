text1=input("Enter text to write to the file: ")
file1=open("output.txt", "w")
file1.write(text1)
file1.close

text2=input("Enter additional text to append: ")
file1=open("output.txt", "a")
file1.write("\n"+text2)
print("Data successfully appended")
file1.close

file1=open("output.txt", "r")
readfile=file1.read()
print("Final content of output.txt:")
print(readfile)
file1.close()
