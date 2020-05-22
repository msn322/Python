class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def intro(self):
        print("My name is " + self.name)


r3 = Robot("Manpreet Singh","Blue",90)
r3.intro()

