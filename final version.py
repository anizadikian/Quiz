class LinkedList:

    def __init__(self):
        self.head = None

    def addAsLast(self, node):
        if self.head ==None:
            self.head = node
        else:
            tmp =self.head
            while(tmp.next != None):
                tmp = tmp.next

            tmp.next = node

    def find(self, data):
        tmp = self.head
        while (tmp!= None):
            if tmp.isEqual(data):
                return tmp
            tmp = tmp.next
        return None


class Assignment:

    def __init__(self, title, deadline, percent):
        self.title = title
        self.deadline = deadline
        self.percent = percent
        self.grade = 0
        self.next = None

    def __str__(self):
        return self.title + ": " + self.deadline + ": " + str(self.percent)+ "%: " + str(self.grade)

    def addGrade(self, grade):
        self.grade = grade

    def getActualGrade(self):
        return self.grade

    def getCalculatedGrade(self):
        return self.grade * self.percent/100

    def isEqual(self, title):
        return self.title == title

class Course:
    def __init__(self, ID):
        self.ID = ID
        self.assignments = LinkedList()
        self.next = None

    def __str__(self):
        return self.ID

    def addAssignment(self, title, deadline, percent):
        assignment = Assignment(title, deadline, percent)
        self.assignments.addAsLast(assignment)

    def getAssignment(self, title):
        return self.assignments.find(title)

    def addGrade(self, title, grade):
        assignment = self.getAssignment(title)
        if assignment != None:
            assignment.addGrade(grade)
        else:
            print("The Assignment", title, "does not exist for this student")

    def getGrade(self):
        grade = 0
        tmp = self.assignments.head
        while (tmp != None):
            grade = grade + tmp.getCalculatedGrade()
            tmp = tmp.next

        return grade

    def isEqual(self,ID):
        return self.ID == ID


class Student:

    def __init__(self, Fname, Lname, ID):
        self.Fname = Fname
        self.Lname = Lname
        self.ID = ID
        self.courses = LinkedList()

    def __str__(self):
        return self.getFullName() + ": " + self.ID

    def getFullName(self):
        return self.Fname + " " + self.Lname

    def addCourse(self, ID):
        course = Course(ID)
        self.courses.addAsLast(course)

    def addAssignment(self, cID, title, deadline, percent):
        course = self.getCourse(cID)
        if course != None:
            course.addAssignment(title, deadline,percent)
        else:
            print("The course", cID, "does not exist for this student")

    def getCourse(self, ID):
        return self.courses.find(ID)

    def getAssignment(self, cID, title):
        course = self.getCourse(cID)
        return course.getAssignment(title)

    def addGrade(self, cID, title, grade):
        course = self.getCourse(cID)
        if course != None:
            course.addGrade(title, grade)
        else:
            print("The course", cID, "does not exist for this student")

    def getCourseGrade(self, cID):
        course = self.getCourse(cID)
        return course.getGrade()

    def getStudentGrade(self):
        grade = 0
        count = 0
        tmp = self.courses.head
        while (tmp != None):
            title = tmp.ID
            grade_tmp = self.getCourseGrade(title)
            grade = grade + grade_tmp
            tmp = tmp.next
            count = count +1
        avg = grade /count
        return avg


def main():
    my_student = Student("Artur", "Sargsyan", "AUA234")
    print(my_student)

    #Adding Courses
    my_student.addCourse("ENGS115")
    print(my_student.getCourse("ENGS115"))
    print(my_student.getCourse("ENGS105"))

    #Adding Assignments
    my_student.addAssignment("ENGS115", "Implement Browser History Using Stack", "2019-10-31",50)
    print(my_student.getAssignment("ENGS115", "Implement Browser History Using Stack"))

    my_student.addAssignment("ENGS115", "Implement Browser History Using Queue", "2019-11-05",50)
    print(my_student.getAssignment("ENGS115", "Implement Browser History Using Queue"))

    # Adding Grades
    my_student.addGrade("ENGS115", "Implement Browser History Using Stack",100)
    my_student.addGrade("ENGS115", "Implement Browser History Using Queue", 100)
    print(my_student.getAssignment("ENGS115", "Implement Browser History Using Stack"))
    print(my_student.getAssignment("ENGS115", "Implement Browser History Using Queue"))

    #Get Grades
    my_student.getCourseGrade("ENGS115")
    print(my_student.getCourseGrade("ENGS115"))
    my_student.getStudentGrade()
    print(my_student.getStudentGrade())

main()
