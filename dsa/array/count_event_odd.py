arr=[1,12,66,85,43,7,98,7]
even=0
odd=0
for i in range(len(arr)):
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)