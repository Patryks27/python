def Stepien_Patryk_ukladL(L,b):
    wynik = b[:];
    suma =0;
    lenA = len(L)
    for i in range(0,lenA):
        if L[i][i]==0:
            print("Nie można dzielić przez 0!")
            return 0;
        for j in range(0,i):
            suma = suma + (L[i][j]*wynik[j])
        wynik[i]=(b[i] - suma)/L[i][i];
        suma =0;
       
    print("Wynik:",wynik);
    return wynik

L=[[1,0,0],
   [-3,1,0],
   [4,2,1]]
    
b= [2,2,16]
Stepien_Patryk_ukladL(L, b);