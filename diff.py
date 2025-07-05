l1=[1,2,3,4,5]
l2=[2,3]
l3=[]
for i in l1:
    if i not in l2:
        l3.append(i)
print(l3)