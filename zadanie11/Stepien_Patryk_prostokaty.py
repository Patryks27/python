import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def Stepien_Patryk_prostokaty(a,b,n):
    n=n-1;
    h= (b-a)/n;
    wynik =0;
    s = a+(b-a)/(2*n);
    pros=a;
    for i in range(n):
        wynik= wynik+ (f(s)*h);
        rect = mpatches.Rectangle((pros, 0), h, f(s), linewidth=1, edgecolor='r', facecolor='none')
        plt.gca().add_patch(rect);
        s=s+h;
        pros= pros+h;
    print(wynik);
    
    
    return wynik;



def f(x): #f(x)=x^2+x+2
    return x*x+x+2;




x1 = np.linspace(-11, 15, 200);
y1 = f(x1); 
    
plt.plot(x1,y1,'-');
Stepien_Patryk_prostokaty(0, 10, 20)
plt.grid();
plt.show();








