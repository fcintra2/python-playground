"""
    BUBBLE SORT
    Percorre o conjunto de dados, comparando o elemento atual com o seu
    sucessor e promovendo a troca entre eles caso o primeiro seja maior
    que o segundo.

    Faz isso em várias passadas, até, que, na última delas, nenhuma troca
    tenha sido registrada.
"""

def bubble_sort(lista):
    
    while True:
        trocas = 0
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                trocas += 1
        if trocas == 0:
            break

nums = [7, 4, 9, 0, 6, 1, 8, 2, 5, 3]

bubble_sort(nums)

print(nums)