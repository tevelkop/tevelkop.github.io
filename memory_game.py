import random
game_continue=True
red_points=[]
blue_points=[]
represent_closed_card_shown_to_user=""

class simulate_plate:
        def __init__(self,plate):
    
             global index_closed_card_content
             self.plate=plate
             index_closed_card_content=[int(index) for index,_ in enumerate(self.plate)]
             for index_for_identifying_card,_ in enumerate(index_closed_card_content):
                     
                if self.plate[index_for_identifying_card]=="_":
                     index_closed_card_content[index_for_identifying_card]="_"
                        
             represent_closed_card_shown_to_user = index_closed_card_content#closed_card_index_shown_to_user

             self.show_template=f"    {represent_closed_card_shown_to_user[0]} ,{represent_closed_card_shown_to_user[1]} ,{represent_closed_card_shown_to_user[2]} ,{represent_closed_card_shown_to_user[3]} \n\
    {represent_closed_card_shown_to_user[4]} ,{represent_closed_card_shown_to_user[5]} ,{represent_closed_card_shown_to_user[6]} ,{represent_closed_card_shown_to_user[7]} \n\
    {represent_closed_card_shown_to_user[8]} ,{represent_closed_card_shown_to_user[9]} ,{represent_closed_card_shown_to_user[10]} ,{represent_closed_card_shown_to_user[11]} \n\
    {represent_closed_card_shown_to_user[12]} ,{represent_closed_card_shown_to_user[13]} ,{represent_closed_card_shown_to_user[14]} ,{represent_closed_card_shown_to_user[15]}\n "
             
        def close(self):
            print(self.show_template)
            
        def open(self,option_1,option_2):
            index_card_to_open = index_closed_card_content
            
            index_card_to_open[option_1]=self.plate[option_1]
            index_card_to_open[option_2]=self.plate[option_2]
            print(f"    {index_card_to_open[0]} ,{index_card_to_open[1]} ,{index_card_to_open[2]} ,{index_card_to_open[3]} \n\
    {index_card_to_open[4]} ,{index_card_to_open[5]} ,{index_card_to_open[6]} ,{index_card_to_open[7]} \n\
    {index_card_to_open[8]} ,{index_card_to_open[9]} ,{index_card_to_open[10]} ,{index_card_to_open[11]} \n\
    {index_card_to_open[12]} ,{index_card_to_open[13]} ,{index_card_to_open[14]} ,{index_card_to_open[15]}\n ")

        def check_if_game_ended(self):
            if len([i for i in represent_closed_card_shown_to_user if i=="_"])==16:
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
    game_finished=Sim_plate.check_if_game_ended()
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
        game_finished=Sim_plate.check_if_game_ended()
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
    game_finished=Sim_plate.check_if_game_ended()
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
