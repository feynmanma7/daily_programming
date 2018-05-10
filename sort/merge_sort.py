#encoding:utf-8

def merge_sort(arr, start, end):

    if start < end:
        mid = int((start + end) / 2)
        arr[start:mid+1] = merge_sort(arr, start, mid)[start:mid+1]
        arr[mid+1:end+1] = merge_sort(arr, mid + 1, end)[mid+1:end+1]
        arr = merge(arr, start, mid, end)

    return arr


def merge(arr, start, mid, end):

    left_arr = arr[start:mid+1]
    right_arr = arr[mid+1:end+1]

    i = 0
    j = 0
    idx = start

    while i < len(left_arr) and j < len(right_arr):

        if left_arr[i] < right_arr[j]:
            arr[idx] = left_arr[i]
            i += 1
            idx += 1
        else:
            arr[idx] = right_arr[j]
            j += 1
            idx += 1

    if i < len(left_arr):
        arr[idx:idx+len(left_arr)-i] = left_arr[i:]

    if j < len(right_arr):
        arr[idx:idx+len(right_arr)-j] = right_arr[j:]

    return arr



if __name__ == '__main__':
    arr = [2, 1, 8, 5, 3, 4, 7, 6]
    print(merge_sort(arr, 0, 7))

