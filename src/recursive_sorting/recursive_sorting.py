# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    nA = len(arrA)
    nB = len(arrB)
    i = 0
    j = 0
    k = 0
    while (i < nA) & (j < nB):
        if arrA[i] <= arrB[j]:
            merged_arr[k] = arrA[i]
            i = i + 1
        else:
            merged_arr[k] = arrB[j]
            j = j + 1
        k = k + 1
    while i < nA:
        merged_arr[k] = arrA[i]
        i = i + 1
        k = k + 1
    while j < nB:
        merged_arr[k] = arrB[j]
        j = j + 1
        k = k + 1
    return merged_arr

# merge function works

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    n = len(arr)
    if n < 2:
        return arr
    left_index = 0
    right_index = n - 1
    middle_index = n // 2
    left = arr[:middle_index]
    right = arr[middle_index:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    sorted_arr = merge(sorted_left, sorted_right)
    return sorted_arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
