arr = [1,2,0,9,5,7,5,0,0]
pos= len(arr)-1
for i in range(len(arr)-1, -1,-1):
    if arr[i]!=0:
        arr[i],arr[pos]=arr[pos],arr[i]
        pos-=1
print(arr)