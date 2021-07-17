"""
    QUICK SORT
    
    Escolhe um dos elementos da lista para ser o pivô (na nossa implementação,
    o último elemento) e, na primeira passada, divide a lista, a partir da posição
    final da lista, em uma sublista à esquerda contendo apenas valores menores que
    o pivô e outra sublista à direita, que contém apenas valores maiores que o pivô.
    
    Em seguida, recursivamente, repete o processo em cada um dos sublistas até que
    toda a lista esteja ordenada.

"""

def quick_sort(lista, fn_comp, ini = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
    # print(f'ini: {ini}, fim: {fim}')

    if fim > ini:
        pivot = fim
        div = ini - 1
        
        # Loop for vai até a PENÚLTIMA posição
        ## print(f'range: {range(ini, fim)}')
        for i in range(ini, fim):
            ## print(f'i: {i}, pivot: {pivot}, div: {div}')
            if fn_comp(lista[pivot], lista[i]) and i != div + 1:
                div += 1
                lista[i], lista[div] = lista[div], lista[i]
        div += 1

        # Colocamos o pivô no seu lugar definitivo
        ## print(f'pivot: {pivot}, div: {div}, lista[pivot]: {lista[pivot]}, lista[div]: {lista[div]}')
        if fn_comp(lista[div], lista[pivot]):
            lista[pivot], lista[div] = lista[div], lista[pivot]

        ## print(f'LISTA: {lista}')

        # Ordena o subvetor à esquerda do pivô
        quick_sort(lista, fn_comp, ini, div - 1)

        # Ordena o subvetor à direita do pivô
        quick_sort(lista, fn_comp, div + 1, fim)

#nums = [7, 4, 9, 0, 6, 1, 8, 2, 5, 3]

#quick_sort(nums)

#print(nums)

from includes.lista_dici_100k_nomes import lista_dados_nomes
from time import time
import sys
sys.setrecursionlimit(100000)
#import tracemalloc

# lista_dados_nomes = lista_dados_nomes[0:10000]

def comp(a, b):
    return a["first_name"] > b["first_name"]

start = time()
#tracemalloc.start()

#quick_sort(lista_dados_nomes, lambda a, b: a["first_name"] > b["first_name"])
quick_sort(lista_dados_nomes, comp)

#current, peak = tracemalloc.get_traced_memory()
end = time()

print(lista_dados_nomes)

print(f'Tempo gasto: {end - start}s')
#print(f"Current memory usage is {current / 1024}KB; Peak was {peak / 1024}KB")
#tracemalloc.stop()