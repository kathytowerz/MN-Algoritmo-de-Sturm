"""
Algoritmo de Sturm
:3 kiubole
vite se la come :v
Cocreado por José Pablo Muñoz
"""

B=[6,5,4,3,2]

def derivar(A):
    Ap=[]
    for i in range(len(A)):
        Ap.append(i*A[i])
    for i in range(1,len(Ap)):
        Ap[i-1]=Ap[i]
    Ap[len(Ap)-1]=0
    return Ap

print("P0:", B)
print("P1:", derivar(B))

def Sturm(P0):
    n=len(P0)
    j=n-1
    #k=j
    P1=derivar(P0)
    Pn=[]
    for i in range(n):
        Pn.append(i)
    #Pnaux=[]
    #for i in range(n):
        #Pnaux.append(0)
    for i in range(j,0,-1):
        if(P1[i-1]!=0):
            #Pnaux[j]=(P0[j]/P1[j])
            aux=P0[i]/P1[i-1]
            print(aux)
            break
    for i in range(j,-1,-1):
        Pn[i]=i
        print(i)
    print(Pn)
        
Sturm(B)
