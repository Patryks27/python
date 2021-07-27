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


def Stepien_Patryk_Gauss_pivot(a,b):
    pro=1;
    lenA = len(a)
    for i in range(0,lenA):
        największa = a[i][i];
        index = i;
        for k in range(0,lenA):
            if największa < a[k][i]:
                największa = a[k][i];
                index=k;
        if index!=i:
                pom = a[i];
                a[i]= a[index];
                a[index]=pom;
                pom1= b[i];
                b[i]= b[index];
                b[index]=pom1;
        for j in range(i,lenA):
            if i!=j:
                pro = (a[j][i]/a[i][i]);
                for k in range(0,lenA):
                    a[j][k] = a[j][k] - (pro * a[i][k]);
                b[j] = b[j] - (pro * b[i]);
        
    for i in range(0,lenA-1):
        for j in range(i,lenA):
            if a[j][i]!=0:
                pom = a[i];
                a[i]=a[j];
                a[j]=pom;
                pom1= b[i];
                b[i]=b[j];
                b[j]=pom1;
    Stepien_Patryk_ukladU(a, b)
    return b
    
a=[[2,1,4],
   [6,6,14],
   [4,14,19]]
b=[1,8,25] 

Stepien_Patryk_Gauss_pivot(a, b)
print()
c=[[2,-3,-1],
   [-4,10,5],
   [8,-4,4]]
d=[9,-29,12]
Stepien_Patryk_Gauss_pivot(c, d)
