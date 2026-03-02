s= "aaabbcaaa"
left= 0
right =len(s)-1
while(left<=right):
    if s[left]!=s[right]:
        print("not a palindrome")
        break
    left+=1
    right-=1
else:
    print("palinrome")