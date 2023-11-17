import csv
import os
list_of_files=[]


def create_all_letters():
    with open("malshabs_project\database\people.csv") as info:    
        lst_info=csv.reader(info)
        for row_for_name in lst_info:
            with open("tsav_gius.txt","r",encoding="utf-8") as message:
                content=message.read()
                content=content.replace("Private_Number",row_for_name[0])
                content=content.replace("his_name",row_for_name[1])
                content=content.replace("the_date!!",row_for_name[2])

                try:
                    letter= open(f"message_for_{row_for_name[1]}.txt",mode="x",encoding="utf-8")
                except FileExistsError:
                    os.remove(f"message_for_{row_for_name[1]}.txt")
                    letter= open(f"message_for_{row_for_name[1]}.txt",mode="x",encoding="utf-8")
                
                else:
                    letter.write(content)
                    list_of_files.append(f"message_for_{row_for_name[1]}.txt")
                finally: 
                    letter.close()
            
def return_list_of_files():
    global list_of_files
    return list_of_files