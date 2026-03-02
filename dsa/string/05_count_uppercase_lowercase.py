s= "ArnSJ"
upper= 0
lower = 0
for ch in s:
    if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        upper +=1
    else:
        lower+=1

print(lower,"l")
print(upper,"u")
