class student:
    studentcount=0
    def __init__(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
        student.studentcount +=1
    def displaycount(self):
        print("total number",student.studentcount)
    def displaystudent(self):
        print("Roll no:", self.rollno)
        print("Name:",self.name)
        print("Course:",self.course)
stud1=student(10,"mark","MCA")
stud1.displaystudent()
stud1.displaycount()
    
