import math
import numpy as np
import matplotlib.pyplot as plt

def f(x): #f(x) = (x-2)*(x+3)*(x-4)
    wynik = (x-2)*(x+3)*(x-4);
    return wynik;


def Stepien_Patryk_zloty_przedzial(a,b,c):
    p=(math.sqrt(5)-1)/2;
    k=b-a;
    j=0;
    while k>c:
        xl=b-p*(b-a);
        xr=a+p*(b-a);
        if(f(xl)>f(xr)):
            a=xl;
        else:
            if(f(xl)<f(xr)):
                b=xr;
        j=j+1;
        k=1;
        for i in range (j):
            k=k*(b-a);
            
    print("wynik",(a+b)/2);
    return (a+b)/2;


a=0;
b=6;

p=Stepien_Patryk_zloty_przedzial(a, b, 0.01);

x1 = np.linspace(a, b, 200);
y1 = f(x1); 
    
plt.plot(x1,y1,'-');
py=f(p);
plt.plot(p,py,'o');
