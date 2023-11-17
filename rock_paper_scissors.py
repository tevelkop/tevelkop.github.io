import random
options =["scissors","rock","paper"]
person1 = "James"
person2= "Clara"
situation = {person1:random.choice(options),person2:random.choice(options)}

def options_interface(situation1):
    dual = []
    dual.append(situation1.get(person1))
    dual.append(situation1.get(person2))
    if "scissors" in dual and "paper" in dual: 
        return f"{[key for key,val in situation1.items() if val=='scissors']} has won!"
    
    elif "rock" in dual  and "paper" in dual:
        return f"{[key for key, val in situation1.items() if val=='paper']} has won!"
    
    elif "scissors" in dual and "rock" in dual:
        return f"{[key for key, val in situation1.items() if val=='rock']} has won!"
    
    else:
        return "no body won"
    
    
example = options_interface(situation)
print(example)
