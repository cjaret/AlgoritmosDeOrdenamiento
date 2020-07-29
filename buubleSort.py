#1.- Comenzar a hacer comparaciones de elementos adyacentes
#2.- Repetir hasta tener una pasada completa sin ningun swap

from datetime import datetime

def bubbleSort(array):
    
    n = len(array)
    
    for i in range(n):
        print(array)

        for j in range(0, n-i-1):    
            if array[j] > array [j+1]:
                array[j], array[j+1] = array[j+1], array[j]

array = [1,98,2,8,9,6,8,5,20,89,8,5,2,6,5,8]

tiempoInicial = datetime.now()

bubbleSort(array)

for i in range(len(array)):
    print("%d"%array[i]),

print(datetime.now() - tiempoInicial),