import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import scipy.interpolate as interpolate

def Stepien_Patryk_trapezy(a,b,n):
    n=n-1;

    h= (b-a)/n;
    wynik =0;
    for i in range(n-1):
        wynik= wynik+ f(a+(i+1)*h );
       # rect = mpatches.Rectangle((pros, 0), h, f(s), linewidth=1, edgecolor='r', facecolor='none')
       # plt.gca().add_patch(rect);
       
    for i in range(n):  #rysowanie trapezów
        x=[a+(i)*h,a+(i+1)*h];
        y=[f(a+(i)*h),f((i+1)*h)];
        new_x = np.linspace(x[0], x[1], 28);
        new_y = interpolate.interp1d(x, y, kind='slinear')(new_x)
        plt.plot(new_x, new_y, 'r-')
        
        x=[a+(i)*h,a+(i)*h];
        y=[f(a+(i)*h),0];
        plt.plot(x, y,'r-');
        
    x=[a+(n)*h,a+(n)*h];#ostatnia linia
    y=[f(a+(n)*h),0];
    plt.plot(x, y,'r-');
    
    x=[0,a+(n)*h];#linia pozioma x=0
    y=[0,0];
    plt.plot(x, y,'r-');
        
        
    wynik=wynik+((f(a)+f(b))/2);
    wynik=wynik*h;
    print(wynik);
    
    
    return wynik;



def f(x): #f(x)=x^2+x+2
    return x*x+x+2;




x1 = np.linspace(-11, 12, 200);
y1 = f(x1); 
    
plt.plot(x1,y1,'-');
Stepien_Patryk_trapezy(0, 10, 8)
plt.grid();


plt.show();








