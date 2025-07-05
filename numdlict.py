a='hello'
s=set(a)
d1={}
for i in s:
    d1[i]=a.count(i)
print(d1)