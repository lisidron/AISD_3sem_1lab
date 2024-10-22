import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


filenames = ["Selection Sort", "Insertion Sort", "Bubble Sort", "Merge Sort",
             "Shell Sort", "Shell Hibbard Sort", "Shell Pratt Sort",
             "Quick Sort", "Heap Sort"]


def txtToDotsArr(filename, graphicsType):
    strNumber = 0
    data = []
    with open(filename, 'r') as file:
        for line in file:
            strNumber += 1

            if ((strNumber >= (3 + 12*graphicsType)) and (strNumber <= 12 + 12*graphicsType)):
                dataSec = [float(x) for x in line.strip().split("-")]
                data.append(dataSec)
            else:
                line.strip()

    return data

def plot_points(points, titleType, sortName):

    # Отделяем координаты X и Y
    x = points[:, 0]
    y = points[:, 1]

    # Создаем фигуру и ось
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Строим график
    ax.plot(x, y, marker='o', linestyle='-', color='b')
    # Устанавливаем заголовок и подписи осей
    if titleType == 0:
        title = sortName + ". График для отсортированного массива"
    elif titleType == 1:
        title = sortName + ". График для массива, отсортированного от \nбольшего к меньшему элементу"
    elif titleType == 2:
        title = sortName + ". График для массива со случайными элементами"
    elif titleType == 3:
        title = sortName + ". График для массива 90/10"

    ax.set_title(title)
    ax.set_xlabel("n, колличество элементом")
    ax.set_ylabel("t, время")

    ax.scatter(x, y, color='blue', label='Экспериментальные данные')


    # Отображаем график
    ax.legend()
    plt.legend()
    plt.grid(True)
    plt.savefig("graph/" + sortName + " " + str(titleType).replace("/", " ") + ".png")
    # plt.show()

def regression(points, titleType, sortName, model):

    x = points[:, 0]
    y = points[:, 1]
    # Выполняем регрессию
    if model == 'linear':
        # Линейная регрессия
        coefficients = np.polyfit(x, y, 1) # Линейная модель
        polynomial = np.poly1d(coefficients)
        regression_line = polynomial(x)

    elif model == 'quadratic':
        # Квадратичная регрессия
        coefficients = np.polyfit(x, y, 2) # Квадратичная модель
        polynomial = np.poly1d(coefficients)
        regression_line = polynomial(x)

    # Визуализация
    plt.scatter(x, y, color='orange', label='Экспериментальные данные')
    plt.plot(x, regression_line, color='purple', label=f'Регрессионная кривая')

    # Устанавливаем заголовок и подписи осей
    if titleType == 0:
        title = sortName + ". График для отсортированного массива"
    elif titleType == 1:
        title = sortName + ". График для массива, отсортированного от \nбольшего к меньшему элементу"
    elif titleType == 2:
        title = sortName + ". График для массива со случайными элементами"
    elif titleType == 3:
        title = sortName + ". График для массива 90/10"

    plt.title(title)
    plt.xlabel("n, колличество элементом")
    plt.ylabel("t, время")
    plt.grid(True)
    plt.legend()
    plt.savefig("graph/" + sortName + " Регрессия " + str(titleType).replace("/", " ") + ".png")
    plt.show()

def plotMultipleGraphs(data, graphicsType,  titleType, marker, filename, regression=False, degree=1):

    # colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Цвета для графиков
    colors = ['purple', 'orange', 'brown', 'pink', 'gray', 'olive', 'cyan', 'blue', 'green', 'red', ]
    # Устанавливаем заголовок и подписи осей
    if titleType == 0:
        title = "График для отсортированного массива"
    elif titleType == 1:
        title = "График для массива, отсортированного от \nбольшего к меньшему элементу"
    elif titleType == 2:
        title = "График для массива со случайными элементами"
    elif titleType == 3:
        title = "График для массива 90/10"

    for i, points in enumerate(data):
        x, y = zip(*points)
        # plt.plot(x, y, "-", color=colors[i % len(colors)], label=filenames[graphicsType[i]])
        if marker == 'o':
            plt.plot(x, y, "o", color=colors[i % len(colors)])

        if regression:
            # Подготовка данных для регрессии
            X = np.array(x).reshape(-1, 1)
            y = np.array(y)

            # Создание полиномиальных признаков
            poly = PolynomialFeatures(degree=degree)
            X_poly = poly.fit_transform(X)

            # Линейная регрессия
            model = LinearRegression()
            model.fit(X_poly, y)
            y_pred = model.predict(X_poly)

            plt.plot(x, y_pred, '-', color=colors[i % len(colors)],label=filenames[graphicsType[i]])
        else:
            plt.plot(x, y, '-', color=colors[i % len(colors)], label=filenames[graphicsType[i]])

    plt.title(title)
    plt.xlabel("n, колличество элементом")
    plt.ylabel("t, время")
    plt.grid(True)
    plt.legend()
    plt.savefig(filename)
    plt.show()

def plotOnceGraphs(data, graphicsType,  labelType, marker, regression=False, degree=1):

    colors = ['purple', 'orange', 'brown', 'pink', 'gray', 'olive', 'cyan', 'blue', 'green', 'red']
    for i, points in enumerate(data):
        x, y = zip(*points)

        if labelType[i] == 0:
            thisLabel = "Отсортированный массива"
        elif labelType[i] == 1:
            thisLabel = "Массив, отсортированный от \nбольшего к меньшему элементу"
        elif labelType[i] == 2:
            thisLabel = "Массив со случайными элементами"
        elif labelType[i] == 3:
            thisLabel = "Массив 90/10"

        if marker == 'o':
            plt.plot(x, y, "o", color=colors[i % len(colors)])

        if regression:
            # Подготовка данных для регрессии
            X = np.array(x).reshape(-1, 1)
            y = np.array(y)

            # Создание полиномиальных признаков
            poly = PolynomialFeatures(degree=degree)
            X_poly = poly.fit_transform(X)

            # Линейная регрессия
            model = LinearRegression()
            model.fit(X_poly, y)
            y_pred = model.predict(X_poly)

            plt.plot(x, y_pred, '-', color=colors[i % len(colors)], label=thisLabel)
        else:
            plt.plot(x, y, '-', color=colors[i % len(colors)],label=thisLabel)

    plt.title(filenames[graphicsType])
    plt.xlabel("n, колличество элементом")
    plt.ylabel("t, время")
    plt.grid(True)
    plt.legend()
    plt.savefig(f"graph/all/{filenames[graphicsType]}, Регрессия {regression}.png")
    plt.show()


def plotsOneFunc ():
    for i in range(0, len(filenames)):
        for j in range(0, 4):
            print(filenames[i])
            print(txtToDotsArr("data/" + filenames[i] + ".txt", j))
            points = np.array(txtToDotsArr(("data/" + filenames[i] + ".txt"), j))
            plot_points(points, j, filenames[i])
            regression(points, j, filenames[i], 'quadratic')



def plotsOnceFunction (graphics, marker, reg):
    types = [0,1,2,3]
    dots = []
    for i in types:
        dots.append(txtToDotsArr(("data/" + filenames[graphics]+".txt"), i))
    print(dots)

    plotOnceGraphs(dots, graphics, types, marker, reg, 2)

def plotsFunctions (graphics, marker, filename, regression):
    type = 2
    dots = []
    for i in graphics:
        dots.append(txtToDotsArr(("data/" + filenames[i]+".txt"), type))
    print(dots)

    plotMultipleGraphs(dots,graphics, type, marker, filename, regression, 2)

plotsOneFunc()

for i in range(len(filenames)):
    plotsOnceFunction(i, 'o', False)

for i in range(len(filenames)):
    plotsOnceFunction(i, '-', True)



filenames = ["Selection Sort", "Insertion Sort", "Bubble Sort", "Merge Sort",
             "Shell Sort", "Shell Hibbard Sort", "Shell Pratt Sort",
             "Quick Sort", "Heap Sort"]


logAvName = ["Merge Sort", "Quick Sort", "Heap Sort"]
quadAvName = ["Selection Sort", "Insertion Sort", "Bubble Sort",
             "Shell Sort", "Shell Hibbard Sort", "Shell Pratt Sort"]




def find (arr, arr1):
    numArr = []

    for i in range(len(arr)):
        for j in range(len(arr1)):
            if arr[i] == arr1[j]:
                numArr.append(i)

    return numArr



plotsFunctions(find(filenames, logAvName), 'o', "graph/svod/log.png", False)
plotsFunctions(find(filenames, quadAvName), 'o', "graph/svod/quad.png", False)
plotsFunctions(range(9), 'o', "graph/svod/all.png", False)

plotsFunctions(find(filenames, logAvName), '-', "graph/svod/logRegression.png", True)
plotsFunctions(find(filenames, quadAvName), '-', "graph/svod/quadRegression.png", True)
plotsFunctions(range(9), '-', "graph/svod/allRegression.png", True)







