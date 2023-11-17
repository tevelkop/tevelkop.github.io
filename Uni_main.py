from students import asign_value
from students import students
import json
class being_in_uni:
    def __init__(self,list_of_students,uni_name):
       
        self.list=list_of_students
        self.uni_name=uni_name  
        
           
        
    def filter_students_from_entrence(self):

        for i in range(len(self.list)):
           v=asign_value(self.list,i,2)
           if v>=100:
               pass
           elif v<100:
            self.list[i]=""
        for left_slots in self.list:
            if left_slots=="":
             self.list.remove(left_slots)

            
        
    def make_study(self):
        for student in self.list:
                  study_result = student.study()
                  print(study_result)
              
    def graduates_list(self):
        grad_content={self.uni_name:{stud.name:stud.intelligence for stud in self.list}}
        
        with open("grad_file.json","x") as grad_file:
            json.dump(grad_content,grad_file)
    
class access_to_file:
    def __init__(self,companies_that_can_see_grads):
        self.accept=companies_that_can_see_grads
    def access_grandted(self,current_one):
        if current_one in self.accept:
            with open("grad_file.json") as grad_file:
               content= json.load(grad_file)
               return content
        else:
            return "access_denied"

Payer=being_in_uni(students,"Andrew_uni")
Payer.filter_students_from_entrence()
Payer.make_study()
Payer.graduates_list()
exceptance_list=["space_x","ex_x","x","mix",Payer.uni_name]
access=access_to_file(exceptance_list)
choose=input("what is the entity?")
print(access.access_grandted(choose))

