#min support = 3
arr = []*30 #dataset
items=[] # unique elements of dataset
x=0
count =[]   #count of elements of dataset [6, 7, 6, 2, 2]
count2=[] #count of c1 [4, 4, 4]
count3=[]
l1 =[] #list 1 ['A', 'B', 'C']
l2=[] # list 2 ['AB', 'AC', 'BC']
c1 =[]  # candidate set 1 ['AB', 'AC', 'BC']
c2=[]   # candidate set 2 ['ABC']
c=0
count_c1=0
count_c2=0
arr2=[] #set of possible 2 element itemsets from dataset
arr3=[] #set of possible 3 element itemsets from dataset

with open("/Users/PRANAV/Desktop/VI sem/dwdm lab/data.txt") as file:
    data = file.readlines()
    for l in data:
        word = l.split()
        x += 1
        #print(word)
        arr.append(word)

#print(arr)
#print(data)


for j in arr:
    for h in j:
        if h not in items:
            items.append(h)
items.sort()

print(items)

for j in items:
    for k in arr:
        for h in k:
            if h == j:
                c=c+1
    count.append(c)
    c = 0
print(count)

l = len(count)
for k in range(l):
    r = count[k]
    if r>=3:    #3 is min sup
        l1.append(items[k])
#print(l1)
l = len(l1)
k=0
for i in range(l):
    for j in range(i+1,l):
        c1.append(l1[i]+l1[j])
print(c1)



for i in arr:
    for j in range(len(i)):
        for k in range(j+1,len(i)):
            arr2.append(i[j]+i[k])
print (arr2)

for j in c1:
    for k in arr2:
        if j == k:
            count_c1=count_c1+1
    count2.append(count_c1)
    count_c1 = 0
print(count2)

for k in range(len(count2)):
    r = count2[k]
    if r>=3:
        l2.append(c1[k])
#print(l2)

l=len(l2)
for i in range(l):
    for j in range(i+1,l):
        a = [*l2[i]]
        b = [*l2[j]]
        if a[0] == b[0]:
            c2.append(a[0]+a[1]+b[1])
print(c2)
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
print(count3)

"""
fin=[]
for i in c2:
    fin.extend(i)
#print(fin)

fcount =[]
for j in fin:
    for k in arr:
        for h in k:
            if h == j:
                c=c+1
    fcount.append(c)
    c = 0
#print(fcount)

y=len(fin)
cf=[]
for i in range(y):
    for j in range(i+1,y):
        cf.append(fin[i]+fin[j])
#print(cf)

cf2=[]
for j in cf:
    for k in arr2:
        if j == k:
            c=c+1
    cf2.append(c)
    c = 0
#print(cf2)
"""