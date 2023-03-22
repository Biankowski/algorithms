# Complexidade de O(n2)

def selection_sort(int_array):
    for i in range(len(int_array)):
        minimun_index = i
        for j in range(i+1, len(int_array)):
            if int_array[j] < int_array[minimun_index]:
                minimun_index = j
        int_array[i], int_array[minimun_index] = int_array[minimun_index], int_array[i]
    return int_array


int_array = [4,9,3,6,2,8,7,5,11,15,14]

print(selection_sort(int_array))