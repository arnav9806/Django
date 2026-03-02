arr = [1,5,7,12,48,52,68]
key = 522
left = 0
right = len(arr)-1

while(left<=right):
    mid= (left+right)//2
    if arr[mid] == key:
        print(mid)
        break
    elif arr[mid]< key:
        left= mid+1
    else:
        right= mid-1
        