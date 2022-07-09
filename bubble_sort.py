import time


def bubble_sort(data, drawdata, time_tick):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]  # swapping
                drawdata(data, ["yellow" if x == j or x == j + 1 else "#A90042" for x in range(len(data))])
                time.sleep(time_tick)
    drawdata(data, ["yellow" for x in range[len(data)]])
