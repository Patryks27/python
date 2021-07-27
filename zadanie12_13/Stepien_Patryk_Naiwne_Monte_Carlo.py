import math
import random 


def Stepien_Patryk_Naiwne_Monet_Carlo(a,b,n):
    wynik = (b-a)/n;
    suma =0;
    for i in range(n):
        losowa = (random.random()*(b-a))+a;
        suma= suma + funkcja(losowa);
    wynik = wynik * suma;
    return wynik;


def funkcja(x):
    return math.sin(x);



a=0;
b=math.pi;
print( Stepien_Patryk_Naiwne_Monet_Carlo(a,b,1000));  #wynik dla tego wywołania wynosi 2 











