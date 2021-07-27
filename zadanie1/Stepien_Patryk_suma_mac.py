def Stepien_Patryk_suma_mac (A,B):
    kol = len(A[0])
    wier = len(A)
    E = "Error"
    if(kol == len(B[0])):
        if(wier == len(B)):
            wynik = [0] * wier
            
            for i in range(wier):
                wynik[i] = [0] * kol
                
            for i in range(0, wier):
                for j in range(0,kol):
                    wynik[i][j] = A[i][j] + B[i][j]
            return wynik
        print ("Różna liczba wierszy")
        return E
    print ("Różna liczba kolumn")
    return E
    


A=[[2,5],
   [2,4]]
B=[[2,6],
   [1,2]]
print(Stepien_Patryk_suma_mac(A, B))