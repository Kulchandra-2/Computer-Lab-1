s = int(input("Enter a number: "))
if s > 1:
    p = True
    for i in range(2, s):
        if s % i == 0:
            p = False
            break
    if p:
        print("Prime")
    else:
        print("Not Prime")
else:
    print("Try Again!!! Wrong Value")