#TASK SIX: FILE HANDLING AND EXCEPTION HANDLING


#Question1 Write a program in Python to allow the error of syntax to go in exception.
while True:
    try:
        print(hello world))
        break
    except SyntaxError:
        print("There is a syntax error on your code. Can you check it again Please")



#question2 Write a program in Python to allow user to open a file by using argv module.
#If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.
from sys import argv
programName, fileName=argv
while True:
    try:
        a=open(fileName)
        b=a.read()
        print(b)
        a.close()
        break
    except:
        print("This file do not exits")
        again=input("Do you want to try again? Y/N: ")
        if again == 'Y' or 'y':
            fileName=input("Enter the file name: ")
        else:
            break

#Question3  Write a program to handle an error
#if the user entered the number more than four digits it should return “Please length is too short/long !!!
#Please provide only four digits”

code="2020"
while True:
    x=input("Please enter you 4 digit code: ")
    if(len(x)>=5):
        print("Your entry is too long")
    elif(len(x)<4):
        print("Your entry is too short")
    elif(x==code):
        print("Welcome to your account")
        break
    else:
        print("Sorry wrong Code")

#Question4 Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type Password and if the password is incorrect give chance to enter
#it again but it should not be more than 3 times.
count=0
while count < 3:
    username = input('Enter Username: ')
    password = input('Enter Password: ')
    if password=="pythonPassword" and username=="python@gmail.com":
        print("Welcome to your account")
        break
    else:
        print("Either the Username or Password you've entered is Wrong. Please Try Again.")
        count += 1

    #Question 6 Read any file using Python File handling concept and return only the even length string from the doc.txt file.
# Hello I am a file
# Where you need to return the data string
# Which is of even length
# Make sure you return the content in
# The same link as it is present.

with open("doc.txt", 'r')as f:
    data=f.readline()
    for line in f:
        line=line.split(" ")
        if (len(line)%2==0):
            print(" ".join(line))
        else:
            pass
