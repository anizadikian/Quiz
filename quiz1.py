class Student:

    def __init__(self, name=None, surname=None, ID=None):
        self.name = name
        self.surname = surname
        self.ID = ID
        self.courses = []
        self.next = None

    def addCourse(self):
        newcourse = Course(assigment=, deadline=)
        self.courses.append(newcourse)

    def addAssigment(self, coursename, assigment, deadline):
        newassigment = Course(coursename, assigment, deadline)
        self.assigments.append(newassigment)


class Course:

    def __init__(self, coursename, assigment, deadline):
        self.coursename = coursename
        self.assigments = assigment
        self.deadline = deadline
        self.assigments = []

    def addAssigment(self):
        newassigment1 = Assigment(name=, deadline=, grade=)
        self.assigments.append(newassigment1)

class Assigment:

    def __init__(self, name, deadline, grade):
        self.name = name
        self.deadline = deadline
        self.grade = grade
        self.__head = None

    def addGrade(self):
        pass

    #
    # def setHead(self, coursename, assigment, deadline):
    #     self.__head = Student(coursename, assigment, deadline)
    #
    # def display(self):
    #     printval = self.__head
    #     while printval is not None:
    #         print(printval.name, printval.surname, printval.course)
    #         printval = printval.next

    # def append(self, name, grade):
    #     temp = self.__head
    #     while temp.next is not None:
    #         temp = temp.next
    #
    #     student1 = Student(name, grade)
    #     temp.next = student1
    #












