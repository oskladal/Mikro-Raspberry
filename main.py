#třídicí algoritmy - laboratorní úloha
import random
import time
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np

seznam = [random.uniform(0, 1000) for p in range(0, 10000)]

def bubble(vstup):
    seconds = time.time()
    for i in range(len(vstup)):
        for j in range(len(vstup) - 1):
            if vstup[j] > vstup[j+1]:

                vstup[j], vstup[j+1] = vstup[j+1], vstup[j]

    seconds2 = time.time()
    #zaokrouhlime a prevedeme na ms
    times = round((seconds2 - seconds) * 1000, 2)

    return vstup, times


def selection(vstup):
    seconds = time.time()
    for i in range(len(vstup)):
        min = i
        for j in range(i + 1, len(vstup)):
            if vstup[j] < vstup[min]:
                min = j
        vstup[i], vstup[min] = vstup[min], vstup[i]
    seconds2 = time.time()
    # zaokrouhlime a prevedeme na ms
    times = round((seconds2 - seconds) * 1000, 2)
    return vstup, times


def merge(vstup):
    seconds = time.time()
    if len(vstup) >1:
        left = vstup[: len(vstup)//2]
        right = vstup[len(vstup) //2 :]

        #rekurze
        merge(left)
        merge(right)

        #spojení
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                vstup[k] = left[i]
                i+=1
            else:
                vstup[k]=right[j]
                j+=1
            k+=1

        while i < len(left):
            vstup[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            vstup[k] = right[j]
            j+=1
            k+=1
    seconds2 = time.time()
    # zaokrouhlime a prevedeme na ms
    times = round((seconds2 - seconds) * 1000, 2)
    return vstup, times

#10K

#definuji pole
bubbletime10K = []
selectiontime10K = []
mergetime10K = []

#plním pole od zadu časy jednotlivých třídění - v každém cyklu nové generované pole
for x in range(100):
    seznam10K = [random.uniform(0, 1000) for p in range(0, 10000)]
    times = bubble(seznam10K)[1]
    bubbletime10K.append(times)

for x in range(100):
    seznam10K = [random.uniform(0, 1000) for p in range(0, 10000)]
    times = selection(seznam10K)[1]
    selectiontime10K.append(times)

for x in range(100):
    seznam10K = [random.uniform(0, 1000) for p in range(0, 10000)]
    times = merge(seznam10K)[1]
    mergetime10K.append(times)

#beru průměrnou hodnotu z pole
prumbub10K = mean(bubbletime10K)
prumsel10K = mean(selectiontime10K)
prumerg10K = mean(mergetime10K)

#výpis průměrných časů
print(" ")
print("Pro 10K:")
print(prumbub10K, 'ms')
print(prumsel10K, 'ms')
print(prumerg10K, 'ms')

#100K

bubbletime100K = []
selectiontime100K = []
mergetime100K = []

for x in range(100):
    seznam100K=[random.uniform(0, 1000) for p in range(0, 100000)]
    times = bubble(seznam100K)[1]
    bubbletime100K.append(times)

for x in range(100):
    seznam100K=[random.uniform(0, 1000) for p in range(0, 100000)]
    times = selection(seznam100K)[1]
    selectiontime100K.append(times)

for x in range(100):
    seznam100K=[random.uniform(0, 1000) for p in range(0, 100000)]
    times = merge(seznam100K)[1]
    mergetime100K.append(times)


prumbub100K = mean(bubbletime100K)
prumsel100K = mean(selectiontime100K)
prumerg100K = mean(mergetime100K)

print(" ")
print("Pro 100K:")
print(prumbub100K, 'ms')
print(prumsel100K, 'ms')
print(prumerg100K, 'ms')

#1M

bubbletime1M = []
selectiontime1M = []
mergetime1M = []

for x in range(100):
    seznam1M = [random.uniform(0, 1000) for p in range(0, 1000000)]
    times = bubble(seznam1M)[1]
    bubbletime1M.append(times)

for x in range(100):
    seznam1M = [random.uniform(0, 1000) for p in range(0, 1000000)]
    times = selection(seznam1M)[1]
    selectiontime1M.append(times)

for x in range(100):
    sseznam1M = [random.uniform(0, 1000) for p in range(0, 1000000)]
    times = merge(seznam1M)[1]
    mergetime1M.append(times)


prumbub1M = mean(bubbletime1M)
prumsel1M = mean(selectiontime1M)
prumerg1M = mean(mergetime1M)

print(" ")
print("Pro 1M:")
print(prumbub1M, 'ms')
print(prumsel1M, 'ms')
print(prumerg1M, 'ms')




plt.subplot(3, 1, 1)
plt.bar(["BubbleSort", "SelectSort", "MergeSort"], [prumbub10K,prumsel10K,prumerg10K], color=['r','g','b'])
plt.ylabel("Time [ms]")
plt.title("10k numbers")


plt.subplot(3, 1, 2)
plt.bar(["BubbleSort", "SelectSort", "MergeSort"], [prumbub100K,prumsel100K,prumerg100K], color=['r','g','b'])
plt.ylabel("Time [ms]")
plt.title("100k numbers")


plt.subplot(3, 1, 3)
plt.bar(["BubbleSort", "SelectSort", "MergeSort"], [prumbub1M,prumsel1M,prumerg1M], color=['r','g','b'])
plt.ylabel("Time [ms]")
plt.title("1M numbers")


plt.show()