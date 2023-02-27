a=10
b=20
print(a>b)
#logical operator
#and
#or
#not
c1=a>10
c2=b>10
r1=c1 and c2
r2=c1 or c2
r3=not c1
print(r1)
print(r2)
print(r3)
##if .....else
n=int(input())
r= n % 2
is_even = (r==0)
if is_even:
    print("n is even")
else:
    print("n is odd")