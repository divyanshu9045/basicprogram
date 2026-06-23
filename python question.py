
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
            #31. Print day name using day number (1–7).
n=int(input("enter the no of day:"))
if(n==1):
    print("MONDAY:")
elif(n==2):
        print("TUESDAY:")
elif(n==3):
            print("WEDNESDAY")
elif(n==4):
                print("THURSDAY:")
elif(n==5):
                print("FRIDAY:")
elif(n==6):
                print("SATURDAY:")
elif(n==7):
                print("SUNDAY:")
else:
    print("invalid input:")
#32. Print month name using month number.
n=int(input("ENTER THE NUMBER OF MONTH:"))
if(n==1):
    print("JANUARY:")
elif(n==2):
    print("FEBRUARY:")
elif(n==3):
    print("MARCH:")
elif(n==4):
    print("APRIL:")
elif(n==5):
    print("MAY:")
elif(n==6):
    print("JUNE:")
elif(n==7):
    print("JULY:")
elif(n==8):
    print("AUGUST:")
elif(n==9):
    print("SEPTEMBER:")
elif(n==10):
    print("OCTOBER:")
elif(n==11):
    print("NOVEMBER:")
elif(n==12):
    print("DECEMBER:")
else:
    print("INVALID MONTH NUMBER:")
    
#33. Display grade based on percentage.
per=float(input("ENTER THE PERCENTAGE :"))
if(per>=90):
    print("GRADE A (PASS):")
elif(per<90 and per>=80):
    print("GRADE B (PASS):")
elif(per<80 and per>=70):
    print("GRADE C (PASS):")
elif(per<70 and per>=60):
    print("GRADE D (PASS):")
elif(per<60 and per>=33):
    print("GRADE E (PASS):")
elif(per<33):
    print("GRADE F(FAIL)")
else:
    print("INVALID INPUT /PLEASE CHECK INPUT")
#34. Display bonus percentage based on experience years.
n=float(input("ENTER THE NO EXPERIENCE YEAR:"))
if(n>=20 ):
        print("BONUS PERCENTAGE IS 60 :")
elif(n>=15 and n< 20):
    print("BONUS PERCENTAGE IS 50 :")
elif(n>=10 and n<15):
        print("BONUS PERCENTAGE IS 40 :")
elif(n>=5 and n< 10):
        print("BONUS PERCENTAGE IS 30 :")
elif(n>=1 and n<5):
        print("BONUS PERCENTAGE IS 20 :")
elif(n<1):
        print("BONUS PERCENTAGE IS ZERO :")
else:
    print("PLEASE CHECK YOUR INPUT:")
    
#35. Identify traffic signal meaning.
n=input("ENTER  THE COLOR OF  TRAFFIC LIGHT:")
if(n in "redRED"):
    print("STOP :")
elif(n in "yellowYELLOW"):
    print("READY :")
elif(n in "GREENgreen"):
    print("GO:")
else:
    print("INVALID COLOUR OF LIGHT OR DAMAGE OR BROKEN LIGHT:")
#36. Categorize temperature as Cold / Warm / Hot.
n=float(input("Enter the degre of tempertature:"))
if(n>=40):
    print(" HOT:")
elif(n<40 and n>=10):
    print("WARM:")
elif(n<10):
    print("COLD:")
else:
    ("invalid input:")
#37. Categorize employee based on salary range.
n=float(input("ENTER THE  SALARY OF EMPLOYEE:"))
if(n>=3000000):
    print(" IT IS A + CLASS EMPLOYEE:")
elif(n<3000000 and n>=2500000):
    print(" IT IS A  CLASS EMPLOYEE:")
elif(n<2500000 and n>=2000000):
    print("IT IS B+ CLASS EMPLOYEE:")
elif(n<200000 and n>= 1500000):
    print("IT IS C CLASS EMPLOYEE:")
elif(n<1500000 and n<1000000):
        print("IT IS D CLASS EMPLOYEE:")
else:
        print("IT IS E CLASS EMPLOYEE:")
#38. Print discount percentage based on purchase amount.
n=float(input("Enter the amount of purchase:"))
if(n>= 25000):
    print(" Discount percentage is 30%:")
elif(n<25000 and n>=20000):
    print("discoun percentage is 20%:")
elif(n<20000 and n>=10000):
    print("discounted percentage is 10%:")
elif(n<10000 and n>=5000):
        print("discounted percentage is 5%:")
elif(n<5000 ):
        print("discounted percentage is (zero)0%:")

#39. Identify number type: single-digit / double-digit / multi-digit.
num =abs(int(input("Enter a number: ")))
if num <= 9:
    print("Single-digit number")
elif num <= 99:
    print("Double-digit number")
else:
    print("Multi-digit number")

#40. Assign performance rating: Poor / Average / Good / Excellent.
n=float(input("enter the rating  between (1 to 5):"))
if(n==5):
    print("Excellent:")
elif(n<5 and n>=4):
    print("Good:")
elif(n<4 and n>=2.5):
    print("Average:")
elif(n<2.5):
    print("Poor:")
else:
    print("invalid input:")
#41. Check whether a number is divisible by 5 and 11.
n=float(input("Enter a Number :"))
if(n%5==0 and n%11==0):
    print("number is divisible by 5 and 11:")
else:
    print("number is not divisible by 5 and 11:")
#42. Check if a person is eligible for loan:
● age ≥ 21
● salary ≥ 25,000
● credit score ≥ 700

age=int(input("Enter the age of custumer:"))
salary=float(input("enter the amount of salary of custumer:"))
creditscore=float(input("enter the credit score :"))
if(age>= 21 and salary>=25000 and creditscore>=700):
    print("you are eligible for loan :")
else:
    print("you are not eligible for loan:")

#43. Validate login using username AND password.
user=input("Enter the username :")
pas=input("enetr the password :")
if(user=="divyanshu" and pas=="xd1234"):
    print("welcome you are a valid user:")
else:
        print("you are not valid user / please check username and password:")
     
#44. Check student pass condition:
 #● All subjects ≥ 40
# ● Average ≥ 50
sub1=float(input("enetr the marks of subject:"))
sub2=float(input("enetr the marks of subject:"))
sub3=float(input("enetr the marks of subject:"))
sub4=float(input("enetr the marks of subject:"))
sub5=float(input("enetr the marks of subject:"))
total=(sub1+sub2+sub3+sub4+sub5)
avg=total/5
if(sub1>=40 and sub2>=40 and sub3>=40 and sub4>=40 and sub5>=40 and avg>=50):
    print("pass:",avg)
else:
    print("fail:")
#45. Check if a number lies between 10 and 100.
n=int(input("enetr a number :"))
if(10 < n < 100):
    print("yees it is lies :")
else:
    print("no it is not lies :")
#46. Check exam eligibility:
● attendance ≥ 75% OR
● medical certificate available
n=float(input("enter the attendance:"))
m=input("enetr yes or no if medical certificate:")
if(n>=75):
    print("you are eligible for exam:")
elif(m in "yesYES"):
    print("you are eligible foe exam:")
else:
        print("you are  not eligible foe exam:")
#47. Determine insurance eligibility using age, health status, and income.
age=int(input("enetr the age :"))
income=float(input("eneter salary:"))
health=input("enetr yes or no if any issueor disease:")
if((age>=18 and age<60) and income>=18000 and health in"NOno"):
    print("you are eligible for health insurance:")
else:
    print("you are  not eligible for health insurance:")





