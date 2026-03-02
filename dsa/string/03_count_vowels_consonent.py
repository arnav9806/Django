s= "abcdefgh"
vowels= 0
consonent =0
for ch in s:
    if ch in "aeiou" or ch in "AEIOU":
        vowels+=1
    else:
        consonent+=1
print(vowels,"v")
print(consonent,"c")
