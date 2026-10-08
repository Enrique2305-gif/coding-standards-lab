class Student:
    def __init__(self, student_id, name):
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Error: Student ID cannot be empty.")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Error: Student name cannot be empty.")

        self.id = student_id.strip()
        self.name = name.strip()
        self.gradez = []
        self.isPassed = False
        self.honor = False

    def addGrades(self, grade):
        if not isinstance(grade, (int, float)) or isinstance(grade, bool):
            print("Error: Grade must be a number.")
            return

        if grade < 0 or grade > 100:
            print("Error: Grade must be between 0 and 100.")
            return

        self.gradez.append(grade)

    def calcaverage(self):
        if len(self.gradez) == 0:
            return 0

        total = 0
        for grade in self.gradez:
            total += grade

        average = total / len(self.gradez)
        return average

    def checkHonor(self):
        self.honor = self.calcaverage() >= 90
        return self.honor

    def get_letter_grade(self):
        average = self.calcaverage()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def deleteGrade(self, target, by="index"):
        if by == "index":
            if type(target) is not int or not 0 <= target < len(self.gradez):
                print("Error: Invalid grade index.")
                return False

            self.gradez.pop(target)

        elif by == "value":
            if target not in self.gradez:
                print("Error: Grade not found.")
                return False

            self.gradez.remove(target)

        else:
            print("Error: Invalid removal method.")
            return False

        self.checkHonor()
        self.check_pass()
        return True

    def check_pass(self):
        self.isPassed = self.calcaverage() >= 60

        if self.isPassed:
            return "Passed"

        return "Failed"

    def report(self):
        self.checkHonor()
        status = self.check_pass()

        print("\n--- STUDENT SUMMARY REPORT ---")
        print(f"Student ID: {self.id}")
        print(f"Student Name: {self.name}")
        print(f"Number of Grades: {len(self.gradez)}")
        print(f"Average Grade: {self.calcaverage():.2f}")
        print(f"Letter Grade: {self.get_letter_grade()}")
        print(f"Pass/Fail: {status}")
        print(f"Honor Roll: {self.honor}")


def startrun():
    print("=== CASE 1: VALID STUDENT ===")

    student = Student("001", "Ana Torres")
    student.addGrades(95)
    student.addGrades(90)
    student.addGrades(100)
    student.report()

    print("\n=== CASE 2: REMOVE GRADES ===")

    student.deleteGrade(1)
    student.deleteGrade(100, by="value")
    student.report()

    student.deleteGrade(10)
    student.deleteGrade(50, by="value")

    print("\n=== CASE 3: INVALID INPUTS ===")

    student.addGrades("Fifty")
    student.addGrades(-10)
    student.addGrades(120)

    try:
        Student("", "Carlos")
    except ValueError as error:
        print(error)

    try:
        Student("002", "")
    except ValueError as error:
        print(error)

    print("\n=== CASE 4: LETTER GRADES ===")

    grades = [90, 80, 70, 60, 50]

    for index, grade in enumerate(grades):
        student = Student(str(index + 100), f"Student {index + 1}")
        student.addGrades(grade)
        student.report()

    print("\n=== CASE 5: STUDENT WITHOUT GRADES ===")

    student = Student("999", "Pedro Lopez")
    student.report()


startrun()
