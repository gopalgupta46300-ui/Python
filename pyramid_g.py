num=  4 #int(input("Enter a num:"))
for i in range(1,1+num):
    for _ in range(1,num-i+1):
       print(" ", end="")
    for j in range(1,2*i):
        print(j, end="")
    print( )