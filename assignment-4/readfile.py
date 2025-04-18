filename="sample.txt"
try:
    file1=open(filename,"r")
    reading_file=file1.read()
    print(reading_file)
    file1.close()
except FileNotFoundError:
    print("The file "+filename+" was not found")

