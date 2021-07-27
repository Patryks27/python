import math


def Stepien_Patryk_Jacobi(A,eps):
    n = len(A);
    
    while(True):
        maksimum = 0;
        for i in range(n):
            for k in range(n):
                if i > k:
                    if maksimum <= math.fabs(A[i][k]):
                        maksimum = math.fabs(A[i][k])
                        p = i;
                        q = k;
        if maksimum < eps:
             break;
        
        
        if(A[p][p] != A[q][q]):
            tmp = 2*A[p][q] / ( A[p][p] - A[q][q] );
            theta = math.atan(tmp) / 2;
        
        
        else:
            theta = math.pi / 4;
        
        T = Macierz_Jednostkowa(n);
        
        T[p][p] = math.cos(theta);
        T[p][q] = -math.sin(theta);
        T[q][p] = math.sin(theta);
        T[q][q] = math.cos(theta);
        
        T_odwrotna = Macierz_Jednostkowa(n);
        
        T_odwrotna [p][p] = math.cos(theta);
        T_odwrotna [p][q] = math.sin(theta);
        T_odwrotna [q][p] = -math.sin(theta);
        T_odwrotna [q][q] = math.cos(theta);
    
        P = Macierz_mnozenie(T_odwrotna,A);
        A = Macierz_mnozenie(P, T);

    return A;


def Macierz_mnozenie(A,B):

    wynik=[[0]*len(B[0]) for i in range (len(A))];
    
    for i in range (len(A)):
        
        for j in range (len(B[0])):
            
            for k in range (len(A[0])):
                wynik[i][j]+=A[i][k]*B[k][j];
                
    return wynik;

def Macierz_Jednostkowa(n):
    wynik = [[0]*n for i in range(n)];

    for i in range (n):
        wynik[i][i] = 1;

    return wynik;

    
    


A =[[4,1,0],
    [1,5,2],
    [0,2,1]]

eps = 0.0000001;


wynik = Stepien_Patryk_Jacobi(A,eps)
print(wynik)


