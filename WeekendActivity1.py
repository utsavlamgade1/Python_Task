##Question 1 Create a list of the 10 elements of four different types of Data Types like int, string, complex, and float.

differentDataType = [10, 20.30, 'New York', 40+5j, 50, 60.7, 'DC', 80, 90.1]

##Question 2 Create a list of size 5 and execute the slicing structure 
slicingList = [10, 20, 30, 40, 50]
print(slicingList[1:3])
print(slicingList[3:])
print(slicingList[:3])
print(slicingList[1:3:2])
print(slicingList[:])

##Question 3  Create a list of given structure and run 
            # x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
#Access list [1, 2, 3, 4] 
print(x[5][:4])
#Access list [600,  700]
print(x[6:8])
#Access list [100, 300, 500, 600, 800]
print(x[::2])
#Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
y=[]
y=[x[::-1]]
print(y)
#Access list [10]
print([x[5][5][0]])
#Access list [ ]
y=[ ]
print(y)

##Question4 Create a list of thousand numbers using range and xrange and see the difference between each other.
r= list(range(50,101))
print r
s = xrange(50, 101)
t = list(s)
print t 


##Question5 How Tuple is beneficial as compared to the list?
Tuple is not mutable whereas a list is mutable data structure and a list has a variable size while a tuple has a fixed size.

##@uestion6 Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and a multiple of 2.
question6 = list(range(1, 1101))
for i in question6:
   if((i%3==0) and (i%2==0)):
      print(i)

##Question7 Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the string with their index.
question7 = "What a wonderful world"
revQuestion7 = question7[::-1]
print(revQuestion7)
for letter in question7:
    if letter in 'aeiou':
        print(letter)

##Question8 Write a program in Python to iterate through the string “hello my name is Abcde” and print the string which has even length of the word.
def printWords(s): 

    s = s.split(' ')  

    for word in s:  

        if len(word)%2==0: 
            print(word)  
  
s = "hello my name is Abcde" 
printWords(s)

##Question9 Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.
#x=[1,2,3,4,5,6,7,8,9,-1]
numbers = [1,2,3,4,5,6,7,8,9,-1]
numberSet = set(numbers)
target = int(input("Enter the number: "))
for x in numbers:
    if target-x in numberSet:
        print("the pair of numbers are: {0} and {1}".format(x, target-x))

##Question10 Write a program in Python to complete the following task:
#Create two different lists as in even_list and odd_list
num = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []
for n in num:
    if (n%2==0):
        even.append(n)
    else:
        odd.append(n)
print("Even list: ", even)
print("Odd list: ", odd)

#Ask the user to enter the number in the range of 1,50 and make sure if the entered number is even appended it to the even_list and if the entered number is odd append it to the odd list
num=int(input("Enter a number between 1 to 150: "))
if(num%2==0):
    print("Even")
else:
    print("Odd")

#Keep that in mind you can only add 5 items in each list
a=[]
for i in range(1,6):
    items=int(input("Enter numbers here: "))
    a.append(items)
print("Added items are: ",a)

#Make sure once you entered the total 5 elements calculate the sum of the list and return the maximum out of the list.
b=[]
for i in range(1,6):
    num=int(input('Enter a number here: '))
    b.append(num)
    c=sum(b)
print("Your list of numbers are: ", b)
print("The sum of the numbers is ",c)

##Question11 Write a program to find out the occurrence of a specific word from an alphanumeric statement. Example: 12abcbacbaba344ab  Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic
li = '12abcbacbaba344ab'
a={}

for i in li:
    if(i.isalpha())==True:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
print(a)

##Question12 Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
num = (1,2,3,4,5,6,7,8,9,10)
even = []
for i in num:
    if (i%2==0):
        even.append(i)
print("Normal Tuple: ",num)
s=tuple(even)
print("Even tuple: ",s)

