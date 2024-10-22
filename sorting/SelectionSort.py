def selectionSort(arr):
    # Проходим по каждому элементу массива
    for i in range(len(arr)):
        # Ищем минимальный элемент в оставшейся части массива
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Меняем найденный минимальный элемент с первым элементом
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
