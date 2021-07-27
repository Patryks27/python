import copy

def Stepien_Patryk_Eliminacja_Gaussa_LU(A):
    lenA = len(A);
    L = copy.deepcopy(A)
    for i in range(0,lenA):
        for j in range(0,lenA):
            if j==i:
                L[i][j]=1;
            else:
                L[i][j]=0;
    for i in range(0,lenA-1):
        for j in range(i+1,lenA):
            if A[i][i]==0:
                print("NIe można dzielić przez 0!")
                return A,L;
            dziel= A[j][i]/A[i][i];
            L[j][i]=dziel;
            for k in range(0,lenA):
                A[j][k]=A[j][k]-(A[i][k]*dziel) 
            
    print("U:",A,"L:",L)
    return A,L;


A=[[1,2,3],
   [2,8,11],
   [3,14,25],]
Stepien_Patryk_Eliminacja_Gaussa_LU(A)