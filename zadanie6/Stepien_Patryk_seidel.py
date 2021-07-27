import numpy as np
import math
import copy

def Stepien_Patryk_seidel(A,b,eps):
    A = np.array(A);
    L = np.array([[0] * len(A) for i in range(len(A))]);
    D =[[0] * len(A) for i in range(len(A))];
    U =np.array([[0] * len(A) for i in range(len(A))]);
    x=np.array([1]*len(A));
    boollen= False;
    
    for i in range(0,len(A)):
        D[i][i]= 1/A[i][i];
        for j in range(i+1,len(A)):
            U[i][j]=A[i][j];
        for j in range(0,i):
            L[i][j]=A[i][j];

    D=np.array(D);
    
    while boollen==False:
        D=(-1)*D;
        M=np.add(L,U);
        M =D.dot(M);
        M= M.dot(x);
        
        D=(-1)*D;
        C=D.dot(b);
        
        wynik= np.add(M,C);
        
        boollen= Czy_konczyc(x, wynik, eps);
        x=copy.deepcopy(wynik);
        
    print ("Wynik:",wynik);
    return A;



def Czy_konczyc(x1,x2,eps):
    for i in range(0,len(x1)):
        if(math.fabs(x2[i]-x1[i])>eps):
            return False;
    return True;



A=[[4,-1,-1,0],
   [-1,4,0,-1],
   [-1,0,4,-1],
   [0,-1,-1,4]]

b=[-1,2,0,1];
Stepien_Patryk_seidel(A, b, 0.01);