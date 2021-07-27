def Stepien_Patryk_Gauss_jordan(a,b):
    pro=1;
    lenA = len(a)
    for i in range(0,lenA):
        for j in range(0,lenA):
            if i!=j:
                pro = (a[j][i]/a[i][i]);
                for k in range(0,lenA):
                    a[j][k] = a[j][k] - (pro * a[i][k]);
                b[j] = b[j] - (pro * b[i]);

    for i in range(0,lenA):
        b[i]= b[i]/a[i][i]
    print(b)
    return b
    
a=[[2,1,4],
   [6,6,14],
   [4,14,19]]
b=[1,8,25] 

Stepien_Patryk_Gauss_jordan(a, b)

c=[[2,-3,-1],
   [-4,10,5],
   [8,-4,4]]
d=[9,-29,12]
Stepien_Patryk_Gauss_jordan(c, d)