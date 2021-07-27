def Stepien_Patryk_silnia(n):
    suma=1
    for x in range(1,n+1):
        suma=suma*x
    #print("Silnia:",n,"= ",suma,"\n") 
    return suma


print(Stepien_Patryk_silnia(6))