"""
class person:
    def __init__(self,name,intelligence):
        self._name=name 
        self._intelligence=intelligence
    def __call__(self):
      return [self._name,self._intelligence]
    
    def cry(self):
        return f"{self._name} is crying"

class student:
    def __init__(self):
        self.dict={}
        self.list_of_objects=[]
    def __getitem__(self,key):
        self.key=key 
        self.value=self.dict.get(key,None)
        self.list_object()
    def list_object(self): 
        self.object=person(self.key,self.value)
        self.list_of_objects.append(self.object)

info={"Joe":145,"Ron":90,"Jayne":2000,"Fox":1,"Hit":100}
Student=student()
Student.dict=info
keyitems=iter(info.keys())
while True:
    try:
        the_key=next(keyitems)
        Student[the_key]
    except StopIteration:
        break  

def the_value():
    global val
    return val

def asign_value(the_list, number, type_of_information):
    val1 = the_list[number]

    if type_of_information == 0:
        return val1.cry()  # Return the person object
    elif type_of_information == 1:
        return val1()[0]  # Return intelligence
    elif type_of_information ==2:
        return val1()[1]

val = Student.list_of_objects
"""

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
    
 # Use the list of Person objects directly
students = student_list

