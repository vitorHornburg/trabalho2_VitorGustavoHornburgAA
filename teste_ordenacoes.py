
import time
import random
import pandas as pd
from statistics import mean

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Tempo de execução
def medir_tempo(algoritmo, arr):
    inicio = time.perf_counter()
    algoritmo(arr)
    fim = time.perf_counter()
    return fim - inicio

# Parâmetros de teste
tamanhos = [1000, 5000, 10000, 20000, 50000, 100000]
repeticoes = 5
algoritmos = {
    "Bubble Sort": bubble_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort
}
casos = {
    "Aleatório": lambda n: [random.randint(1, 100000) for _ in range(n)],
    "Ordenado": lambda n: list(range(n)),
    "Reverso": lambda n: list(range(n, 0, -1))
}

resultados = []

for tamanho in tamanhos:
    for tipo, gerador in casos.items():
        base = gerador(tamanho)
        for nome, func in algoritmos.items():
            tempos = []
            for _ in range(repeticoes):
                vetor = base.copy()
                tempo = medir_tempo(func, vetor)
                tempos.append(tempo)
            media = mean(tempos)
            resultados.append({
                "Caso": tipo,
                "Algoritmo": nome,
                "Tamanho": tamanho,
                "Tempo Médio (s)": media,
                "Tempos Individuais": tempos
            })
            print(f"Executado: {nome} | {tipo} | {tamanho} -> Média: {media:.4f}s")

df_resultados = pd.DataFrame(resultados)
df_resultados.to_csv("resultados_teste_casos_completo.csv", index=False)
print("Resultados salvos em resultados_teste_casos_completo.csv")
