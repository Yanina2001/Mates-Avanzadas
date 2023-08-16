import numpy as np  
from fractions import Fraction 
  
print("\n Algoritmo metodo simplex tabular \n\n") 
  
  
A = np.array([[1, 1, 0, 1], [2, 1, 1, 0]]) 
b = np.array([8, 10])            
c = np.array([1, 1, 0, 0])              
  
cb = np.array(c[3]) 
B = np.array([[3], [2]])           
 
cb = np.vstack((cb, c[2]))         
xb = np.transpose([b])                  
table = np.hstack((B, cb))              
table = np.hstack((table, xb))          
table = np.hstack((table, A))          
table = np.array(table, dtype ='float')  
  
MIN = 0
  
print("Tabla en itr = 0") 
print("B \tCB \tXB \ty1 \ty2 \ty3 \ty4") 
for row in table: 
    for el in row: 
                
        print(Fraction(str(el)).limit_denominator(100), end ='\t')  
    print() 
print() 
  
reached = 0     
itr = 1
unbounded = 0
alternate = 0
  
while reached == 0: 
  
    print("Iteracion: ", end =' ') 
    print(itr) 
    print("B \tCB \tXB \ty1 \ty2 \ty3 \ty4") 
    for row in table: 
        for el in row: 
            print(Fraction(str(el)).limit_denominator(100), end ='\t') 
        print() 
  
    
    i = 0
    rel_prof = [] 
    while i<len(A[0]): 
        rel_prof.append(c[i] - np.sum(table[:, 1]*table[:, 3 + i])) 
        i = i + 1
  
    print("Profit: ", end =" ") 
    for profit in rel_prof: 
        print(Fraction(str(profit)).limit_denominator(100), end =", ") 
    print() 
    i = 0
      
    b_var = table[:, 0] 
    
    while i<len(A[0]): 
        j = 0
        present = 0
        while j<len(b_var): 
            if int(b_var[j]) == i: 
                present = 1
                break; 
            j+= 1
        if present == 0: 
            if rel_prof[i] == 0: 
                alternate = 1
                print("Caso Alterno encontrado") 
                
        i+= 1
    print() 
    flag = 0
    for profit in rel_prof: 
        if profit>0: 
            flag = 1
            break
        
    if flag == 0: 
        print("Todas las ganancias son <= 0, optimalidad alcanzada") 
        reached = 1
        break
  
    
    k = rel_prof.index(max(rel_prof)) 
    min = 99999
    i = 0; 
    r = -1
    
    while i<len(table): 
        if (table[:, 2][i]>0 and table[:, 3 + k][i]>0):  
            val = table[:, 2][i]/table[:, 3 + k][i] 
            if val<min: 
                min = val 
                r = i     
        i+= 1
  
        
    if r ==-1: 
        unbounded = 1
        print("Limite") 
        break
  
    print("Pivote:", end =' ') 
    print(np.array([r, 3 + k])) 
  
    pivot = table[r][3 + k] 
    print("Elemento del pivote: ", end =" ") 
    print(Fraction(pivot).limit_denominator(100)) 
          
        
    
    table[r, 2:len(table[0])] = table[ 
            r, 2:len(table[0])] / pivot 
              
    
    i = 0
    while i<len(table): 
        if i != r: 
            table[i, 2:len(table[0])] = table[i, 2:len(table[0])] - table[i][3 + k] *table[r, 2:len(table[0])] 
        i += 1
  
      
    
    table[r][0] = k 
    table[r][1] = c[k] 
      
    print() 
    print() 
    itr+= 1
  
if unbounded == 1: 
    print("Limite") 
    exit() 
if alternate == 1: 
    print("Solucion ALTERNATIVA") 
  
print("Tabla Opimizada:") 
print("B \tCB \tXB \ty1 \ty2 \ty3 \ty4") 
for row in table: 
    for el in row: 
        print(Fraction(str(el)).limit_denominator(100), end ='\t') 
    print() 
print() 
print("Valor optimo de Z: ", end =" ") 
  
basis = [] 
i = 0
sum = 0
while i<len(table): 
    sum += c[int(table[i][0])]*table[i][2] 
    temp = "x"+str(int(table[i][0])+1) 
    basis.append(temp) 
    i+= 1
if MIN == 1: 
    print(-Fraction(str(sum)).limit_denominator(100)) 
else: 
    print(Fraction(str(sum)).limit_denominator(100)) 
print("Base Final: ", end =" ") 
print(basis) 
  
print("Fin...") 
print() 