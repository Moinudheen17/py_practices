#count vowels and consonants .
a = input("enter word :")
v = "aeiou"
i = 0
s = 0
for ch in a :
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'  :
        i = i + 1
    else :
        s = s + 1
print("wovels  : ",i)
print("consonants :",s)
