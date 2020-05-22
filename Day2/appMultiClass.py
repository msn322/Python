class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def intro(self):
        print("My name is " + self.name)

class Person:
    def __init__(self, name, age, sex, region, is_sitting):
        self.name = name
        self.age = age
        self.sex = sex
        self.region = region
        self.is_sitting = is_sitting

    def intro(self):
        print("My name is " + self.name)

    def stand_up(self):
         self.is_sitting = True
    def sit_down(self):
        self.is_sitting = False

r1 = Robot("Piddu", "Red", 100 )
p1 = Person("Manu", 23, "M", "Europe", True)
p1.intro()

p1.robot_owned = r1
p1.robot_owned.intro()

# pi owns r1
