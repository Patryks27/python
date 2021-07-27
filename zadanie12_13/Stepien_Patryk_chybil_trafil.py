import math
import random 
import numpy as np


def Stepien_Patryk_chybil_trafil(a,b,n):
    wynik = (b-a)/n;
    max_y=funkcja(a);
    min_y=max_y;
    po = np.linspace(a,b,1000);
    for i in range(1000):           #szukamy min i max funckji
        fx = funkcja(po[i]);
        if(fx>max_y):
            max_y=fx;
        if(fx<min_y):
            min_y=fx;
        
        
    k=0;
    for i in range(n):      #algorytm chybił trafił Monte Carlo
        x = (random.random()*(b-a))+a;
        y = (random.random()*(max_y-min_y))+min_y;
        if(funkcja(x)>=0):
            if(funkcja(x)>=y and y>0):
                k=k+1;
        else:
            if(funkcja(x)<y and y<0):
                k=k-1;
                
    wynik = k/n * (b-a) *(max_y- min_y); #obliczamy wynik
    return wynik;
    


def funkcja(x):
    return math.sin(x);


a=0;
b=math.pi;
print( Stepien_Patryk_chybil_trafil(a,b,1000));  #wynik dla tego wywołania wynosi 2 












