class Student:

    population = 0

    def __init__(self, name, age, subject):

        self.name = name
        print("(Initializing{})".format(self.name))

        Student.population += 1

    def say_hi(self):
        """Hi."""

        print("Greetings, hi{}".format(self.name))


        if Student.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} students.".format(
                Student.population
            ))
    def transfer(self):

        """Transfer."""

        print("Transfer.{}".format(self.name))
        Student.population -= 1

    @classmethod
    def how_many(cls):
        """Print the current population."""

        print("We have {:d} students.".format(cls.population))


student1 = Student("Mg Mg", 14, "Bio")
student1.say_hi()
student1.how_many()


student2 = Student("Ma Ni", 13, 'Eco')
student2.say_hi()
student2.how_many()

student3 = Student("Hla HLa", 12, 'Eco')
student3.say_hi()
student3.how_many()

student2.transfer()




