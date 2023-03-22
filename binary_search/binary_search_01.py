# Algoritimo que encontra a posição do valor alvo dentro de um array SORTED.
# O array precisa estar SORTED.
# Metade do array será eliminado durante cada "passo"

# O algoritimo de busca binária não é muito eficiente em datasets pequenos.
# O algoritimo de busca binaria será muito eficiente quando estivermos trabalhando com datasets gigantes, como por exemplo 1 milhão de dados.

# A comlexidade do algoritimo de busca binária é O(log n).
# Quanto maior o dataset, a busca binária se torna mais eficiente comparando com outros algoritmos de busca.

def binary_search(int_array, numero):

    low = 0
    high = len(int_array) - 1

    while low <= high:
        middle = int(low + (high - low) / 2)
        value = int_array[middle]

        print("middle: " ,value)

        if value < numero:
            low = middle + 1
        elif value > numero:
            high = middle - 1
        else:
            return middle #numero encontrado
    return -1


int_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

print(binary_search(int_array, 42))