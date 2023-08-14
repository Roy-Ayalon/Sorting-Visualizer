import pygame
import numpy as np
import random

pygame.init()

class DrawInformation:

    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BACKGROUND_CLR = WHITE
    GRAYS = [(128,128,128),
             (192,192,192),
             (162,162,162)]

    SIDE_PAD = 100
    TOP_PAD = 150

    FONT = pygame.font.SysFont("comicsans", 30)
    MEDIUM_FONT = pygame.font.SysFont("comicsans", 20)
    SMALL_FONT = pygame.font.SysFont("comicsans", 10)


    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst =lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = (self.width - self.SIDE_PAD) // len(lst)
        self.block_height = (self.height - self.TOP_PAD) // (self.max_val - self.min_val)
        self.start_x = self.SIDE_PAD // 2

def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_CLR)
    controls = draw_info.FONT.render("R - Reset  A- Ascending  D- Distending", 1, draw_info.BLACK)
    sorting = draw_info.MEDIUM_FONT.render("B - Bubble Sort  I - Insertion Sort  H - Heap Sort  S - Selection Sort",1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width // 2 - controls.get_width() // 2, 5))
    draw_info.window.blit(sorting, (draw_info.width // 2 - sorting.get_width() // 2, 45))
    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info, color_positions = {} , clear_bg = False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD,
                      draw_info.width -draw_info.SIDE_PAD, draw_info.height- draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_CLR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i*draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) *draw_info.block_height

        color = draw_info.GRAYS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width,draw_info.height))

        val_text = draw_info.SMALL_FONT.render(str(val),1, draw_info.BLACK)
        draw_info.window.blit(val_text, (x,draw_info.height-20))

    if clear_bg:
        pygame.display.update()


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
                draw_list(draw_info, {j: draw_info.GREEN, j+1:draw_info.RED},True)
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
            draw_list(draw_info,{i: draw_info.RED, j: draw_info.GREEN},True)
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
        draw_list(draw_info,{ind: draw_info.RED, minmax_index: draw_info.GREEN}, True)
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
        draw_list(draw_info, {0: draw_info.RED, i:draw_info.GREEN}, True)
        yield True

def main():
    run =True
    clock =pygame.time.Clock()

    min_val = 0
    max_val = 100
    n = 50
    sorting = False
    ascending =True

    lst = generate_starting_list(n,min_val,max_val)
    draw_info = DrawInformation(800,600,lst)

    sorting_algorithm = bubbleSort
    sorting_algorithm_generator = None

    while run:
        clock.tick(100)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting =False
        else:
            draw(draw_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue
            elif event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_a:
                ascending = True
            elif event.key == pygame.K_d:
                ascending = False
            elif event.key == pygame.K_b and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)
            elif event.key == pygame.K_i and sorting == False:
                sorting =True
                sorting_algorithm = insertionSort
                sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)
            elif event.key == pygame.K_s and sorting == False:
                sorting = True
                sorting_algorithm = selectionSort
                sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)
            elif event.key == pygame.K_h and sorting == False:
                sorting = True
                sorting_algorithm = heapSort
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)

    pygame.quit()


if __name__ == '__main__':
    main()