x = int(input("Enter no of values: "))
l=[]
for a in range(0,x):
    n= int(input())
    l.append(n)
print(l)
target = int(input("enter target: "))

left,right = 0,len(l)-1
while left < right:
    mid = (left+right)//2
    if l[mid]==target:
        print("found at index - ",mid)
        break
    elif l[mid]<<target:
        left = mid+1
        
    elif l[mid]>>target:
        right = mid-1
        
    else:
        print("value not found")
        break




    
    



