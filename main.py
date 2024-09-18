# #Using conditional statements, check if the number is:
# #  - Even or Odd.
# #  - Positive, Negative, or Zero.
# #  - Whether it is divisible by both 2 and 3 or anyone of them or not divisible by both 
# #  check all the cases and print statement for each case.
num:int = int(input("enter the number"))
if(num%2 == 0):
    print("Number is even")
else:
    print("Number is odd")

if(num>=1):
    print("Number is positive")
elif(num<0):
    print("Number is negative")
else:
    print("Number is Zero")

if(num%2==0 and num%3 ==0):
    print("Number is divisible by 2 and 3")
elif(num%2==0):
    print("Number is divisible by 2")
elif(num%3 == 0):
    print("Number is divisible by 3")
else:
    print("not divisible by both 2 aND 3")


#Enter a month (as a number between 1 and 12). Print the n
# # - Take the user age.
# #   -- If the age is 18 or above:
# #   -- Ask if they have a nationality of "Pakistani".
# #     ---If yes, print "You are eligible to vote."
# #     ---If no, print "Please obtain a valid ID to vote."
age:int=int(input("Enter your age : "))
nationality:int=int(input("If you have Pakistani nationality enter 1 else enter 0 : "))
if(nationality ==1 and age>=18):
    print("You are eligible to vote")
elif(nationality ==0 or age<18 ):
    print("You are not eligible to vote")
else:
    print("Please obtain a valid ID to vote")

# # - Write a program that takes the age of a person as input and determines whether they are 
# # a child (0-12 years),
# #  teenager (13-19 years), adult (20-59 years),
# #  or senior citizen (60 years and above)
age:int=int(input("enter the age  "))
if(age >0 and age <=12):
    print ("child")
elif (age>=13 and age <=19):
    print("teenageer")
elif(age>=20 and age<=59):
    print("adult")
elif (age>=60):
    print("senior citizen")
else:
    print("invalid input")


#  -Enter a month(as a number between 1 and 12)print a  number of days in that month. Assume a non-leap year.
month:int=int(input("enter the month number : "))
match month:
    case 1:
        print ("january")
    case 2:
        print ("feburary")
    case 3 :
        print ("march") 
    case 4:
        print ("april")
    case 5:
        print ("may")
    case 6:
        print ("june")
    case 7:
        print ("july")
    case 8:
        print ("august")
    case 9:
       print ("september")
    case 10:
        print ("0ctober")
    case 11:
        print ("november")
    case 12:
        print ("december")
    case _:
        print ("invalid month")
    def days in month (month)
    days =(12,3,28,16,30,20,13,7,10)
    if 1<= month <=12
     return days(month-1)
     else :
        return "invalid month please enter anumber between 1 and 12"
        month =int(input"(enter a month as a number between 1 and 12)")
        print(f"number of days in month{month}")













