def Stepien_Patryk_ukladU(L,b):
    wynik = b[:];
    suma =0;
    lenA = len(L);
    i = len(L)-1;
    while i>=0:
        if L[i][i]==0:
            print("Nie można dzielić przez 0!");
            return 0;

        for j in range(i+1,lenA): 
            suma = suma + (L[i][j]*wynik[j])
        
        wynik[i]=(b[i] - suma)/L[i][i];
        suma =0;
        i = i - 1;
       
    print("Wynik:",wynik);
    return wynik

def Stepien_Patryk_Gauss(A,b):
    pro=1;
    lenA = len(A)
    for i in range(0,lenA):
        for j in range(i+1,lenA):
                if A[i][i]==0:
                    print("Nie można dzielić przez 0!");
                    return 0;
                pro = (A[j][i]/A[i][i]);
                for k in range(0,lenA):
                    A[j][k] = A[j][k] - (pro * A[i][k]);
                b[j] = b[j] - (pro * b[i]);
            
    
    return Stepien_Patryk_ukladU(A,b)

A=[[2,-3,-1],
   [-4,10,5],
   [8,-4,4]]
    
b= [9,-29,12]
Stepien_Patryk_Gauss(A, b)

D=[[2,1,4],
   [6,6,14],
   [4,14,19]]
    
c= [1,8,25]
print("Próba dla innych wartosci.")
Stepien_Patryk_Gauss(D, c)