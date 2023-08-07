#-----------------------------------------------------------------------------------------
#Password Manager
#-----------------------------------------------------------------------------------------

from cryptography.fernet import Fernet

#-----------------------------------------------------------------------------------------
#KEY FUNCTIONS 

#use write key function on first run, afterwards put write_key() as a comment 
#in order to not make multiple key files 

def write_key():
    key = Fernet.generate_key() #generate key file
    with open("key.key", "wb") as key_file: #make file called key
        key_file.write(key) #write the key in the file

def load_key():
    file = open("key.key", "rb")  #opening the file
    key = file.read() #reading file
    file.close #closing the file 
    return key #returning the key

#-----------------------------------------------------------------------------------------
#MASTER PASSWORD CREATION AND ENCRYPTION 

master_pwd = input("What is the master password? ")
key = load_key() #convert master_pwd into bytes 
fer = Fernet(key) #using the byte converted master_pwd as the actual key

#-----------------------------------------------------------------------------------------
#PASSWORD FUNCTIONS 

def view():
    with open('passwords.txt', 'r') as f: #open a file for reading data
        for line in f.readlines(): #read each line
            data = (line.strip()) 
            user, passw = data.split("|") #split data using | as seperator 
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode()) #print user and password 

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f: #open file for appending data
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") #convert password into bytes, store it beside the name 

#-----------------------------------------------------------------------------------------
#USER INTERACTION 

while True:
    mode = input("Would you like to add a new password or view preexisting ones? (view, add, or q to quit) ")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
