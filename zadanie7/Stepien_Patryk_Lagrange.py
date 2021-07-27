def Stępień_Patryk_Lagrange(x,xw,yw,n):
    px=1
    suma =0;
    wynik = [0]*len(x);
    for k in range(len(x)):
        for i in range(n):
            gora =1;
            dol=1;
            for j in range (n):
                if(i!=j):
                    gora = gora * (x[k]-xw[j]);
                    dol = dol * (xw[i]-xw[j]);
            px=gora/dol;
            suma =suma + px*yw[i];
        wynik[k]=suma;
        suma =0;
    print("Wynik: ",wynik);
    return wynik;
    
    
x=[5,3];
xw=[2,3,10];
yw=[0,2,1];
Stępień_Patryk_Lagrange(x,xw,yw,3); #trójka oznacza funkcje kwadratową