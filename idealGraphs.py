import math
from math import log10

import numpy as np
import matplotlib.pyplot as plt

def selectionBest(x):
    return (x+1)*x/2
def selectionAv(x):
    return (x**2 + 3*x)/4
def selectionWorst(x):
    return (x**2 + x)/2

def insertionBest(x):
    return 4*x-4
def insertionAv(x):
    return (3*x**2 + 13*x - 16)
def insertionWorst(x):
    return (3*x**2 + 5*x - 8)

def bubbleBest(x):
    return (x**2 - x)/2
def bubbleAv(x):
    return 3*x*(x-1)/4
def bubbleWorst(x):
    return x**2 - x

def mergeBest(x):
    return x + 2 * x * np.log2(x)
def mergeAv(x):
    return x * np.log2(x)
def mergeWorst(x):
    return 2* x * np.log(x) + x + 1

def shellBest(x):
    return 2*x*np.log2(x) - 2*x
def shellAv(x):
    return x**2
def shellWorst(x):
    return 2*x**2

def quickBest(x):
    return x*np.log2(x)
def quickAv(x):
    return x*np.log2(x)
def quickWorst(x):
    return x**2

def heapBest(x):
    return x + (x-1)*np.log2(x)
def heapAv(x):
    return x*np.log2(x)-x
def heapWorst(x):
    return 4*x*np.log2(x) - 2*x - np.log2(x)


def plot_multiple_functions(functions, title, labels, pictureName):
    colors = ['purple', 'orange', 'brown', 'pink', 'gray', 'olive', 'cyan', 'blue', 'green', 'red']
    if not isinstance(functions, list):
        functions = [functions]
    if not isinstance(labels, list):
        labels = [labels]

    x = np.linspace(1, 100000, 100)

    for i, func in enumerate(functions):
        y = func(x)
        plt.plot(x, y, label=labels[i], color=colors[i % len(colors)])

    plt.title(title)
    plt.xlabel("n")
    plt.ylabel("O(n)")

    plt.legend()
    plt.grid(True)
    plt.savefig(pictureName)
    plt.show()




titlesType = ["Лучший случай", "Средний случай", "Худший случай"]


functionsBest = [selectionBest, insertionBest, bubbleBest, mergeBest, shellBest, quickBest, heapBest]
functionsAv = [selectionAv, insertionAv, bubbleAv, mergeAv, shellAv, quickAv, heapAv]
functionsWorst = [selectionWorst, insertionWorst, bubbleWorst, mergeWorst, shellWorst, quickWorst, heapWorst]
filenames = ["Selection Sort", "Insertion Sort", "Bubble Sort", "Merge Sort",
             "Shell Sort", "Quick Sort", "Heap Sort"]



for i in range(7):
    for j in range(3):

        plot_multiple_functions(functionsBest[i], filenames[i], titlesType[j], ("idealGraph/ " + str(i) + str(j) + filenames[i] + titlesType[j]))


for i in range(7):
    plot_multiple_functions([functionsBest[i], functionsAv[i], functionsWorst[i]], filenames[i], titlesType,
                            ("idealGraph/allVariations/" + str(filenames[i])))


logAv = [mergeAv, quickAv, heapAv]
quadAv = [selectionAv, insertionAv, bubbleAv, shellAv]
logAvName = ["Merge Sort", "Quick Sort", "Heap Sort"]
quadAvName = ["Selection Sort", "Insertion Sort", "Bubble Sort",
             "Shell Sort"]

plot_multiple_functions(logAv, titlesType[1], logAvName, "idealGraph/all/Свобдный теор лог")
plot_multiple_functions(quadAv, titlesType[1], quadAvName, "idealGraph/all/Свобдный теор квад")
plot_multiple_functions(logAv+quadAv, titlesType[1], logAvName + quadAvName, "idealGraph/all/Свобдный теор")

logWorst = [mergeWorst, heapWorst]
quadWorst = [selectionWorst, insertionWorst, bubbleWorst, shellWorst, quickWorst]






