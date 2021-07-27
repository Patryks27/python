import math
import random 
import numpy as np


def Stepien_Patryk_Pole_kola(r,n):  #obliczenia wykonujemy tylko dla cwiartki koła
    a=0;
    b=r;
    x = (random.random()*(b-a))+a;  #losowanie x i y od 0 do r
    y = (random.random()*(b-a))+a;
        
        
    k=0;
    for i in range(n):      #algorytm chybił trafił Monte Carlo
        x = (random.random()*(b-a))+a; # losujemy x i y z przedziału <0,r>
        y = (random.random()*(b-a))+a;
        if(funkcja(x,y)<=r):
            k=k+1;
        

    wynik = (k / n) * r * r * 4; #obliczamy wynik
    return wynik;
    


def funkcja(x,y):   #zwraca promień 
    return math.sqrt((x*x) + (y*y));


r=4;
print( Stepien_Patryk_Pole_kola(r,1000));  #pole dla tego koła wynosi 16*pi, około 50.2654...












