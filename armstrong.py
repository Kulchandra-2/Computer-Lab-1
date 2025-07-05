for num in range(100, 1000):
    a = str(num)
    s = int(a[0])**3 + int(a[1])**3 + int(a[2])**3
    if s == num:
        print(num)