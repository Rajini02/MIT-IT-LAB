a=int(input("Enter number:"))
binary = 0
s=1
a1=a
while a1!=0:
    d=a1%2
    binary=s*d+binary
    a1=a1//2
    s=s*10
print (binary)


a2=a
octal = 0
s=1
while a2!=0:
    d=a2%8
    octal=s*d+octal
    a2=a2//8
    s=s*10
print (octal)


a3=a
hexa = ''
d=0
h=''
while a3!=0:
    d=a3%16
    match d:
        case 0 : h='0'
        case 1 : h='1'
        case 2 : h='2'
        case 3 : h='3'
        case 4 : h='4'
        case 5 : h='5'
        case 6 : h='6'
        case 7 : h='7'
        case 8 : h='8'
        case 9 : h='9'
        case 10 : h='A'
        case 11 : h='B'
        case 12 : h='C'
        case 13 : h='D'
        case 14 : h='E'
        case 15 : h='F'
    hexa=h+hexa
    a3=a3//16
print (hexa)