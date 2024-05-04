
import string
import random

length=int(input("Enter the password length : "))
print('''Choose  Character set for the password from these :
    1.Digits
    2.Letters
    3.Special characters
    4.Exit''')

characterlist=" "

while(True):
    choice=int(input("Pick a number:"))
    if(choice==1):
        characterlist+=string.ascii_letters
    elif(choice==2):
        characterlist+=string.digits
    elif(choice==3):
        characterlist+=string.punctuation
    elif(choice==4):
        break
    else:
        print("please enter a valid choice:")

password=[]

for i in range(length):
    randomchar=random.choice(characterlist)
    password.append(randomchar)
print("The random password is "+" ".join (password))

    
        
           
           
