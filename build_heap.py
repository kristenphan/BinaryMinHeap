# python3


def build_heap_naive(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps

def LeftChild(i):
    return 2*i + 1

def RightChild(i):
    return 2*i + 2

# this function heapifies the subtree starting at node array[i] and turns it into a binary-min tree format
# inputs include:
# array = array that contains all nodes to be re-arranged into a binary-min heap,
# n = size of the array,
# swaps = list to keep track of swap operations performed when MinHeapify is called
# i = index of the starting node of the subtree
def MinHeapify(array, n, swaps, i):
    minIdx = i
    l = LeftChild(i)
    if l <= (n-1) and array[l] < array[minIdx]:
        minIdx = l
    r = RightChild(i)
    if r <= (n-1) and array[r] < array[minIdx]:
        minIdx = r
    if minIdx != i:
        array[i], array[minIdx] = array[minIdx], array[i]
        swaps.append([i,minIdx])
        MinHeapify(array, n, swaps, minIdx)

# this function builds and returns a binary-min heap from the argument array of integers
# input format:
# first line of the input contains single integer n.
# the next line contains n space-separated integers ai
# output format:
# the first line of the output should contain single integer - the total number of swaps with 0<= m <= 4n
# the next m lines contain the swap operations used to convert the array into a heap.
# each swap is described by a pair of integers i, j - the 0-based indices of the elements to be swapped
# note that all elements of the input array are distinct
# sample input:
# 5
# 5 4 3 2 1
# sample output (note: the transformed array is 1 2 3 5 4 which is already a binary-min heap)
# 3
# 1 4
# 0 1
# 1 3
# if the input is already a binary-min heap, the function will return 0 as the number of swaps performed is 0
def build_heap(data, n):
    swaps = [] # store all swap operations performed
    # the array data is of size n
    # because the data will be transformed into a binary tree, there are n//2 non-leaf nodes out of n nodes
    # additionally, all leaf nodes do not have children and, therefore, do not violate the heap property
    # that said, in order to transform the data into a binary-min heap, we need to min-heapify all non-leaf nodes
    i = n//2
    while i >= 0:
        MinHeapify(data, n, swaps, i)
        i -= 1

    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data, n)

    print(len(swaps))
    for i in range(len(swaps)):
        print(swaps[i][0],swaps[i][1])


if __name__ == "__main__":
    main()
