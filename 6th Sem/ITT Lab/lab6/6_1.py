s = input("Enter string: ")
l = len(s)
f=0
for i in range (int(l/2)):
  if(s[i] != s[l-i-1]):
    print("Not Palindrome")
    f=1
    break
if(f==0):
  print("Palindrome")