import random


game_continue=True
red_points=[]
blue_points=[]
index_of_cards=""
class simulate_plate:
        def __init__(self,plate):
             global metadata_indexes
             self.plate=plate
             metadata_indexes=[int(index) for index,_ in enumerate(self.plate)]
             for value_index,_ in enumerate(metadata_indexes):
                if self.plate[value_index]=="_":
                    metadata_indexes[value_index]="_"
             index_of_cards=metadata_indexes
             self.template=f"    {index_of_cards[0]} ,{index_of_cards[1]} ,{index_of_cards[2]} ,{index_of_cards[3]} \n\
    {index_of_cards[4]} ,{index_of_cards[5]} ,{index_of_cards[6]} ,{index_of_cards[7]} \n\
    {index_of_cards[8]} ,{index_of_cards[9]} ,{index_of_cards[10]} ,{index_of_cards[11]} \n\
    {index_of_cards[12]} ,{index_of_cards[13]} ,{index_of_cards[14]} ,{index_of_cards[15]}\n "
             
        def close(self):
            print(self.template)
            
        def open(self,option_1,option_2):
            a = metadata_indexes
            
            a[option_1]=self.plate[option_1]
            a[option_2]=self.plate[option_2]
            print(f"    {a[0]} ,{a[1]} ,{a[2]} ,{a[3]} \n\
    {a[4]} ,{a[5]} ,{a[6]} ,{a[7]} \n\
    {a[8]} ,{a[9]} ,{a[10]} ,{a[11]} \n\
    {a[12]} ,{a[13]} ,{a[14]} ,{a[15]}\n ")

        def win(self):
            if len([i for i in index_of_cards if i=="_"])==16:
                return True
            else:
                return False
        
class cards_match_or_not:
        def __init__(self,option_1,option_2,metadata_plate):
            self.opt_1=option_1
            self.opt_2=option_2 
            self.plate=metadata_plate
        def __str__(self):
            if self.plate[self.opt_1]==self.plate[self.opt_2]:
                return True
            else:
                if self.plate[self.opt_1]!=self.plate[self.opt_2]:
                    return False
                
        
                
class player:
        def __init__(self,option_1,option_2,plate):
             self.option_1=option_1
             self.option_2=option_2 
             self.plate=plate
             global red_points    
             global blue_points         
        def player_red(self):
            
            red_points.append(self.plate[self.option_1])
            red_points.append(self.plate[self.option_2])
                
            print(red_points)

        def player_blue(self):
           
            blue_points.append(self.plate[self.option_1])
            blue_points.append(self.plate[self.option_2])
        
            print(blue_points)


metadata_plate=["King","QUEEN","Prince","Knight","Soldier","Troop","Dog","Cat"]
metadata_plate=metadata_plate+metadata_plate
random.shuffle(metadata_plate)

while  game_continue==True:
    
    text="move to blue"
    print(f"\033[{34}m{text}\033[0m")
    Sim_plate=simulate_plate(metadata_plate)
    game_finished=Sim_plate.win()
    if game_finished==True:
            game_continue=False
            break
    print("=============================================================")
    
    Sim_plate.close()
    
    card_1=eval(input("give me the first card: "))
    card_2=eval(input("give me the second card: "))
    
    Sim_plate.open(card_1,card_2)
    check=cards_match_or_not(card_1,card_2,metadata_plate)
    TorF=check.__str__()
    
    #===========================================================================
    while TorF==True and metadata_plate[card_1]!="_" and metadata_plate[card_2]!="_" and 0<=card_1<=15 and 0<=card_2<=15:
        game_finished=Sim_plate.win()
        if game_finished==True:
            game_continue=False
            break
        Player=player(card_1,card_2,metadata_plate)
        Player.player_blue()
        
        metadata_plate[card_1:card_1+1]="_"
        metadata_plate[card_2:card_2+1]="_"
        print("=============================================================")
        Sim_plate=simulate_plate(metadata_plate)
        Sim_plate.close()
        
        card_1=eval(input("give me the first card: "))
        card_2=eval(input("give me the second card: "))

        Sim_plate.open(card_1,card_2)
        check=cards_match_or_not(card_1,card_2,metadata_plate)
        TorF=check.__str__()
#===========================================================================
    text="move to red"
    print(f"\033[{31}m{text}\033[0m")
    Sim_plate=simulate_plate(metadata_plate)
    game_finished=Sim_plate.win()
    if game_finished==True:
            game_continue=False
            break
    print("=============================================================")
    Sim_plate.close()
    
    card_1=eval(input("give me the first card: "))
    card_2=eval(input("give me the second card: "))
    Sim_plate.open(card_1,card_2)
    check=cards_match_or_not(card_1,card_2,metadata_plate)
    TorF=check.__str__()

#==================================================================   
    while TorF==True and metadata_plate[card_1]!="_" and metadata_plate[card_2]!="_" and 0<=card_1<=15 and 0<=card_2<=15:
        if game_finished==True:
            game_continue=False
            break
        Player=player(card_1,card_2,metadata_plate)
        Player.player_red()
        
        metadata_plate[card_1]="_"
        metadata_plate[card_2]="_"
        print("=============================================================")
        Sim_plate=simulate_plate(metadata_plate)
        Sim_plate.close()

        card_1=eval(input("give me the first card: "))
        card_2=eval(input("give me the second card: "))
        Sim_plate.open(card_1,card_2)

        check=cards_match_or_not(card_1,card_2,metadata_plate)
        TorF=check.__str__()
print("game is finished!")
print("who won?")
print(f"\033[{34}m{f'blue: {blue_points}'}\033[0m")
print(f"\033[{31}m{f'red: {red_points}'}\033[0m")
if len(blue_points)>len(red_points):
    print("blue won!")
elif(len(blue_points)<len(red_points)):
     print("red won!")
else:
    print("תיקו!")