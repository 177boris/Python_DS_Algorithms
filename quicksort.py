from queues import Queue


def partition(input_list,low,high):
    i = (low - 1)
    item = input_list[high]
    for j in range(low, high):
        if input_list[j] <= item:
            i = i + 1
            input_list[i], input_list[j] =  input_list[j], input_list[i]
    input_list[i+1],input_list[high] = input_list[high],input_list[i+1]
    return (i+1)

def quickSort(input_list, low, high):
    if low < high:
        partition_index = partition(input_list,low,high)
        quickSort(input_list, low, partition_index - 1)
        quickSort(input_list, partition_index + 1, high)
        
        
queue = Queue()

input_l = queue.create()
list_length = len(input_l)
quickSort(input_l, 0, list_length -1)

print(f"Quickly sorted ! :      {input_l}")

