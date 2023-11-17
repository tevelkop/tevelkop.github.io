import email_sender
import file_creator
import os
import time

def delete_letters():

    directory = '/Users/user/Desktop/python projects/tic-tac-toe.py/computer_network/work'
    prefix = "message_"
    all_files = os.listdir(directory)
    lst_of_files = [file for file in all_files if file.startswith(prefix)]
    for file in lst_of_files:
        os.remove(file)

if __name__=="__main__":
    file_creator.create_all_letters()
    time.sleep(2)
    email_sender.send_mail_to_each_person()
    time.sleep(3)
    delete_letters()