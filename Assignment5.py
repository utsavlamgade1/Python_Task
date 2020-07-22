#Question1 Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. Make sure to use only higher order function.
a = [i for i in range(1,100) if i%7==0 and i%3!=0]
print(a)

#Question2 Write a program in Python to  multiple the element of list by itself using a traditional function and pass the function to map to complete the operation.
def mulByIteself(num):
    return num*num
numbers = [1,2,3,4,5,6,7]
res = list(map(mulByIteself, numbers))
print(res)

#Question3 Write a program to Python find out the character in a string which is uppercase using list comprehension.
capslock = [i for i in ("IsThisaRealLifeOrIsThisAFantasy") if i == i.upper()]
print(capslock)

#Question4 Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should maps
#the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension.
Student =['Smith', 'Jaya', 'Rayyan']
Capital = ['CSE', 'Networking', 'Operating System']
dictionaryStudentCapital = {Student:Capital for Student, Capital in zip(Student,Capital)}
print(dictionaryStudentCapital)

#Question5 Learn More about Yield, next and Generators
Yeild is a keyword in Python that is used to return from a function without destroying the states of its local variable and when the function is callled,
the execution starts from the last yeild statement. Any function thta contains a yeild keyword is termed as Generators.

Next: Python file method next() is used when a file is used as an iterator, typically in a loop, the next() method is called repeatedly.
This method reurns the next input line, or raises Stopiteration when EOF is hit.
Combining next() method with other file methods like readline() does not work right. However, usingseek() to reposition the file to an absolute position will
flush the read-ahead buffer.

Generators are used to create iterators, but with a different approach. Generators are simple finctions which return an iterable set of items,
in a special way. When an iteration over a set of item starts using the for statement, the generator is run.

#Question6 Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”
def reverseStr(a):
    length = len(a)
    for i in range(length -1,-1,-1):
        yield a[i]
b=reverseStr('htrae')
print(b.__next__())
print(next(b))
print(next(b))
print(next(b))
print(next(b))


#Question 7 Write any example ob decorators
def addition(subtraction):
    res=1+2
    print("Addition: ", res)
    subtraction()
    res1=4-3
    print("Subtraction",res1)

@addition
def multiply():
    res2=2*2
    print("Multiply: ", res2)

#Question8 Learn about What is FRONT END and its Technologies and Tools
In programming and development, front-end is a term that describes someone who designs and develops the User Interface.
For example, a website front-end developer handels the visual aspects of how the webpage looks adn responds to the visitor.


The top 5 frontend Technologies are JS, Typescript, HTML, CSS, Flutter
JS: Yahoo, Typescript: Google, HTML: wikipedia, CSS: everyone, Flutter: Google
