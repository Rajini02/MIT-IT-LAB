s=input("Enter string: ")
t = int(input("Enter key: "))

s_new=''
for i in s:
    p=ord(i)
    p+=t
    if(p>90):
        p-=26
    s_new+=chr(p)
print(s_new)