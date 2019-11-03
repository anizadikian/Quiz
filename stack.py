class Assignment:

    def __init__(self, title=None, deadline=None, percent=None):
        self.title = title
        self.deadline = deadline
        self.percent = percent
        self.grade = 0
        self.next = None

    def __str__(self):
        return self.title + ": " + self.deadline + ": " + str(self.percent) + ": " + str(self.grade)

    def addGrade(self, grade):
        self.grade = grade

    def getActualGrade(self):
        return self.grade

    def getCalculatedGrade(self):
        return self.grade * self.percent/100


class Course:
    def __init__(self, ID=None):
        self.ID = ID
        self.assignments = []

    def __str__(self):
        return self.ID

    def addAssignment(self, title, deadline, percent):
        assignment = Assignment(title, deadline, percent)
        self.assignments.append(assignment)

    def getAssignment(self, title):
        for item in self.assignments:
            if (item.title == title):
                return item
        return None

    def addGrade(self, title, grade):
        assignment = self.getAssignment(title)
        if (assignment != None):
            assignment.addGrade(grade)
        else:
            print("The Assignment", title, "doesn't exist for the student")

    def getGrade(self):
        grade = 0
        for item in self.assignments:
            grade = grade + item.getCalculatedGrade()
        return grade



class Student:
    def __init__(self, fName=None, lName=None, ID=None):
        self.fName = fName
        self.lName = lName
        self.ID = ID
        self.courses = []

    def __str__(self):
        return self.getFullName() + ": " + self.ID

    def getCourse(self, ID):
        for item in self.courses:
            if (item.ID == ID):
                return item
        return None

    def getFullName(self):
        return self.fName + " " + self.lName

    def addCourse(self, ID):
        course = Course(ID)
        self.courses.append(course)

    def addAssignment(self, cID, title, deadline, percent):
        course = self.getCourse(cID)
        if (course != None):
            course.addAssignment(title, deadline, percent)
        else:
            print("The Course", cID, "doesn't exist for the student")

    def getAssignment(self, cID, title):
        course = self.getCourse(cID)
        return course.getAssignment(title)

    def addGrade(self, cID, title, grade):
        course = self.getCourse(cID)
        if (course != None):
            course.addGrade(title, grade)
        else:
            print("The Course", cID, "doesn't exist for the student")

    def getCourseGrade(self, cID):
        course = self.getCourse(cID)
        return course.getGrade()

    def getAssignmentGrade(self, cID, title):
        assigment = self.getAssignment(cID, title)
        return assigment.getGrade()

    def AssignmentCalculatedGrade(self):
        pass

class Stack:

    def __init__(self):
        self.__head = None

    def isEmpty(self):
        if self.__head == None:
            return True
        else:
            return False

    def pushAssigment(self, newtitle, newdeadline):
        if self.__head == None:
            self.__head = Assignment(newtitle, newdeadline)
        else:
            newData = Assignment(newtitle, newdeadline)
            newData.next = self.__head
            self.__head = newData

    def pushCourse(self, newID):
        if self.__head == None:
            self.__head = Course(newID)
        else:
            newData1 = Course(newID)
            newData1.next = self.__head
            self.__head = newData1

    def pushStudent(self, fName, lName, ID):
        if self.__head == None:
            self.__head = Student(fName, lName, ID)
        else:
            newData2 = Student(fName, lName, ID)
            newData2.next = self.__head
            self.__head = newData2




def main():
    my_student = Student("Arthur", "Sargsyan", "AUA234")
    print(my_student)

    #Adding Ccourses
    my_student.addCourse("ENGS115")
    print(my_student.getCourse("ENGS115"))
    print(my_student.getCourse("ENGS103"))

    #Adding Assignments
    my_student.addAssignment("ENGS115", "Implement Browser History using Stack", "2019-10-31", 30)
    print(my_student.getAssignment("ENGS115", "Implement Browser History using Stack"))

    #Adding Assignments
    my_student.addAssignment("ENGS115", "Implement Browser History using Queue", "2019-11-05", 40)
    print(my_student.getAssignment("ENGS115", "Implement Browser History using Queue"))

    #adding Grades
    my_student.addGrade("ENGS115", "Implement Browser History using Stack", 90)
    my_student.addGrade("ENGS115", "Implement Browser History using Queue", 50)
    print(my_student.getAssignment("ENGS115", "Implement Browser History using Stack"))
    print(my_student.getAssignment("ENGS115", "Implement Browser History using Queue"))

    print(my_student.getCourseGrade("ENGS115"))
    # my_student.getAssignmentGrade("ENGS115", "Implement Browser History using Stack")
    # my_student.getAssignmentCalculatedGrade("ENGS115", "Implement Browser History using Stack")

main()
