
# Write a Python program to check if a number is positive.
a=int(input("enter a number: "))
if(a>0):
    print("number is postive")
else:
    print("number is negative")"
#2. Print "Eligible to vote" if age is 18 or above.
age=int(input("enter the age:"))
if(age>=18):
    print("elgible for vote")
else:
    print("not elgible for vote")
#3. Check if a number is divisible by 7.
a=int(input("enter a number :"))
if(a%7==0):
    print("no is divisible by 7")
else:
    print(" no is  not divisble by 7")
#4. Print "Pass" if marks are greater than 40
marks=float(input("enter marks :"))
if(marks>40):
    print("pass")
else:
    print("false")
#5. Check if a number is greater than 100.
a=float(input("enter a number:"))
if (a>100):
    print(" number is greater then 100")
else:
    print("number is less then 100")
#6. Display a message if temperature exceeds 45°C.
temp=float(input("enter the temperatuere:"))
if(temp>45):
    print("temperature is exceed from 45 degree")  
#7. Check if a string length is more than 8 characters.
name=(input("enetr string :"))
if(len(name)>8):
    print(" string ")
#8. Check if a number is a multiple of 10.
a=float(input("enter the number:"))
if(a%10==0):
    print("number is multiple of 10")
else:
    print("number is not multiple of 10")
#9 Print "Logged In" if password matches "admin123".
password=(input("enter password :"))
if(password=="admin123"):
    print("logged in")
else:
    print("not loggin")
1#0. Print a warning if balance is below minimum limit.
balance=float(input("enter amount:"))
if(balance>1000):
    print(balance)
else:
    print("balance is below the minimum limit")
#11.Check whether a number is even or odd
n=int(input("enter a number:"))
if(n%2==0):
    print("Number is even ")
else:
    print("number is odd ")
#12. Find the largest of two numbers.
a=float(input("enter a number:"))
b=float(input("enter a number:"))
if(a>b):
    print("a is gretest number")
else:
    print("b is greates number")
#13. Check whether a person is eligible for driving license.
age=float(input("enter your age :"))
if(age>=18):
    print(" person is eligible for driving license")
else:
    print("person is not elgible for driving license")
#14. Print Pass or Fail based on marks.
marks=float(input("enter your marks"))
if(marks>=45):
            print("pass")
else:
    print("fail")
#15. Check whether a number is positive or negative.
a=int(input("enter a number: "))
if(a>0):
    print("number is postive")
else:
    print("number is negative")
#16. Check whether a character is a vowel or consonant.
ab=(input("enter a character:"))
if(ab in("aeiouAEIOU")):
    print("vowels")
else:
    print("consonant")
#17. Check if a year is leap or not.
year=int(input("enter a year :"))
if(year%4==0):
    print("this is leap year")
else:
    print("this is not a leap year")
    #18. Print Valid Password or Invalid Password
p=(input("enter a password:"))
if(p=="div123"):
    print("valid password ")
else:
    print("invalid")
#19. Determine whether salary is taxable or not.
s=float(input("enter the salary:"))
if(s>=8000000):
    print(" salary is taxable")
else:
    Print("salary is not taxable")
#20. Check whether a number is greater than 50 or not.
n=float(input("enter a number:"))
if(n>50):
    print("number is greater then 50")
else:
    print("number is less then 50")
#21.Find the largest of three numbers
a=float(input("enter first number:"))
b=float(input("enter second number:"))
c=float(input("enter third number:"))
if(a>b and a>c):
    print("first number is greatest")
else:
    if(b>c):
        print("second no is greates")
    else:
        print("third no is greates")
#22. Check whether a number is positive, negative, or zero.
n=float(input("enter a number:"))
if(n==0):
        print("number is zero")
else:
    if(n>0):
        print("number is postive")

    else:
        print("number is negative")
"""23.Assign grades:
● A → marks ≥ 90
● B → marks ≥ 75
● C → marks ≥ 60
● Fail → below 60"""
marks=float(input("enter your marks:"))
if(marks>=90):
    print("grade A")
else:
    if(marks>=75 and marks<90):
        print("grade B")
    else:
        if(marks>=60 and marks<75):
            print("grade c")
        else:
            print("fail")
#24. Check whether a triangle is equilateral, isosceles, or scalene.
a=float(input("enter first side of triangle :"))
b=float(input("enter second side of triangle:"))
c=float(input("enter third side of triangle:"))
if(a==b==c):
    print(" it is an equlateral triangle:")
else:
    if(a==b or b==c or a==c):
        print("it is an isosceles triangle:")
    else:
            print("it is an scalene triangle:")         
#25. Validate login using username and password.
user=input("Enter your username :")
password=input("Enter your passoword:")
if(user=="abcd123" and password=="divy123"):
    print("welcome your are login:")
else:
    print(" please enter a valid username and password:")
#26. Check student result using marks of 3 subjects.
sub1=float(input("eneter the marks of subject:"))
sub2=float(input("eneter the marks of subject:"))
sub3=float(input("eneter the marks of subject:"))
total=(sub1+sub2+sub3)
per=total/3
if(sub1>=33 and sub2>=33 and sub3>=33):
    print("pass:",total,per)
else:
    print("fail:",total,per) 
27. Find the second largest number among three numbers.
a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
c=float(input("enter the third number:"))
number=[a,b,c]
number.sort()
print("first largest number is:",number[0])
print("second largest number is:",number[1])
print("third largest number is:",number[2])
#28. Check loan eligibility using age, salary, and credit score
name=input("enter name of cusutumer:")
age=float(input("enter the age of custumer:"))
salary=float(input("enter the salary of cusutmer:"))
creditscore=float(input("enter the credit score of custumer:"))
if(age>=21 and salary>=30000 and creditscore>=750):
    print(name,"you are eligible for loan:")
else:
    print(name,"you are not eligible for loan:")  
#29. Calculate electricity bill using slab-wise rates.
units=float(input("enter the total amount of unit:"))
bill = 0
if(units<=100):
    bill = units*5
else:
    if(units<=200):
        bill=(100*5)+((units-100)*7)
    else:
            bill=(100*5)+(100*7)+((units-200)*10)
            print("elecricity bill =",bill)   
#30. Check whether a character is uppercase, lowercase, digit, or special character.
ch = input("Enter a character: ")
if ch.isupper():
    print("Uppercase Letter")
else:
    if(ch.islower()):
        print("Lowercase Letter")
    else:
        if(ch.isdigit()):
            print("Digit")
        else:
            print("Special Character")

