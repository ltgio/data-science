# example of class with with inheritance

CURRENT_YEAR = 2019


class Person:
    def __init__(self, name: str, year_born: int):
        self.name = name
        self.year_born = year_born

    def getAge(self):
        return CURRENT_YEAR - self.year_born

    def __str__(self):
        return "{} ({})".format(self.name, self.getAge())


# define class Student by inheriting from class person all ATTRIBUTES and METHODS
class Student(Person):
    def __init__(self, name, year_born):
        """HOWTO Inherit all the attributes from Person and add knowledge"""
        Person.__init__(self, name, year_born)
        # add new attribute only for student
        self.knowledge = 0

    def study(self):
        self.knowledge += 1

    def getAge(self):
        """
        HOWTO invoke the parent's method
        """
        print('The age of this student it {}'.format(Person.getAge(self)))
        return Person.getAge(self)

alice = Person(name='Alice', year_born=1990)
print(alice)

giovanni = Student('Giovanni', 1989)

giovanni.getAge()