def linaer(arr, t):
    for i in range(len(arr)):
        if arr[i]==t:
            return i
        else:
            return -1

arr=[12,85,6,9,5,85,32]
t=85
print(linaer(arr, t))
