import random

group_people=input("the names of the group") 
list_group_people=group_people.split(" ")
message = input("what is the message?")
Dezibell = eval(input("what is the intensity?"))
the_new_message=message
class phone_game:
    def __init__(self,list_group_people,volume,message):
        self.volume=volume
        self.message=message
        self.list_group_people=list_group_people
        self.constructed_person=person(self.list_group_people)
        self.constructed_messages=messages(self.message)
    def count(self):
        for i in range(len(self.list_group_people)):
            print(self.constructed_person.interpet_the_message())
            if (i+1)%self.volume==0:
                print(self.constructed_messages.change_message())
            else: 
                print(self.message)
class person(phone_game):
    def __init__(self,list_group_people):
        self.list_group_people=list_group_people
        self.person_number=0
    def  interpet_the_message(self):
        name =self.list_group_people[self.person_number]
        self.person_number= self.person_number+1
        return f"{name} is saying:"
    
class messages:
    def __init__(self, message):
        self.message = message
        self.random_letters=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        global the_new_message
        self.the_new_message=the_new_message 
  
    def change_message(self):
       
       self.the_new_message=self.message.replace(random.choice(self.message),random.choice(self.random_letters),1)
       self.message = self.the_new_message
       return self.message

round_1 = phone_game(list_group_people,Dezibell,message)
round_1.count()