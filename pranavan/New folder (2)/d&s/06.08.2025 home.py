def prints(n):
    if(n<=0):
        return
    print("codingal")
    prints(n)
prints(50)


def arraysum(a):
    sum=0
    for i in a:
        sum=sum+i
    print(sum)

a=[19,13,6,9]
arraysum(a)