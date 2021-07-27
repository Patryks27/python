def f_od_x(A,x):
    i = len(A)-1;
    wynik=0;
    x2=1;
    while i>=0:
        wynik= wynik + x2*A[i];
        x2= x2*x;
        i= i-1;
    return wynik;

def pochodna(A):
    B = [0] * len(A);
    i=len(A)-2;
    x=1;
    while i>=0:
        B[i] =A[i]*x;
        x=x+1;
        i=i-1;
    return B;

def Stepien_Patryk_metoda_stycznych(A,a,b,eps):
    x_k=a;
    x=b;
    A_prim= pochodna(A);
    while abs(x_k-x)>=eps:
        x_k= x;
        x= x_k - (f_od_x(A, x_k)/f_od_x(A_prim, x_k));
    print("Wynik: ",x);
    return x;

A=[1,0,-6];
a=1;
b=5;
Stepien_Patryk_metoda_stycznych(A, a, b, 0.01); #wynik dla tego przykładu to sqrt(6)
