# Task Two
# Question1

x = 52

if x%3==0 and x%5==0:
    print ("Consultadd Python Training")

elif x%3==0:
    print("Consultadd")

elif x%5==0:
    print('c')

else:
    print('Sorry You got the wrong number!!')

# Question2

choice  = input("Pick any one of among 1, 2, 3, 4 or 5: ")
if choice in ('1','2','3','4','5'):
    first = float(input("Enter your first number: "))
    second = float(input("Enter your second number: "))

    if choice == '1':
        sum = first+second
        print(sum)
        if sum < 0:
            print('Zsa')

    if choice == '2':
        subtraction = first-second
        print(subtraction)
        if subtraction < 0:
            print('Zsa')

    if choice == '3':
        division = first/second
        print(division)
        if division < 0:
            print('Zsa')

    if choice == '4':
        multiplication = first*second
        print(multiplication)
        if multiplication < 0:
            print('Zsa')

    if choice == '5':
        first1 = float(input("Enter your first1 number: "))
        second2 = float(input("Enter your second2 number: "))
        print("The average of the four numbers = ", (first+second+first1+second2)/4)

else:
    print("Sorry Choose the right option please!!")


#Question3

age = 38
if age >= 11:
    print("You are eligible to see the Football Match")
    if age <= 20 or age >= 60:
        print("Ticket price is $12")
    else:
        print("Ticket price is $20")
else:
    print("You're not eligible to buy a ticket")

#Question4

while True:
    out = int(input('Enter the number: '))
    if out < 0:
        break
    else:
        print("Good Going")
print('Its Over')

#Question5

for i in range(2000, 3200):
    if (i%7==0) and (i%5!=0):
        print(i)

#Question6

x = 123
for i in x:
    print(i)
## OUTPUT TypeError: 'int' object is not iterable
i = 0
while i<5:
    i += 1
    if i == 3:
        break
else:
    print('error')
##OUTPUT is it will just run the while loop and break

##Question7

for x in range(6):
    if (x==3 or x==6):
        continue
    print(x,end=" ")
print("\n")

##Question8

countLetterAndNumber = (input("Enter Here: "))

Digit = 0
Letter = 0

for i in range(len(countLetterAndNumber)):
    if countLetterAndNumber[i].isalpha():
        Letter = Letter + 1
    if countLetterAndNumber[i].isdigit():
        Digit = Digit + 1

print("Letters", Letter)
print("Digits", Digit)

##Question 9

#part 1
num = int(input("Guess the lucky number "))
while num != 28:
    print("That is not the lucky number")

#part 2
num = -1
again = "yes"
while num !=28 and again != "no":
    number = int(input("Guess the lucky number: "))
    if number != num:
        print("That is not the lucky number")
        again = input("Would you like to guess again? ")

##Question 10

counter=1
while counter<=5:
    number = int(input("Guess the number: "))
    if number !=22:
        print("Try Again")
    else:
        print("Good Guess")
    counter = counter + 1
else:
    print("Game Over")

##Question11

counter=1
while counter<=5:
    number = int(input("Guess the number: "))
    if number !=22:
        print("Try Again")
    else:
        print("Good Guess")
        break
    counter = counter + 1
else:
    print("Sorry but that was not very successful")
