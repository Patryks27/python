def f_od_x(x):#x^3-x+1
    A=[1,0,-1,1];
    i = len(A)-1;
    wynik=0;
    x2=1;
    while i>=0:
        wynik= wynik + x2*A[i];
        x2= x2*x;
        i= i-1;
    return wynik;


def Stepien_Patryk_sieczne(a,b,exp):
    x0=a;
    x1=a;
    x=b;
    while abs(x-x1)>=exp:
        x1=x;
        x=x1 -( ( (x1 - x0)/(f_od_x(x1)-f_od_x(x0)) ) * f_od_x(x1) );
        x0=x1;

    print("Wynik:",x);
    return x;
        
                    
    
        

a=-2;
b=2;
Stepien_Patryk_sieczne(a, b, 0.01);