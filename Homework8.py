"""Example 1"""


class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Mammals(Animals):
    def __init__(self, name, age, warm_blooded, presence_of_wool):
        Animals.__init__(self, name, age)
        self.warm_blooded = warm_blooded
        self.presence_of_wool = presence_of_wool


class Human(Mammals):
    def __init__(self, name, age, warm_blooded, presence_of_wool, gender):
        Mammals.__init__(self, name, age, warm_blooded, presence_of_wool)
        self.gender = gender


class Dog(Mammals):
    def __init__(self, name, age, warm_blooded, presence_of_wool, abil_bark):
        Mammals.__init__(self, name, age, warm_blooded, presence_of_wool)
        self.abil_bark = abil_bark


class Cat(Mammals):
    def __init__(self, name, age, warm_blooded, presence_of_wool, abil_MEOW):
        Mammals.__init__(self, name, age, warm_blooded, presence_of_wool)
        self.abil_MEOW = abil_MEOW


"""Example 2"""


class human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class student(human):
    def __init__(self, name, age, gender, college, course, count_homework):
        Human.__init__(self, name, age, gender)
        self.college = college
        self.course = course
        self.count_homework = count_homework
