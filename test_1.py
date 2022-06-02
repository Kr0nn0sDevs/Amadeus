import os
import sys
import openpyxl #pip install openpyxl

contacts = openpyxl.load_workbook('Contacts.xlsx')
contact = contacts.read()

sheet = contacts.active
for i in range(len(contact)):
    a1 = sheet['A'+1]
    b1 = sheet['B'+1]
    
    print(a1)

print(a1.value)
print(b1.value)

for i in range(a1 + 1, b1 +1):

    print(a1.value)
    print(b1.value)



"""with open('contacts.txt', 'r+') as contacts:
    contact = contacts.read()
    query = str(input("Please enter the name of the contact you wish to search: "))
    temp = []
    check = -1
    for i in range(len(contact)):
        if query == contact[i][0]:
            check = i
            temp.append(contact[i])"""