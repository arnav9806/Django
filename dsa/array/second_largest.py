arr=[12,2,16,54,78,9,63]
max = s_max = float('-inf')
for i in range(len(arr)):
    if arr[i]>max:
        s_max=max
        max=arr[i]
    if arr[i]>s_max and arr[i]!= max:
        s_max=arr[i]
print(s_max)

