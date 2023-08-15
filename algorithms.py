import main

#///////////////////////////////////////////////////////////////////////
#                       SORTING ALGORITHMS
#///////////////////////////////////////////////////////////////////////

def bubbleSort(draw_info, ascending):
    lst = draw_info.lst
    # Traverse through all array elements
    for i in range(len(lst)-1):
        for j in range(len(lst)- i - 1):
            if (lst[j] > lst[j + 1] and ascending) or (lst[j]<lst[j+1] and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                main.draw_list(draw_info, {j: draw_info.GREEN, j+1:draw_info.RED},True)
                yield True

def insertionSort(draw_info, ascending):
    lst =draw_info.lst
    n = len(lst)
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = lst[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while (j >= 0 and key < lst[j] and ascending) or (j>=0 and key>lst[j] and not ascending):  # Move elements greater than key one position ahead
            lst[j + 1] = lst[j]  # Shift elements to the right
            j -= 1
            main.draw_list(draw_info,{i: draw_info.RED, j: draw_info.GREEN},True)
            yield True
        lst[j + 1] = key


def selectionSort(draw_info, ascending):
    lst = draw_info.lst
    for ind in range(len(lst)):
        minmax_index = ind
        for j in range(ind + 1, len(lst)):
            if ascending:
                # select the minimum element in every iteration
                if lst[j] < lst[minmax_index]:
                    minmax_index = j
            else:
                if lst[j] > lst[minmax_index]:
                    minmax_index = j
        # swapping the elements to sort the array
        (lst[ind], lst[minmax_index]) = (lst[minmax_index], lst[ind])
        main.draw_list(draw_info,{ind: draw_info.RED, minmax_index: draw_info.GREEN}, True)
        yield True


def heapify_min(arr, n, i):
    smallest = i  # Initialize smallest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # If left child is smaller than root
    if l < n and arr[l] < arr[smallest]:
        smallest = l

    # If right child is smaller than
    # smallest so far
    if r < n and arr[r] < arr[smallest]:
        smallest = r

    # If smallest is not root
    if smallest != i:
        (arr[i],
         arr[smallest]) = (arr[smallest],
                           arr[i])

        # Recursively heapify the affected
        # sub-tree
        heapify_min(arr, n, smallest)

def heapify_max(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

 # Change root, if needed

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap

        heapify_max(arr, n, largest)


def heapSort(draw_info,ascending):
    lst = draw_info.lst
    n = len(lst)

    for i in range(n // 2 - 1, -1, -1):
        if ascending:
            heapify_max(lst, n, i)
        else:
            heapify_min(lst,n,i)

    for i in range(n - 1, 0, -1):
        (lst[i], lst[0]) = (lst[0], lst[i])  # swap
        if ascending:
            heapify_max(lst, i, 0)
        else:
            heapify_min(lst, i, 0)
        main.draw_list(draw_info, {0: draw_info.RED, i:draw_info.GREEN}, True)
        yield True
