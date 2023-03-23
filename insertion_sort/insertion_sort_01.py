# Algoritimo que pega um Array, começa no index 1, armazena o valor que estiver no index em uma variável temporária e compara com o valor anterior.
# A cada iteração, o processo é repetido.
# O algoritimo chega no final quando todos os itens da lista tiverem sido percorridos
# Complexidade de O(n2). No melho cenário ele performa como O(n)
# Decente para pequenos dataset. Péssimo para grandes datasets.

def insertion_sort(int_array):
    i = 1
    for i in range(len(int_array)):
        temp = int_array[i]
        j = i - 1

        while j >= 0 and int_array[j] >= temp:
            int_array[j+1] = int_array[j]
            j -= 1

        int_array[j+1] = temp
    return int_array


int_array = [9, 1, 8, 2, 7, 3, 6, 5, 4]

print(insertion_sort(int_array))
