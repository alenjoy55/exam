for i in range(1,5):
    a=64
    for j in range(i):
        print(chr(a+i),end=" ")
        a-=1
    print()