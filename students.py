
class Person:
    def __init__(self, name, intelligence):
        self.name = name
        self.intelligence = intelligence

    def study(self):
        return f"{self.name} is studying!"
 
info = {"Joe": 145, "Ron": 90, "Jayne": 2000, "Fox": 1, "Hif": 100}
student_list = [Person(name, intelligence) for name, intelligence in info.items()]


def asign_value(the_list, number, type_of_information):
    val1 = the_list[number]

    if type_of_information == 0:
        return val1.study()
    elif type_of_information == 1:
        return val1.name
    elif type_of_information == 2:
        return val1.intelligence

students = student_list

