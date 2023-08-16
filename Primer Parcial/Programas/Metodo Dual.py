"Salinas Velazquez Jacob"

import math
import numpy as np

"VALORES Q INGRESAR"
p = [6, 5, 12, 3, 4]
Q = [[-2, -1, -5,  0,  1],
    [8, -3, -2,  -1,  1]]
r = [-5, -7]

"FUNCION DE TABLA"

def tablat(p, Q, r):
    xb = [eq + [x] for eq, x in zip(Q, r)]
    z = p + [0]
    return xb + [z]

"FUNCION PIVOTE"

def pivote(tabla, posicion_pivote):
    nuetabla = [[] for eq in tabla]

    i, j = posicion_pivote
    valorpivote = tabla[i][j]
    nuetabla[i] = np.array(tabla[i]) / valorpivote

    for eq_i, eq in enumerate(tabla):
        if eq_i != i:
            multiplicar = np.array(nuetabla[i]) * tabla[eq_i][j]
            nuetabla[eq_i] = np.array(tabla[eq_i]) - multiplicar

    return nuetabla

"FUCION PARA MEJORAR DUAL"

def mejorardual(tabla):
    entradasrhs = [fila[-1] for fila in tabla[:-1]]
    return any([entrada < 0 for entrada in entradasrhs])

"FUNCION CONSEGUIR POSICION PIVOTE"

def conposicionpiv(tabla):
    entradasrhs = [fila[-1] for fila in tabla[:-1]]
    valminrhs = min(entradasrhs)
    fila = entradasrhs.index(valminrhs)

    columnas = []
    for index, elemento in enumerate(tabla[fila][:-1]):
        if elemento < 0:
            columnas.append(index)
    valorcolumna = [tabla[fila][p] / tabla[-1][p] for p in columnas]
    colminindex = valorcolumna.index(min(valorcolumna))
    columna = columnas[colminindex]

    return fila, columna

"FUNCION PARA VER SI UNA COLUMNA ES BASICA"
def basica(columna):
    return sum(columna) == 1 and len([p for p in columna if p == 0]) == len(columna) - 1

def solucion(tabla):
    columnas = np.array(tabla).T
    soluciones = []
    for columna in columnas[:-1]:
        soluc = 0
        if basica(columna):
            unindice = columna.tolist().index(1)
            soluc = columnas[-1][unindice]
        soluciones.append(soluc)

    return soluciones

def dual_simplex(p, Q, r):
    tabla = tablat(p, Q, r)

    while mejorardual(tabla):
        posicion_pivote = conposicionpiv(tabla)
        tabla = pivote(tabla, posicion_pivote)

    return solucion(tabla)

dual_simplex(p, Q, r)
print('Dual: ', dual_simplex(p, Q, r))