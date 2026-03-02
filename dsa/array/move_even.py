arr=[1,2,8,16,33,45,55,8,6]
pos= 0
for i in range(len(arr)):
    if arr[i]%2==0:
        arr[i],arr[pos]=arr[pos],arr[i]
        pos+=1
print(arr)