import time

def merge(arr, begin, mid, end, displayArr):
    p = begin
    q = mid + 1
    tempArray = []

    for i in range(begin, end + 1):
        if p > mid:
            tempArray.append(arr[q])
            q += 1
        elif q > end:
            tempArray.append(arr[p])
            p += 1
        elif arr[p] < arr[q]:
            tempArray.append(arr[p])
            p += 1
        else:
            tempArray.append(arr[q])
            q += 1

    for p in range(len(tempArray)):
        arr[begin] = tempArray[p]
        begin += 1


def merge_sort(arr, begin, end, displayArr, tym):
    if begin < end:
        mid = int((begin + end) / 2)
        merge_sort(arr, begin, mid, displayArr, tym)
        merge_sort(arr, mid + 1, end, displayArr, tym)

        merge(arr, begin, mid, end, displayArr)

        displayArr(arr, ["#71189E" if x >= begin and x < mid else "#A225AD" if x == mid
        else "#F381FC" if x > mid and x <= end else "blue" for x in range(len(arr))])
        time.sleep(tym)

    displayArr(arr, ["blue" for x in range(len(arr))])

