# array / easy (sorting)

def insertionSort(array):
    # i get reassigned at start of each loop in 'range'
    for i in range(1, len(array)):
        while i > 0 and array[i] < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
    return array
