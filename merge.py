d1={'a':1,'b':2,'c':3}
d2={'c':5}
d3={}
for i in d1:
    d3[i]=d1[i]
for i in d2:
    if i in d3:
        d3[i]+=d2[i]
    else:
        d3[i]=d2[i]
print(d3)