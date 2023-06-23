#global support = 3
#partitions =3
import numpy as np
min_sup=3
loc_sup=1
arr = []*30 #dataset
par1=[]
par2=[]
par3=[]
countf=0

items=[] # unique elements of dataset
x=0


with open("/Users/PRANAV/Desktop/VI sem/dwdm lab/data.txt") as file:
    data = file.readlines()
    for l in data:
        word = l.split()
        x += 1
        #print(word)
        arr.append(word)

#print(arr[0])
l=len(arr)
for i in range (0,l):
    if i<(l/3):
        par1.append(arr[i])
        continue
    elif ((l/3)<=i<(2*(l/3))):
        par2.append(arr[i])
        continue
    elif i>=(2*(l/3)):
        par3.append(arr[i])
        continue
#print(par1)
#print(par2)
#print(par3)
#print(data)



def apriori(arr):
    count =[]   #count of elements of dataset [6, 7, 6, 2, 2]
    count2=[] #count of c1 [4, 4, 4]
    count3=[]
    count4=[]
    l1 =[] #list 1 ['A', 'B', 'C']
    l2=[] # list 2 ['AB', 'AC', 'BC']
    l3=[]
    l4=[]
    c1 =[]  # candidate set 1 ['AB', 'AC', 'BC']
    c2=[]   # candidate set 2 ['ABC']
    c3=[]

    arr2=[] #set of possible 2 element itemsets from dataset
    arr3=[] #set of possible 3 element itemsets from dataset
    arr4=[] #set of possible 4 element itemsets from dataset
    c=0
    count_c1=0
    count_c2=0
    count_c3=0
    for j in arr:   #isolate elements and sort
        for h in j:
            if h not in items:
                items.append(h)
    items.sort()
    #print(items)

    for j in items: #find count of elements
        for k in arr:
            for h in k:
                if h == j:
                    c=c+1
        count.append(c)
        c = 0
    #print(count)

    l = len(count)

    for k in range(l):  #list of elements satisfying  min support
        r = count[k]
        if r>=loc_sup:
            l1.append(items[k])
    #print(l1)

    l = len(l1)
    k=0

    for i in range(l):  #creating candidate list 1
        for j in range(i+1,l):
            c1.append(l1[i]+l1[j])
    #print(c1)

    for i in arr:
        for j in range(len(i)):
            for k in range(j+1,len(i)):
                arr2.append(i[j]+i[k])
    #print (arr2)

    for j in c1:
        for k in arr2:
            if j == k:
                count_c1=count_c1+1
        count2.append(count_c1)
        count_c1 = 0
    #print(count2)

    for k in range(len(count2)):
        r = count2[k]
        if r>=loc_sup:
            l2.append(c1[k])
    #print(l2)

    l=len(l2)
    for i in range(l):
        for j in range(i+1,l):
            a = [*l2[i]]
            b = [*l2[j]]
            if a[0] == b[0]:
                c2.append(a[0]+a[1]+b[1])
    #print(c2)
    l=len(arr2)
    for i in arr:
        if len(i)>=3:
            for j in range(len(i)):
                for k in range(j+1,len(i)):
                    for t in range(k+1,len(i)):
                        arr3.append(i[j]+i[k]+i[t])
    #print(arr3)
    for j in c2:
        for k in arr3:
            if j == k:
                count_c2=count_c2+1
        count3.append(count_c2)
        count_c2 = 0
    #print(count3)
    for k in range(len(count3)):
        r = count3[k]
        if r>=loc_sup:
            l3.append(c2[k])
    #print(l3)
    l=len(l3)
    for i in range(l):
        for j in range(i+1,l):
            a = [*l3[i]]
            b = [*l3[j]]
            if a[0] == b[0] and a[1]==b[1]:
                c3.append(a[0]+a[1]+a[2]+b[2])
    #print(c3)
    l=len(arr3)
    for i in arr:
        if len(i)>=4:
            for j in range(len(i)):
                for k in range(j+1,len(i)):
                    for t in range(k+1,len(i)):
                        for p in range(t+1,len(i)):
                            arr4.append(i[j]+i[k]+i[t]+i[p])
    #print(arr4)
    for j in c3:
        for k in arr4:
            if j == k:
                count_c3=count_c3+1
        count4.append(count_c3)
        count_c3 = 0
    #print(count4)
    for k in range(len(count4)):
        r = count4[k]
        if r>=loc_sup:
            l4.append(c3[k])
    #print(l4)
    return l1,l2,l3,l4


b=[]
cg=[]
lg=[]
a = apriori(par1)
print("L for par1",a)
for i in a:
    b.extend(i)

c = apriori(par2)
print("L for par2",c)
for i in c:
    b.extend(i)

d = apriori(par3)
print("L for par3",d)
for i in d:
    b.extend(i)
#print(b)

for i in b:
    if i not in cg:
        cg.append(i)
print("Global candidate set =",cg)

for i in cg:
    for j in b:
        if i==j:
            countf=countf+1
    if countf>=min_sup:
        lg.append(i)
    countf=0
print("Global L=", lg)