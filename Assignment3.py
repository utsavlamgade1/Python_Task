##Question 1 Create a list of the 10 elements of four different types of Data Types like int, string, complex, and float.

differentDataType = [10, 20.30, 'New York', 40+5j, 50, 60.7, 'DC', 80, 90.1]

##Question 2 Create a list of size 5 and execute the slicing structure 
slicingList = [10, 20, 30, 40, 50]
print(slicingList[1:3])
print(slicingList[3:])
print(slicingList[:3])
print(slicingList[1:3:2])
print(slicingList[:])

##Question 3 Write a program to get the sum and multiply of all the items in a given list.
total = 0
total2 = 1
num = [1,2,3,4,5]
for n in range(len(num)):
    total=total+num[n]
    total2=total2*num[n]

print("The sum of total number is ",total)
print("The multiplication of total number is ", total2)


##Question 4 Find the largest and smallest number from a given list.
numberList=[1,2,3,4,5,6,7,8,9]
maxValue=max(numberList)
minValue=min(numberList)
print("The maximum value is ", maxValue)
print("The minimum value is ", minValue)

##Question 5 Create a new list that contains the specified numbers after removing the even numbers from a predefined list. 
numList=[1,2,3,4,5,6,7,8,9,10]
oddNum=[]
for n in range(len(numList)):
    if (n%2==0):
        pass
    else:
        oddNum.append(n)
print("The original list ", numList)
print("After removing the even number ",oddNum)

##Question 6 Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
li=[]
for i in range(1,31):
    li.append(i**2)
print(li[:5])
print(li[-5:])

##Question 7 Write a program to replace the last element in a list with another list.
# Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
# Expected output: [1,3,5,7,9,2,4,6,8]

num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]
num1[-1:] = num2
print(num1)

##Question 8 	Create a new dictionary by concatenating the following two dictionaries:
# a={1:10,2:20}
# b={3:30,4:40}
# Expected Result: {1:10,2:20,3:30,4:40}
Dic1={1:"Jack", 2:"Matt",3:"Tim"}
Dic2={4:"Mary", 5:"Jason",6:"Danny"}
result=Dic1.update(Dic2)
print(Dic1)

##Question 9 Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
# Sample data (n=5)
# Expected Output: {1:1,2:4,3:9,4:16,5:25}

dic1=dict()
for x in range(1,6):
    dic1[x]=x**2
print(dic1)

##Question 10 Write a program which accepts a sequence of comma-separated numbers from the console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# The output should be:
# [‘34’,’67’,’55’,’33’,’12’,’98’]
# (‘34’,’67’,’55’,’33’,’12’,’98’)

numbers = input("Enter few numbers and seperate it with comma(,): ")
list = numbers.split(",")
tuple = tuple(list)
print(list)
print(tuple)


