dict_students={"Alice":85,"Lalit":70,"Mario":90,"Mary":45}
name=input("Enter the student's name: ")
marks=dict_students.get(name)
if marks != None:
    print(name+"'s marks: "+str(marks))
else:
    print("Student not found")