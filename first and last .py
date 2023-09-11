def first_and_last(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            first = i
            while i+1 < len(arr) and arr[i+1]==target:
                i+=1
            return [first,i]
    return [-1,-1]


#driver code
arr = []
l = int(input("enter total numbers: "))
for i in range(l):
    n=int(input())
    arr.append(n)
print(arr)    
target = int(input("Enter target:"))
print(first_and_last(arr,target))