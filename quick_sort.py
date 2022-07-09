import time


def partition(data, head, tail, drawdata, timetick):
    border = head
    pivot = data[tail]

    drawdata(data, colorarray(len(data), head, tail, border, border))
    time.sleep(timetick)
    for i in range(head, tail):
        if data[i] < pivot:
            drawdata(data, colorarray(len(data), head, tail, border, i, True))
            time.sleep(timetick)
            data[border], data[i] = data[i], data[border]
            border += 1
        drawdata(data, colorarray(len(data), head, tail, border, i))
        time.sleep(timetick)

    # swapping pivot elements with border
    drawdata(data, colorarray(len(data), head, tail, border, tail, True))
    time.sleep(timetick)
    data[border], data[tail] = data[tail], data[border]
    return border


def quick_sort(data, head, tail, drawdata, timetick):
    if head < tail:
        partition_idx = partition(data, head, tail, drawdata, timetick)

        # left partition
        quick_sort(data, head, partition_idx - 1, drawdata, timetick)

        # right partition
        quick_sort(data, partition_idx + 1, tail, drawdata, timetick)


def colorarray(datalen, head, tail, border, curridx, isswapping=False):
    colorarray = []
    for i in range(datalen):
        # Base color
        if i >= head and i <= tail:
            colorarray.append("grey")
        else:
            colorarray.append("white")

        if i == tail:
            colorarray[i] = "orange"
        elif i == border:
            colorarray[i] = "red"
        elif i == curridx:
            colorarray[i] = "yellow"

        if isswapping:
            if i == border or i == curridx:
                colorarray[i] = "green"
    return colorarray
