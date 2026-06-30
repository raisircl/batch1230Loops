num=int(input("Enter a number:")) #5
i=2
while i<num:
    if num%i==0:
        break
    i+=1
if num==i:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")