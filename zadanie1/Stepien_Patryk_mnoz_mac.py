def Stepien_Patryk_suma_mac (A,B):
    kol = len(A[0])
    wier = len(A)
    t = 0
    E = "Error"
    if(kol == len(B)):
        wynik = [0] * wier
            
        for i in range(wier):
            wynik[i] = [0] * len(B[0])
            
        for i in range(0, len(wynik)):
            for j in range(0, len(wynik[0])):
                for k in range(0, kol):
                    t += A[i][k] * B[k][j]
                wynik[i][j] += t
                t=0
        return wynik
    return E
    

A=[[2,5],
   [2,4]]
B=[[2,6],
   [1,2]]
print(Stepien_Patryk_suma_mac(A, B))