def Stepien_Patryk_Doolittle(A):
    lenA = len(A);
    U = [[0] * lenA for i in range(lenA)];
    U[0]=A[0];
    L = [[0] * lenA for i in range(lenA)];
    
    for i in range(0,lenA):
        for j in range(i,lenA):
            suma = 0;
            for k in range(0,i):
                suma= suma + (L[i][k] * U[k][j]);
            U[i][j]=A[i][j] - suma;
            
        for j in range(i,lenA):
            suma = 0;
            for k in range(0,i):
                suma= suma + (L[j][k] * U[k][i]);
            L[j][i]=(A[j][i] - suma)/U[i][i];
                
    print(L,U);
    return A;

A=[[5,3,2],
   [1,2,0],
   [3,0,4]]
Stepien_Patryk_Doolittle(A)

