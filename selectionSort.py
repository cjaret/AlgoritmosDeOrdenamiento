#Buscar el número menor en mi array
#Crear dos sub arrays para llevar el control de mi algoritmo
#imprimir resultado del ordenamiento

import sys

array = [20,3,6,9,00,4,2,5,67,4455,66]

def selectionSort(array):
    #Recorrer todo el array
    for i in range(len(array)):

        #Encontrar el valor mínimo restante de nuestro array desordenado
        idxDesordenado = i

        for j in range(i+1, len(array)):
            
            if array[idxDesordenado] > array[j]:
                idxDesordenado = j

        #Cambiar el mínimo elemento por el primer valor de nuestro array desordenado

        array[i], array[idxDesordenado] = array[idxDesordenado], array[i]

selectionSort(array)
for i in range(len(array)):
    print("%d" %array[i]),