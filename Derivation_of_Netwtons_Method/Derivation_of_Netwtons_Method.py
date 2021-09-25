import math as m
def F(x):
    return 5*m.cos(x**2)-3*x

def F1(x):
    return -10*x*m.sin(x**2)-3

def F2(x):
    return -10*m.sin(x**2)-20*pow(x,2)*m.cos(pow(x,2))

a=0.8;
b=1.1;
E=1e-4;

x=a
if(F(x)*F2(x)<0):
    x=b

while(abs(F(x))>E):
    x=x-(F(x)/F2(x))

print("x= ", x)



