#Question 1
a,b,c = 1,2.23,"Catherine"

print(a)
print(b)
print(c)

#Question 2
a= (33+33j)
b=12345

a,b = b,a

print(a)
print(b)

#Question 3
#Part 1 Swap two numbers using the third variable as the result
a, b = 10, 20

print(a)
print(b)

result = a
a = b
b = result

print(a)
print(b)

#Part 2 Swap two numbers withour using the third variable as the result
a, b = 10, 20

a,b = b,a

print(a)
print(b)

#Question 4
#Python 2.x
y = raw_input("Give a value: ")
print y

#Python 3.x
x = input("Give a Value: ")
print(x)

#Question 5
#task1
x = int(input("Enter a number between 1 through 10: "))
y = int(input("Enter a number between 1 through 10: "))
z = x+y
print(z)

#task2
result = (z+30)
print(result)

#Question 6
entered_value = (input("Enter anything here: "))
print (type(entered_value))

#Question 7
# If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again.
# Will it change the value. If Yes then Why?
'''Yes, it will change the value because we can change the value of variable how many times we what to change it doesn't
matter if the given value is sting or integer or float. The last given value would be the answer
for example
x = 'Tower'
x = 234
if we print x the answer will be 234'''
