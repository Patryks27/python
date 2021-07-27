def f_od_x(x):
    A=[1,0,-1,1];#x^3-x+1
    i = len(A)-1;
    wynik=0;
    x2=1;
    while i>=0:
        wynik= wynik + x2*A[i];
        x2= x2*x;
        i= i-1;
    return wynik;

def Stepien_Patryk_bisekcja(a,b,eps):
    x1= x1=(a+b)/2;
    while abs(a-b)>eps:
        x1=(a+b)/2;
        if(abs(f_od_x(x1)) <=eps):
            break;
        if(f_od_x(x1) * f_od_x(a) < 0):
            b=x1;
        else: 
            a=x1;
    print("Wynik: ",x1);
    return x1;
            


a=-2;
b=2;
Stepien_Patryk_bisekcja(a, b, 0.1);