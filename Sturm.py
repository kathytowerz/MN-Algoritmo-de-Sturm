"""
Algoritmo de Sturm
Creado por Kathleen Lucía Torres Mancilla, 
           Francisco Javier Vite Mimila y 
           José Pablo Muñoz Guerrero
"""

from future import division

B=[6.0,5.0,4.0,3.0,2.0]
C=[-2.0,1.0,0.0,-4.0,0.0,0.0,1.0]


#Esta función deriva el polinomio
def derivar(A):
    Ap=[]
    for i in range(len(A)):
        Ap.append(i*A[i])
    for i in range(1,len(Ap)):
        Ap[i-1]=Ap[i]
    Ap[len(Ap)-1]=0.0
    return Ap

#Esta función da el grado del polinomio
def dar_grado(A):
    for i in range(len(A)-1,-1,-1):
        if(A[i]!=0):
            g=i
            break
    return g

#Se ven las listas antes de meterlas a la función
print("P0:", C)
print("P1:", derivar(C))

def Sturm(Pn,izq,der):
    #Se definen variables que serán utilizadas después
    P1=derivar(Pn)
    grado=dar_grado(Pn)
    guar_izq=0
    guar_der=0
    contador_izq=0
    contador_der=0
    
    #Se valuan los polinomios originales para analizar los cambios de signo después
    aux=Pn[0]
    for i in range(1,dar_grado(Pn)+1):
        aux=Pn[i]*izq**i+aux 
    if(aux<0):
        señ_izq=-1
    else:
        señ_izq=1
    if(guar_izq!=señ_izq):
        contador_izq+=1
        guar_izq=señ_izq
    
    #Se repite el procedimiento para el extremo derecho
    aux=Pn[0]
    for i in range(1,dar_grado(Pn)+1):
        aux=Pn[i]*der**i+aux    
    if(aux<0):
        señ_der=-1
    else:
        señ_der=1
    if(guar_der!=señ_der):
        contador_der+=1
        guar_der=señ_der
    
    #Ahora se evalua la derivada del polinomio    
    aux=P1[0]
    for i in range(1,dar_grado(P1)+1):
        aux=P1[i]*izq**i+aux    
    if(aux<0):
        señ_izq=-1
    else:
        señ_izq=1
    if(guar_izq!=señ_izq):
        contador_izq+=1
        guar_izq=señ_izq
    
    aux=P1[0]
    for i in range(1,dar_grado(P1)+1):
        aux=P1[i]*der**i+aux  
    if(aux<0):
        señ_der=-1
    else:
        señ_der=1
    if(guar_der!=señ_der):
        contador_der+=1
        guar_der=señ_der
      
    #Comienza el ciclo de divisiones del polinomio
    while(dar_grado(P1)!=0):
        aux=0
        grado=dar_grado(Pn)
        
        #Se toma el valor del divisor para definir el auxiliar
        #Pn se convierte en el cociente
        while(dar_grado(P1)<=dar_grado(Pn)):
            #print("Bien")
            aux=Pn[dar_grado(Pn)]/P1[dar_grado(P1)]
            diferencia=dar_grado(Pn)-dar_grado(P1)
            print("Auxiliar:",aux,"\nDiferencia:", diferencia)
            for i in range(dar_grado(P1)+diferencia,-1,-1):
                Pn[i]=Pn[i]-aux*P1[i-diferencia]
        Pn[grado]=0.0
        
        #Se invierten los signos del polinomio
        for i in range(dar_grado(Pn)+1):
            Pn[i]=-Pn[i]
        print("Cociente:",Pn)
        
        #Se valua el polinomio en el extremo izquierdo
        aux=Pn[0]
        for i in range(1,dar_grado(Pn)+1):
            aux=Pn[i]*izq**i+aux
        print("Pn (",izq,") =",aux)
        
        if(aux<0):
            señ_izq=-1
        else:
            señ_izq=1
        #Si cambia de signo respecto a la iteración pasada, sube el contador
        if(guar_izq!=señ_izq):
            contador_izq+=1
            guar_izq=señ_izq
        
        #Se repite el procedimiento para el extremo derecho
        aux=Pn[0]
        for i in range(1,dar_grado(Pn)+1):
            aux=Pn[i]*der**i+aux
        print("Pn (",der,") =",aux)
        
        if(aux<0):
            señ_der=-1
        else:
            señ_der=1
        if(guar_der!=señ_der):
            contador_der+=1
            guar_der=señ_der
        
        #Se reacomodan los polinomios para la siguiente iteración    
        P=Pn
        Pn=P1
        P1=P
        
        print("\nNueva iteración")
        print("Pn:", Pn)
        print("P1", P1)
    #Si se rompe el ciclo, se restan ambos contadores
    
    print("\nContador izquierdo:", contador_izq,"\nContador derecho:", contador_der)
    num=abs(contador_izq-contador_der)
    print("\nEn el intervalo dado, el polinomio tiene",num,"raíces.")
