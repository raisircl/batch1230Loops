num=int(input("Enter a number: "))
x=0
while num>0:
    x=x+1
    num=num//10
print(f"Total digits in the number is: {x}")
