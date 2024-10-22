import random


def partially_shuffled_array(array):

    # Создаем копию исходного массива
    shuffled_array = array.copy()

    # Вычисляем количество элементов для перемешивания
    num_to_shuffle = int(len(array) * 0.05)

    # Создаем список индексов для перемешивания
    indices = list(range(len(array)))
    random.shuffle(indices)

    # Перемешиваем выбранные элементы
    for i in range(num_to_shuffle):
        j = indices[i]
        shuffled_array[i], shuffled_array[j] = shuffled_array[j], shuffled_array[i]

    return shuffled_array



def newArrs ():
    directionNames = ["randomArrs", "reverseArrs", "semiSortedArrs", "sortArrs"]
    file = open("1.txt", "w+", encoding="UTF-8")

    for i in directionNames:
        for j in range(1,11):
            if i == "randomArrs":
                file = open(i + "/" + str(j) + ".txt", "w+", encoding="UTF-8")
                randomArr = [random.randint(0, 10 ** 4 * j) for _ in range(10 ** 4 * j)]
                file.write(str(randomArr))
                file.close()

            elif i == "reverseArrs":
                file = open(i + "/" + str(j) + ".txt", "w+", encoding="UTF-8")
                reverseArr = [x for x in range(10 ** 4 * j, 0, -1)]
                file.write(str(reverseArr))
                file.close()

            elif i == "semiSortedArrs":
                file = open(i + "/" + str(j) + ".txt", "w+", encoding="UTF-8")
                semiSortedArr = partially_shuffled_array([x for x in range(1, 10 ** 4 * j + 1)])
                file.write(str(semiSortedArr))
                file.close()

            elif i == "sortArrs":
                file = open(i + "/" + str(j) + ".txt", "w+", encoding="UTF-8")
                arr = [x for x in range(1, 10 ** 4 * j + 1)]
                file.write(str(arr))
                file.close()
        print(i)
newArrs()








