# A complexidade do algoritmo de busca sequencial(linear search) 
# é de O(n).
# Quanto maior for o dataset, maior será a quantidade de passos para concluir a busca.

# Desvantagens:
#   Lento para grandes datasets
#Vantagens:
#   Rápido para buscas em pequenos e médios datasets
#   Não precisa ser sorted
#   Bons para estruturas de dados que não tenham acesso randômico


def linear_search(int_array, numero):

    for i in range(len(int_array)):
        if int_array[i] == numero:
            return i
    return -1


int_array = [9, 1, 8, 2, 7, 3, 6, 4, 5]

index = print(linear_search(int_array, 5))