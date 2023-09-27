def binary(arr,target):
    left , right = 0, len(arr)-1
    while left <=right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else: 
            right = mid-1
        
    return "Not in array"


    
arr = [10,20,30,40,50]
target = 100
x = binary(arr,target)
print(x)


    
