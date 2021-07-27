def Stepien_Patryk_ukladL(L,b):
    pro=1;
    lenA = len(L)
    for i in range(0,lenA):
        if L[i][i]==0:
            print("Nie można dzielić przez 0!")
            return 0;
        pro = 1/L[i][i];
        L[i][i] = 1;
        b[i]= b[i] * pro;
        for j in range(i+1,lenA):
            pro = L[j][i];
            L[j][i]= L[j][i] - (L[i][i]* pro)
            b[j]= b[j] - (b[i] * pro)
    print(L,"Wynik:",b)
    return L,b

L=[[-2,0,0],
   [1,3,0],
   [4,2,2]]
    
b= [2,5,2]
Stepien_Patryk_ukladL(L, b);