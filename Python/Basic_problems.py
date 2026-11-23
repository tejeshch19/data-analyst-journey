# problem1: number is vald or not 
# constrains:given number must be in b/w 200 to 900 number should not contain 5 as digit
number = input("enter a number: ")
if( int(number) >=200 and int(number)<=900):
    checking=(number[0]=="5"or number[1]=="5" or number[2]=="5")
    if(checking):
        print("not valid")
    else:
        print("Valid")
else:
    print("please enter number between 200 to 900")

# problem2:sum and product checking
# given a,b if both sum and product of given numbers are less than three digits

a=int(input("enter a number:"))
b=int(input("enter b number:"))
sum=a+b
product=a*b
if(sum<=0 and product<=0):
    print("given numbers are zero and negative")
elif(sum<=100 and product<=100):
    print("given numbers are less than two digits")
elif(sum <=999 and product<=999):
    print("given numbers less than three digits")
else:
    print("given numbers are greater than three digits")

# problem3:Triangles
# given a,b,c
# if a,b,c are equal -->equilateral
#any of two sides are equal -->isosceles
#a,b,c are not equal to each other -->scalene
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
eq=(a==b)and(b==c)and(c==a)
iso=(a==b)or(b==c)or(c==a)
sca=(a!=b)and(b!=c)and(c!=a)

if eq:
    print("equilateral")
elif iso:
    print("isosceles")
elif sca:
    print("scalene")

# problem4:sum of n squares
n = int(input("enter n: "))
result=0
for i in range(1,n+1):
    result +=i**2
print("sum of", n," squares is",result)

# problem5:striped rectangle
m=int(input("enter row: "))
n=int(input("enter col: "))
for i in range(1,m+1):
    if(i%2==0):
        print(n * "-")
    else:
        print(n*"+")