import copy
import math

def Stepien_Patryk_jacobi(A,b,eps):
    x=[0]*len(A);
    wynik = [0]*len(A);
    boollen= False;
    
    if(Czy_wierszowo_dominujaca(A)==0):
        print("Macierz nie jest wierdszowo dominująca!");
        return wynik;
    
    while boollen==False:
        for i in range(0,len(A)):
            suma = b[i];
            for j in range(0,len(A)):
                if(j!=i):
                    suma= suma - (A[i][j]*x[j]);
            wynik[i]=(1/A[i][i])*suma;
        boollen = Czy_konczyc(wynik,x,eps);
        x=copy.deepcopy(wynik);

    print("Wynik:",wynik);
    return wynik;

def Czy_wierszowo_dominujaca(A):
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if(i!=j):
                if(math.fabs(A[i][i])<=math.fabs(A[i][j])):
                    return 0;
                
    return 1;

def Czy_konczyc(x1,x2,eps):
    for i in range(0,len(x1)):
        if(math.fabs(x2[i]-x1[i])>eps):
            return False;
    return True;


A=[[4,-1,-0.2,2],
   [-1,5,0,-2],
   [0.2,1,10,-1],
   [0,-2,-1,4]]

b=[30,0,-10,5];
Stepien_Patryk_jacobi(A, b, 0.5);

C=[[4,-1,-1,0],
   [-1,4,0,-1],
   [-1,0,4,-1],
   [0,-1,-1,4]]

d=[-1,2,0,1];
Stepien_Patryk_jacobi(C, d, 0.01);