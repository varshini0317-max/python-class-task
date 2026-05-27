'''#1
def demo (*a):
    for i in  a:
        print(i*2)
demo(1,2,3,4)
#2
g=lambda a,b:a*b
print(g(1,2))

g1=lambda a,b:a+b
print(g1(1,2))
#3
def fun(**a):
    for i,j in a.items():
        print(i,j)
fun(name="varshini",age="17",city="salem")
#4
def sub(**p):
    for i,j in p.items():
        print(i,j)
sub(a=12,b=16,c=3,d=4)
#5
def sub(*p):
    for i in p:
        print(i)
sub(1,2,4,5)'''
a=90
def add():
    b=20
    print(a)

add()
def fac():
    fa=6
    for i in range(1,6):
        fa=fa*i
        print(fa)
fac()

