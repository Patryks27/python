def Stepien_Patryk_ukladU(L,b):
    wynik = b[:];
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
       
    print("Wynik:",wynik);
    return wynik

L=[[3,2,3],
   [0,2,3],
   [0,0,-4]]
    
b= [2,8,-8]
Stepien_Patryk_ukladU(L, b);
