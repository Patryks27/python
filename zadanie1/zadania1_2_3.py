def silnia(n):
    suma=1
    for x in range(1,n+1):
        suma=suma*x
    print("Silnia:",n,"= ",suma,"\n") 
    return suma
   

def dodawanie_macierzy (A,B):
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
    
def mnozenie_macierzy (A,B):
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
    

silnia(6)
silnia(4)

a =[[0,2,3],
    [2,1,1]]
b =[[1,2,1],
    [0,0,2]]
print(dodawanie_macierzy(a, b))

c = [[5,-1,0],
     [4,9,4],
     [-10,0,7],
     [1,2,3]]
d = [[1,-5,5],
     [6,-2,1],
     [2,13,-3]
     ]
print(mnozenie_macierzy(c,d))
