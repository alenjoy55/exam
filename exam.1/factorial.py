# def fact(f):
#     i=1
#     f=1
#     for i in range(i,f+1):
#         f*=i
#         print("factorial of number:",f)

# n=int(input("enter the no:"))
# fact(n)


def fact():
    a=int(input("enter a number"))
    fact=1
    for i in range(1,a+1):
        fact*=i
        print(fact)
fact()