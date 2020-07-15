#Question 1 Write a program to reverse a string. Sample data: “1234abcd” & Expected Output: “dcba4321”
a = "1234abcd"
b = a[::-1]
print(b)

#Question2 Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
def find_case(sen):
    a={"U":0,"L":0}
    for i in sen:
        if i in sen:
            if i.isupper():
                a["U"]+=1
            elif i.islower():
                a["L"]+=1
            else:
                pass
    print(sen)
    print("No. of Upper case characters : ",a["U"])
    print("No. of Lower case characters : ",a["L"])
find_case("Hey You, out there in the cold Getting lonely, getting old")

#Question3  Create a function that takes a list and returns a new list with unique elements of the first list.
def uniqueElement(element):
    a=[]
    for i in element:
        if i not in a:
            a.append(i)
    return a
print(uniqueElement([1,1,1,1,1,2,2,2,2,3,4,5,6,6,6,7,7,8,8,9,9,9,10,10,10]))

#Question4 Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
a=[]
listOfAlpha=input("Enter your Code: ")
for i in listOfAlpha:
    a.append(i)
a.sort()
print("-".join(a))

#Question5 Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

lines=input("What's your favorite Quote? ")
print(lines.upper())

#Question6 Define a function that can receive two integral numbers in string form and compute their sum and print it in console.

def sum(a, b):
    total = a+b
    print(total)

sum(22,33)

#Quesion7  Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
firstSent = input("Enter a sentence: ")
secondSent = input("Enter second sentence: ")
if (len(firstSent)>len(secondSent)):
    print(firstSent)
elif (len(firstSent)==len(secondSent)):
    print(firstSent)
    print(secondSent)
else:
    print(secondSent)

#Question8 Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.

def square():
    a=[]
    for i in range(1,21):
        a.append(i**2)
    print(tuple(a))
square()

#Question9 Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.

def showNumber(limit):
    for i in range(0,limit):
        if(i%2==0):
            print(i,"Even")
        else:
            print(i,"Odd")
showNumber(4)

#Question10 Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)
def evenNumber():
    for i in range(1,21):
        if(i%2==0):
            print(i)
        else:
            pass
evenNumber()

#Question11 Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
lis=[1,2,3,4,5,6,7,8,9,10]
even=list(map(lambda x: x**2, filter(lambda x:x%2==0,lis)))
print(even)

#Question12 Write a function to compute 5/0 and use try/except to catch the exceptions
try:
    a=int(input('Enter a number here: '))
    b=int(input('Enter a number here: '))
    x=a/b
    print(x)
except:
    print('Can\'t be divided by a zero')


#Question13 Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
#Goal : Turn [1,2,3,4,5,6,7] to 1234567
li=[[1,2,3],[4,5],6,7,8]
le=[]
def number(li):
    for i in li:
        if type(i)==list:
            number(i)
        else:
            le.append(i)
print(li)
number(li)
print(le)

#Question14 
