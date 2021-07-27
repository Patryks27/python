
import math

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
    print ("Wynik:",L);
    return ;



A=[[4,2,2],
   [2,5,3],
   [2,3,6],
   ]
wynik =[[2,0,0],[1,2,0],[1,1,2]]
Stepien_Patryk_rozklad_cholesky(A);