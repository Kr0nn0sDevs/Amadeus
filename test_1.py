import re

def file():
    with open('contacts.txt','ab+') as f:
        read_file = f.readlines()
    return read_file

def add_contact(pb):
    with open('contacts.txt','a') as file:
        name = str(input("What's the name for contact: "))
        phone = str(input("What's the phone number for contact: "))
        file.write(name+" = "+phone+"\n")

def menu():
    print("1._Add a new contact\n2._search for a contact\n3._Display all contacts")    
    option = int(input("Type your option: \n"))
    return option

def search_contact(pb):
    temp = []
    check = -1
    query = str(input("Please enter the name of the contact you wish to search: "))
    for i in range(len(pb)):
        if query == pb[i][0]:
            check = i
            temp.append(pb[i])
            print(temp)

def display_contacts(pb):
    with open('contacts.txt','r') as f:
        filee = f.readlines()
        print(filee)

ch = 1
pb = file()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        pb == add_contact(pb)
    elif ch == 2:
        pb == search_contact(pb)
    elif ch == 3:
        pb == display_contacts(pb)