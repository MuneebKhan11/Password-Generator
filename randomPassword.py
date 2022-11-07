import random

lowercase="abcdefghijklmnopqrstuvwxyz"
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
symbols="!£$%&/<>@()*+-"
string = lowercase + uppercase + numbers + symbols
length=10
password="".join(random.sample(string,length))




1

while True:
    inp=input("Enter 1 to create a new password\nPress 2 to add a specific character into password\nPress 3 to delete a specific character \nPress 4 to change the lenght of the password\nPress 5 to Exit")
    
    if inp=="1":
        print("Your new password is: ",password)
    elif inp=="2":
        char_add = input("Please enter the character you want to add : ")
        new_pass="".join(random.sample(char_add,string,length))
    elif inp=="3":
        char_remove = input("Please enter the character you want to remove :")
        new_pass1= "".join(random.sample(string.replace(char_remove,""),length))
    elif inp=="4":
        change_len=input("Please enter the length of your new password : ")
        length==change_len
        print("Your new password is: ",password)
        
    elif inp=="5":
        print("Exiting...")
        exit()
    
    else:
        print("Invalid!")
                
        
