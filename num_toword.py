num=int(input("Enter a number: ")) 
d=0
x=0
while num>0:
    x=x*10+num%10
    num=num//10
while x>0:
    d=x%10
    if d==0:
        print("Zero",end=" ")
    elif d==1:
        print("One",end=" ")
    elif d==2:
        print("Two",end=" ")
    elif d==3:
        print("Three",end=" ")
    elif d==4:
        print("Four",end=" ")
    elif d==5:
        print("Five",end=" ")
    elif d==6:
        print("Six",end=" ")
    elif d==7:
        print("Seven",end=" ")
    elif d==8:
        print("Eight",end=" ")
    elif d==9:
        print("Nine",end=" ")
    x=x//10
