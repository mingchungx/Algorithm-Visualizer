#Algorithm Visualizer
import matplotlib.pyplot as plt
from random import randint
import PySimpleGUI as sg

pause_time = 0.000000001

#VISUALIZATION
def plot(arr,foo):
    global pause_time
    #After each sort display it on a chart, compare value to index
    plt.bar([i for i in range(len(arr))],arr)
    plt.title(foo)
    plt.xlabel("Index")
    plt.ylabel("Element Value")
    plt.draw() #show() is not cleared by .clf()
    plt.pause(pause_time)
    plt.clf() #clear

##################################################################################################################

#BUBBLE SORT
def bubblesort(arr):
    size = len(arr)
    for i in range(size-1): #Negate 1 because that is start/end
        swapped = False
        for j in range(size-1-i): #The i is amount of sorted elements at end of array
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                swapped = True
                plot(arr,"Bubble Sort")
        if not swapped:
            break

##################################################################################################################

#QUICKSORT
def swap(a,b,arr):
    if a != b:
        arr[a],arr[b] = arr[b],arr[a]

def partition(arr, start, end):
    pivot = arr[end]
    p_index = start
    for i in range(start, end):
        if arr[i] <= pivot:
            swap(i, p_index,arr)
            p_index += 1
    swap(p_index,end,arr)
    return p_index

def quicksort(arr, start, end):
    if len(arr) == 1:
        return
    if start < end:
        part_index = partition(arr, start, end)
        quicksort(arr, start, part_index-1)
        quicksort(arr, part_index+1, end)
        plot(arr,"Quick Sort - Lumoto")

##################################################################################################################

#INSERTION SORT
def insertionsort(elements):
    for i in range(1,len(elements)):
        anchor = elements[i] #Elements dealt with now
        j = i - 1 #Previous element
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j -= 1
        plot(elements,"Insertion Sort")
        elements[j+1] = anchor

##################################################################################################################

#MERGE SORT
def merge_two_sorted_arr(arr1,arr2,arrS):
    len1 = len(arr1)
    len2 = len(arr2)
    i = j = k = 0
    while i < len1 and j < len2: 
        if arr1[i] <= arr2[j]:
            arrS[k] = arr1[i] 
            i += 1 
            k += 1 
        else: 
            arrS[k] = arr2[j]
            j += 1
            k += 1
    while i < len1:
        arrS[k] = arr1[i]
        i += 1
        k += 1
    while j < len2:
        arrS[k] = arr2[j]
        j += 1
        k += 1

def mergesort(arr): 
    if len(arr) <= 1:
        return 
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    mergesort(left) 
    mergesort(right)

    merge_two_sorted_arr(left,right,arr)
    
    plot(arr,"Merge Sort")

##################################################################################################################

#SHELL SORT
def shellsort(arr):
    size = len(arr)
    gap = size // 2 
    while gap > 0: 
        for i in range(gap,size):
            anchor = arr[i]
            j = i
            while arr[j-gap] > anchor and j >= gap: 
                arr[j] = arr[j-gap] 
                j -= gap
            arr[j] = anchor
        plot(arr,"Shell Sort")
        gap = gap // 2

##################################################################################################################

if __name__ == "__main__":
    #INTERFACE
    layout = [
        [sg.Text("Enter desired algorithm: 'bubble sort', 'quick sort', 'insertion sort', 'merge sort', 'shell sort'")],
        [sg.Text('->'), sg.InputText()],
        [sg.Text("Enter randomized array size, 1 -> 50 inclusive")],
        [sg.Text("->"), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')] 
        ]

    window = sg.Window('Window Title', layout)
    running = True
    #Event loop
    algorithms = (
            "bubble sort",
            "quick sort",
            "insertion sort",
            "merge sort",
            "shell sort"
            )

    while running:
        event, values1 = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if values1[0] not in algorithms:
            print("Invalid algorithm")
            break
        if values1[0] in algorithms:
            alg = values1[0]
            size = int(values1[1])
            break

    window.close()

    if size > 50 or size <= 0: #Make sure data size is reasonable
        raise Exception("Invalid Size, must be between 1 - 25 inclusive.")

    #Get a randomly sorted, non-repetitive array of numbers 1 -> inp inclusive
    arr = []
    for i in range(1,size+1):
        while len(arr) >= 0: 
            x = randint(1,size) #Keep finding a new random number until it is not in the array already, once it is, append it
            if x not in arr:
                arr.append(x)
                break #Once you append it you move to the next number
            else:
                continue
    
    if alg == "bubble sort":
        bubblesort(arr)
    elif alg == "quick sort":
        quicksort(arr,0,len(arr)-1)
    elif alg == "insertion sort":
        insertionsort(arr)
    elif alg == "merge sort":
        mergesort(arr)
    elif alg == "shell sort":
        shellsort(arr)
    else:
        raise Exception("Invalid Algorithm, choose 'bubble sort', 'quick sort', 'insertion sort', 'merge sort', 'shell sort'")