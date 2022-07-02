"""
    Merge sort is an efficient, general-purpose, comparison-based sorting algorithm.
    Most implementations produce a stable sort, which means that the order of equal
    elements is the same in the input and output.
    Merge sort is a divide and conquer algorithm.
"""



from queues import Queue


def merge(listA, listB):
    # merging two sorted arrays to one sorted array
    newlist = list()
    a = 0
    b = 0
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newlist.append(listA[a])
            a += 1
        else:
            newlist.append(listB[b])
            b += 1
    while a < len(listA):
        newlist.append(listA[a])
        a += 1
    while b < len(listB):
        newlist.append(listB[b])
        b += 1
    return newlist


def merge_sort(input_list):
    # recursive function to divide array into 2 sub arrays for sorting
    if len(input_list) <= 1:
        return input_list
    else:
        mid = len(input_list) // 2
        left = merge_sort(input_list[:mid])
        right = merge_sort(input_list[mid:])
        newlist = merge(left, right)
        return newlist


queue = Queue()
a = queue.create()
print(merge_sort(a))