#initialize the outterloop counter
#nested loop : when we use a loop inside another loop
i=1
while i<=3: #outer loop
    #initialize the innerloop counter
    j=1
    while j<=i: # inner loop
        print("*",end=" ")
        j=j+1
    print() #new line after inner loop
    i=i+1

    