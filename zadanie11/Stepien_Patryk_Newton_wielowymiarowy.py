import numpy as np
import math
import matplotlib.pyplot as plt
#y=1/x ; x^2 + y^2 =9
def f_od_x(x): # X^2 -1/X^2 - 16=0
    wynik=( ((x*x*x*x) + 1 - (9*x*x))/(x*x)) ;
    return wynik;

def f1(x): #y=1/x;
    wynik=0;
    wynik=1/x;
    return wynik;  
  



def Stepien_Patryk_Newton_wielowymiarowy(a,b,eps):
    x1= x1=(a+b)/2;
    while abs(a-b)>eps:
        x1=(a+b)/2;
        if(abs(f_od_x(x1)) <=eps):
            break;
        if(f_od_x(x1) * f_od_x(a) < 0):
            b=x1;
        else: 
            a=x1;
    print("X=",x1);
    return x1;
            




#rysowanie
#plt.plot(x, y, 'o');

xfn=np.setdiff1d(np.linspace(-8,0,200),[0])
xfp=np.setdiff1d(np.linspace(0,8,800),[0])
yfn=f1(xfn)
yfp=f1(xfp)

yf = plt.plot(xfn, yfn)
plt.plot(xfp, yfp, color=yf[0].get_color());


r = 3; 
t = np.linspace(0,2*math.pi,200);

x1 = np.linspace(0, 2, 200);
y1 = np.linspace(0, 2, 200);
for i in range (len(t)):
    x1[i] = r*math.cos(t[i]);
    y1[i] = r*math.sin(t[i]);
    
plt.plot(x1,y1,'-');

#x2= np.linspace(-2,2,400);
#y2= np.linspace(-2,2,400);
#for i in range (len(x2)):
#    y2[i] = f2(x2[i]);
#plt.plot(x2,y2);


plt.axis([-8, 8, -8, 8])

a=-4;
b=-2;
px1=Stepien_Patryk_Newton_wielowymiarowy(a, b, 0.01);
py1=f1(px1);
plt.plot(px1,py1,'o');

a=-2;
b=0.1;
px1=Stepien_Patryk_Newton_wielowymiarowy(a, b, 0.01);
py1=f1(px1);
plt.plot(px1,py1,'o');

a=0.1;
b=2;
px1=Stepien_Patryk_Newton_wielowymiarowy(a, b, 0.01);
py1=f1(px1);
plt.plot(px1,py1,'o');

a=2;
b=4;
px1=Stepien_Patryk_Newton_wielowymiarowy(a, b, 0.01);
py1=f1(px1);
plt.plot(px1,py1,'o');



