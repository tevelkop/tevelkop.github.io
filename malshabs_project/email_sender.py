import smtplib
import os
import csv
import file_creator 

def send_mail_to_each_person():
   
    with open("malshabs_project\database\people.csv") as info:    
        lst_info=csv.reader(info)
        for row in lst_info:
            list_of_closed_files=file_creator.return_list_of_files()
            prefix = f"message_for_{row[1]}.txt"

            password="ogqlmffqjbveidmz"
            username="tevelkop@gmail.com"
            smtplib.SMTP("smtp.gmail.com", port=587)
            connection=smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            
            opened_file=[open(prefix,"r",encoding="utf-8") for specific_file in list_of_closed_files if specific_file==prefix]
            executed_file=opened_file[0]
            content_of_file=executed_file.read()

            connection.login(username,password)
            connection.sendmail(from_addr=username,to_addrs="tevelkopler@gmail.com",msg=f"subject: Tsav gius\n\n .{content_of_file}")

            executed_file.close()
            connection.close()

