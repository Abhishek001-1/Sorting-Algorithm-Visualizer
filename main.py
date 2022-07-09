from tkinter import *
from tkinter import ttk
from bubble_sort import bubble_sort
from quick_sort import quick_sort
import random

root = Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry('900x600')
root.config(bg='black')
data = []


# Drawing bars
def drawdata(data, color_array):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 870
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing_bet_rect = 10

    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x1 = i * x_width + offset + spacing_bet_rect
        y1 = canvas_height - height * 400
        # We've multiplied 400 because we'll normalize our values with one formula so that our data
        # won't exceed our canvas

        x2 = (i + 1) * x_width
        y2 = canvas_height

        canvas.create_rectangle(x1, y1, x2, y2, fill=color_array[i])
        canvas.create_text(x1 + 2, y1, anchor=SW, text=str(data[i]), font=("new roman", 15, "italic bold"),
                           fill="orange")

    root.update_idletasks()


def StartAlgorithm():
    global data
    if not data:
        return
    if algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, drawdata, speed_scale.get())
        drawdata(data, ["green" for x in range(len(data))])

    elif algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawdata, speed_scale.get())


def Generate():
    global data
    print("Selected Algorithm :" + selected_algorithm.get())
    minivalue = int(minvalue.get())

    maxivalue = int(maxvalue.get())

    sizeevalue = int(sizevalue.get())

    data = []
    for i in range(sizeevalue):
        # We'll add that speed scaled by appending it
        data.append(random.randrange(minivalue, maxivalue + 1))
    drawdata(data, ['#A90042' for x in range(len(data))])


selected_algorithm = StringVar()

# Label,buttons
mainlabel = Label(root, text="Algorithm : ", font=("new roman", 15, "italic bold"), bg="#05897A", width=10, fg="black",
                  relief=GROOVE, bd=5)
mainlabel.place(x=0, y=0)

algo_menu = ttk.Combobox(root, width=15, font=("new roman", 18, "italic bold"), textvariable=selected_algorithm,
                         values=["Bubble Sort", "Merge Sort", "Quick Sort"])
algo_menu.place(x=145, y=0)
algo_menu.current(0)  # by default bubble sort

# Generate button
random_generate = Button(root, text="Generate", bg="#2DAE9A", font=("arial", 12, "italic bold"), relief=SUNKEN,
                         activebackground="#05945B", activeforeground="white", bd=5, width=10, command=Generate)
random_generate.place(x=750, y=60)

# To choose specific size of array
size_value_label = Label(root, text="Size:", font=("new roman", 12, "italic bold"), bg="#0E6DA5", width=10,
                         fg="black", height=2, relief=GROOVE, bd=5)
size_value_label.place(x=0, y=60)

sizevalue = Scale(root, from_=0, to=30, resolution=1, orient=HORIZONTAL, font=("arial", 14, "italic bold"),
                  relief=GROOVE, bd=2, width=10)
sizevalue.place(x=120, y=60)

# we'll set a particular range of numbers from min to max
# min
min_value_label = Label(root, text="Min Value:", font=("new roman", 12, "italic bold"), bg="#0E6DA5", width=10,
                        fg="black", height=2, relief=GROOVE, bd=5)
min_value_label.place(x=250, y=60)

minvalue = Scale(root, from_=0, to=10, resolution=1, orient=HORIZONTAL, font=("arial", 14, "italic bold"),
                 relief=GROOVE, bd=2, width=10)
minvalue.place(x=370, y=60)

# max
max_value_label = Label(root, text="Max Value:", font=("new roman", 12, "italic bold"), bg="#0E6DA5", width=10,
                        fg="black", height=2, relief=GROOVE, bd=5)
max_value_label.place(x=500, y=60)

maxvalue = Scale(root, from_=0, to=100, resolution=1, orient=HORIZONTAL, font=("arial", 14, "italic bold"),
                 relief=GROOVE, bd=2, width=10)
maxvalue.place(x=620, y=60)

# Start
start = Button(root, text="Start", bg="#C45B09", font=("arial", 12, "italic bold"), relief=SUNKEN,
               activebackground="#05945B", activeforeground="white", bd=5, width=10, command=StartAlgorithm)
start.place(x=750, y=0)

# Speed
speed_label = Label(root, text="Speed: ", font=("new roman", 12, "italic bold"), bg="#0E6DA5", width=10,
                    fg="black", relief=GROOVE, bd=5)
speed_label.place(x=400, y=0)

speed_scale = Scale(root, from_=0.2, to=5.0, resolution=0.2, length=200, digits=2, orient=HORIZONTAL,
                    font=("arial", 14, "italic bold"),
                    relief=GROOVE, bd=2, width=10)
speed_scale.place(x=520, y=0)

# bars window
canvas = Canvas(root, width=870, height=450, bg="black")
canvas.place(x=10, y=130)

root.mainloop()
