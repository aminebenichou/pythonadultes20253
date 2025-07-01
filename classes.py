class Student:
    level = 0
    moyenne = 0
    marks = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        print("object initialized")

    
    def countMoyenne(self):
        total = 0
        for mark in self.marks :
            total = total + mark
        moyenne = total/len(self.marks)
        return moyenne

first_student = Student(name="hello", age=24)
first_student.marks = [12, 15, 19, 17]
print(first_student.countMoyenne())


class Player:
    health = 100
    username = ""
    score = 0



players = [
    'test'
    'test'
    'test'
    'test'
    'test'
]
for x in players:
    Player().username = x