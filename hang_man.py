"""I Developed a text-based hangman game where the user has to guess a random word, one letter at a time."""


def represent_found_chars(letter_from_user,word_to_find):
    global not_break_from_code1
    global GUI_completed_word
    n=0
    if not_break_from_code1==True:
      while(n<len(word_to_find)): 
        GUI_completed_word=GUI_completed_word+"_"
        n=n+1
          
      GUI_completed_word[0]==""
      not_break_from_code1=False
        
    indexes=[int(index) for index,letter in enumerate(word_to_find) if letter==letter_from_user]
    
    for i in indexes:
      GUI_completed_word = GUI_completed_word[:i] + letter_from_user + GUI_completed_word[i+1:]
        
    if GUI_completed_word.count("_")==1:
      GUI_completed_word=GUI_completed_word.replace("_","",1)
      return GUI_completed_word
        
    else:
      return GUI_completed_word
    

    

def set_all_chars_needed_to_find(word_to_find):
    global not_break_from_code2
    if not_break_from_code2==True:
        
        global left_letters_to_win
        for char in word_to_find:
            
          if char not in left_letters_to_win:
            left_letters_to_win += char
              
        not_break_from_code2=False  
        
    return left_letters_to_win



def game_cycle(letter_from_user,word_to_find):
    global heart
    global left_letters_to_win
    global game
    global GUI_completed_word
    
    if("_" in GUI_completed_word):
      

      if letter_from_user in set_all_chars_needed_to_find(word_to_find):

        left_letters_to_win = left_letters_to_win.replace(letter_from_user,"")
        print(represent_found_chars(letter_from_user,word_to_find))

      else:
        print("wrong!")
        print(GUI_completed_word)
        heart=heart-1
    else:
      print("you gained succces!")
      game=False
    if heart<=0:
     print("try next time!")
     game=False

  



if __name__=="__main__":
   
  heart=3
  word="hello" 
  game=True
  not_break_from_code1=True
  not_break_from_code2=True
  left_letters_to_win=""
  GUI_completed_word="_"

  old_letters=[]
  while(game==True):
      letter=input("give me the letter🦉: ")
      if letter.isdigit()==False and len(letter)==1:
    
        if letter not in old_letters:
            old_letters.append(letter)

            game_cycle(letter,word)
        else:
            print("same letter! you Cannot do that!")
            continue
  
      else:
        print("you can only insert: 1 letter strings!")
        continue
