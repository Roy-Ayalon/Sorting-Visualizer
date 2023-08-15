# Sorting-Visualizer

This is a project that I made to show my knowledge in python and sorting algorithms 

Examples:

# -**Bubble Sort**

![Bubble sort Gif](https://github.com/Roy-Ayalon/Sorting-Visualizer/assets/90352235/cfb6af72-d78d-47a1-8e4b-e15bd4ae3d67)

Time Complexity: O(n^2)

Space Complexity: O(1)

**How it works?**
1. Iterate through the List: Start by iterating through the entire list of elements, comparing each element with its adjacent element.

2. Compare and Swap: Compare the current element with the next element. If the current element is greater than the next element, swap them. This step ensures that the larger elements "bubble up" towards the end of the list.

3. Repeat Iterations: Continue iterating through the list, comparing and swapping adjacent elements until you reach the end. This completes one pass of the algorithm.

4. Multiple Passes: Repeat the above steps for a number of passes equal to the total number of elements in the list. With each pass, the largest unsorted element will "bubble up" to its correct position at the end of the list.

# -**Insertion Sort**

![Insertion Sort Gif](https://github.com/Roy-Ayalon/Sorting-Visualizer/assets/90352235/af990249-5cc9-437c-a880-dda45478ebc7)

Time Complexity: O(n^2)

Space Complexity: O(1)

**How it works?**
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

# -Heap Sort

![Heap Sort Gif](https://github.com/Roy-Ayalon/Sorting-Visualizer/assets/90352235/e2b23140-83f3-444e-9c4b-faa0d6b365a7)

Time Complexity: O(n*log(n))

Space Complexity: O(log(n))

**How it works?**
First convert the array into heap data structure using heapify, then one by one delete the root node of the Max-heap and replace it with the last node in the heap and then heapify the root of the heap.

Repeat this process until size of heap is greater than 1.

Build a heap from the given input array.

Repeat the following steps until the heap contains only one element:

Swap the root element of the heap (which is the largest element) with the last element of the heap.

Remove the last element of the heap (which is now in the correct position).

Heapify the remaining elements of the heap.

The sorted array is obtained by reversing the order of the elements in the input array.

# -Selection Sort

![Selection Sort Fig](https://github.com/Roy-Ayalon/Sorting-Visualizer/assets/90352235/52d85845-4f7d-47d1-8612-4794a9429ea5)

Time Complexity: O(n^2)

Space Complexity: O(1)

**How it works?**
1. Divide the Array: Start by dividing the array into two parts: a sorted portion and an unsorted portion. Initially, the sorted portion is empty, and the unsorted portion contains all the elements.

2. Find the Minimum: Search the unsorted portion of the array to find the minimum element.

3. Swap Minimum: Swap the minimum element found in step 2 with the first element of the unsorted portion. This effectively adds the minimum element to the end of the sorted portion and reduces the size of the unsorted portion by one.

4. Expand Sorted Portion: Increment the boundary between the sorted and unsorted portions. Now, the sorted portion is one element larger, and the unsorted portion is one element smaller.

5. Repeat Steps 2-4: Repeat steps 2 to 4 until the unsorted portion becomes empty. In each iteration, find the minimum element in the remaining unsorted portion and swap it with the first element of the unsorted portion.
