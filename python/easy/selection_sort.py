# array / easy (sorting)

def selectionSort(array):
    for i in range(len(array)-1):
        smallest = i
        for j in range(i+1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]
    return array
