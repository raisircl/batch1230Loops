#ENTER A NUMBER AND COUNT ITS DIGITS
num=int(input("Enter a number: ")) # 523
x=0 
temp=num
d=0
while num>0:  
    d=num%10
    x=x+d**3 
    num=num//10 
if temp==x:
    print(f"{temp} is a armstrong number")
else:
    print(f"{temp} is not a armstrong number")

#print(f"Total of digits in the number is: {x}") # X=># 3
# Q1. enter a number and print sum of its digits
# Q2. enter a number and print reverse of the number
# Q3. enter a number check whether it is palindrome or not
# Q4. enter a number and print is it arm strong or not
# 153 => 1**3 + 5**3 + 3**3 = 153
# Q5. enter a number and print it in word
# 523 => Five Two Three
