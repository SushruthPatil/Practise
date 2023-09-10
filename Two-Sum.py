x = int(input("Enter no of values: "))
l=[]
for a in range(0,x):
    n= int(input())
    l.append(n)
print(l)
y = int(input("enter target: "))
for i in range (len(l)):
    for j in range(len(l)):
        if i<j and l[i]+l[j] == y:
            print("Possible outcomes are:")
            print("array = ",i,j)
            break
        