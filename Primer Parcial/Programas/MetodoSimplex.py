#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 07:16:43 2022

@author: usuario
"""
import numpy as np

def Simp_Met(A,b,c):
    """
    INPUT:
     A.-Matriz de costo. 
     b.- Vector del lado derecho.
     c.- Coeficientes de la funcion a optimizar.
    OUTPUT:
     x.- Solucion basica factible y optima del problema definido por A,b,c.   
    """
   

    
    s=A.shape # Dimension de la matriz A (mxn), s=(m,n)
              #m.- numero de filas de A,
              #n.- numero de columnas
              #A=[B|N]
    
    
    
    z_c=np.zeros(s[1]-s[0])#z_c.- Este vector contiene en sus entrada i-esima
                           #el numero z_i-c_i, donde x_i es no basico  
                           # s[1]-s[0].- Numero de variables no basicas
    
    k=1 # Indice que guardara a k
    
    lim=1# Variable que guarda a max_j{ z_j-c_j}
    
    while(lim>0):# Esta condicion es equivalente a que exista una variable no basica x_k 
                 # que entre a la base
        
        
      B=A[:, 0:s[0]]     # Base B,  (matriz mxm)
      N=A[:, s[0]:s[1]]  #Columnas con indices no basicos (Matriz mx(n-m))
      
      
      
      c_B=c[:s[0]]       #  Entradas de c con coeficientes basicos (c_1,...,c_m).
      
      c_N=c[s[0]:s[1]]   # Entradas de c con coeficientes NO basicos (c_(m+1),...,c_n) 
      
      l_zc= s[1]-s[0]    # n-m
      
      B_inv= np.linalg.inv(B) # B^{-1}
#      b_= np.dot(B_inv,b)    # b^{-}
      
      k=1
      lim= -np.inf 
      
      for i in range(0,l_zc):
          #En la iteracion i-esima de este ciclo for se calcula z_i-c_i
          hd=np.dot(c_B,B_inv)
          z_c=np.dot(hd,N[:,i])-c_N[i]#z_c guarda al valor z_i-c_i
          
          if z_c > lim:
              lim=z_c
              k=i #Indice de la variable no negativa con maximo z_k-c_k      
      
      x=np.dot(B_inv,b)#x_B
      #x=x_B-x_ky_k
      if (lim>0):# Existencia de una variable que entra x_k
          
        y_k= np.dot(B_inv,N[:,k])    
        
        
        x_k= np.inf
        r=0
        
        for i in range(0,len(y_k)):  
        
          if y_k[i]>0.0 and x_k*y_k[i]> x[i]:
              
              x_k=x[i]/y_k[i]
              r=i
          
        if  x_k< np.inf :
            
            x=x-x_k*y_k
            
            
            x[r]=x_k
            
            B_aux=B[:,r].copy()           
            N_aux=N[:,k].copy()
            
            c_Baux=c_B[r].copy()
            c_Naux=c_N[k].copy()
            
            B[:,r]=N_aux
            N[:,k]=B_aux
            
            c_B[r]=c_Naux
            c_N[k]=c_Baux
            
        else:
       
            print("La solucion optima es no acotada.")                              
           
    return x      
         
          
          
          
          

A=np.array([[1.0, 0.0, 2.0, 3.0],
            [0.0, 1.0, -1.0, 1.0]])
    
b=np.array([6.0,1.0])    
c=np.array([0.0, 0.0, -1.0, -3.0])    

print(Simp_Met(A,b,c))
    
    
