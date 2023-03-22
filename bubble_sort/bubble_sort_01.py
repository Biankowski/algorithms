# O algoritimo de Bubble sorte pega um array desordenado e o ordena em valores ascendentes
# O algoritimo de bubble sort no pior caso terá complexidade de tempo - O(n2)
# No melhor dos casos, se o array já estiver ordenado, a complexidade de tempo ainda será O(n)

def bubble_sort(list_a):
    indexing_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    
    return list_a


print(bubble_sort([4,6,9,2,3,5,8,7]))