import time
from arrays.txtToArr import txtToArr

from sorting.InsertionSort import insertionSort
from sorting.BubbleSort import bubbleSort
from sorting.MergeSort import mergeSort
from sorting.QuickSort import quickSort
from sorting.HeapSort import heapSort
from sorting.SelectionSort import selectionSort
from sorting.ShellSort import shellSort, shellSortPratt, shellSortHibbard

filenames = ["Selection Sort", "Insertion Sort", "Bubble Sort", "Merge Sort",
             "Shell Sort", "Shell Hibbard Sort", "Shell Pratt Sort",
             "Quick Sort", "Heap Sort"]

def someKindOfSorting (arr, sortName):
    if (sortName==0):
        timer = time.time()
        selectionSort(arr)
        timer = time.time() - timer
        print(filenames[sortName])
    elif (sortName==1):
        timer = time.time()
        insertionSort(arr)
        timer = time.time() - timer
        print(filenames[sortName])
    elif (sortName==2):
        timer = time.time()
        bubbleSort(arr)
        timer = time.time() - timer
        print(filenames[sortName])
    elif (sortName==3):
        timer = time.time()
        mergeSort(arr)
        timer = time.time() - timer
        print(filenames[sortName])
    elif (sortName==4):
        timer = time.time()
        shellSort(arr)
        timer = time.time() - timer
        print(filenames[sortName])
    elif (sortName==5):
        timer = time.time()
        shellSortHibbard(arr)
        timer = time.time() - timer
        print(filenames[sortName])
    elif (sortName==6):
        timer = time.time()
        shellSortPratt(arr)
        timer = time.time() - timer
        print(filenames[sortName])
    elif (sortName==7):
        timer = time.time()
        quickSort(arr)
        timer = time.time() - timer
        print(filenames[sortName])
    elif (sortName==8):
        timer = time.time()
        heapSort(arr)
        timer = time.time() - timer
        print(filenames[sortName])
    else:
        print(f"Неверно передан аргумент. Сортировок всего {len(filenames)} штук")
        return 0


    file.write(str(len(arr)) + "-" + str(timer) + "\n")
    return timer



for i in range(0, len(filenames)):
    file = open("data/" + filenames[i] + ".txt", "w+", encoding="UTF-8")
    file.write(filenames[i])

    directionNames = ["randomArrs", "reverseArrs", "semiSortedArrs", "sortArrs"]



    file.write("\nГрафик для отсортированного массива\n")
    for j in range(1, 11):
        arr = txtToArr("arrays/sortArrs/" + str(j) + ".txt")

        print(someKindOfSorting(arr,i))

    file.write("\nГрафик для массива, отсортированного от большего к меньшему элементу\n")
    for j in range(1, 11):
        reverseArr = txtToArr("arrays/reverseArrs/" + str(j) + ".txt")

        print(someKindOfSorting(reverseArr,i))

    file.write("\nГрафик для массива со случайными элементами:\n")
    for j in range(1, 11):
        randomArr = txtToArr("arrays/randomArrs/" + str(j) + ".txt")

        print(someKindOfSorting(randomArr,i))

    file.write("\nГрафик для массива 90/10\n")
    for j in range(1, 11):
        semiSortedArr = txtToArr("arrays/semiSortedArrs/" + str(j) + ".txt")

        print(someKindOfSorting(semiSortedArr,i))

    file.close()
    print(f"Подсчет {filenames[i]} закончен.")







