rollno=int(input("enter rollno:"))
name=str(input("enter your name:"))
class student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def show_student(self):
        print(self.rollno)
        print(self.name)
s1=student(rollno,name)
s1.show_student()
