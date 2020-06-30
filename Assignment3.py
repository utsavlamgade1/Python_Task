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
