import numpy as np
import math
import copy
import matplotlib.pyplot as plt

def Stepien_Patryk_ukladU(L,b): #górna
    wynik = [0] * len(b);
    suma =0;
    lenA = len(L);
    i = len(L)-1;
    while i>=0:
        if L[i][i]==0:
            print("Nie można dzielić przez 0!")
            return 0;

        for j in range(i+1,lenA): 
            suma = suma + (L[i][j]*wynik[j])
        
        wynik[i]=(b[i] - suma)/L[i][i];
        suma =0;
        i = i - 1;
       
    return wynik;

def Stepien_Patryk_ukladL(L,b):
    wynik = [0] * len(b);
    suma =0;
    lenA = len(L);
    for i in range(0,lenA):
        if L[i][i]==0:
            print("Nie można dzielić przez 0!")
            return 0;
        for j in range(0,i):
            suma = suma + (L[i][j]*wynik[j]);
        wynik[i]=(b[i] - suma)/L[i][i];
        suma =0;

    return wynik;

def Stepien_Patryk_rozklad_cholesky(A):
    L = [[0] * len(A) for i in range(len(A))]
    for i in range (0,len(A)):
        for j in range (0,i+1):
            if(i==j):
                suma =0;
                for k in range (0,j):
                    suma = suma + (L[i][k]*L[i][k]);
                L[i][i]=math.sqrt(A[i][i] - suma);
            else:
                suma =0;
                for k in range (0,j):
                    suma = suma + (L[j][k]*L[i][k]);
                L[i][j] = (A[i][j] - suma) / L[j][j];
    return L;


def Stepien_Patryk_MNK(x,y,n):
    a = [1] * len(x);
    A = [[1] * len(x) for i in range(len(x))];
    At = [[1] * len(x) for i in range(len(x))];
    for i in range(0,len(x)):
        for j in range(1,len(x)):
            A[i][j] = x[i]* A[i][j-1];
            
    for i in range(0,len(x)):   #odwracamy macierz A
        for j in range(0,len(x)):
            At[i][j] =A[j][i];
            
    A = np.array(A);
    At = np.array(At);
    y=np.array(y);
    L = At.dot(A);
    p= At.dot(y);
    L= Stepien_Patryk_rozklad_cholesky(L);
    U=copy.deepcopy(L);
    
    for i in range(len(A)):
        for j in range(len(A)):
            U[i][j]=L[j][i];
    z = Stepien_Patryk_ukladL(L, p);
    wynik=Stepien_Patryk_ukladU(U, z);

    
    return wynik;
    
def obliczaj_warotci(fx,x):
    wynik = [0]*len(x);
    for i in range(len(x)):
        x2 =1;
        suma =0;
        for j in range(len(fx)):
            suma=suma+(x2 * fx[j]);
            x2=x2*x[i];
        wynik[i]= suma;
            

    return wynik;
    



x=[1,3,4];
y=[1,2,4];
MNK=Stepien_Patryk_MNK(x, y, 3);
print("Mnk:",MNK);
print(MNK[1]);
#wykres
plt.plot(x, y, 'o');
x2=[0]*1000;
i=0;
xmin=min(x);
przekoskok = (max(x)-min(x)) /1000;
while (i<len(x2)):
    x2[i]= xmin;
    xmin = xmin+ przekoskok;
    i=i+1;

y2=obliczaj_warotci(MNK,x2);

plt.plot(x2,y2);


