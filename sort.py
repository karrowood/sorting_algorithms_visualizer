# Kyle Arrowood
# 6/8/2020
# A sorting visualizer
# This program will show how different sorting algorithms work on an unsorted
# list of random numbers. The user will select the algorithm and the amount of
# numbers to be sorted.

from tkinter import *
import random
import time

class window:
    def __init__(self, screen, canvas_width, canvas_height):
        self.screen = screen
        self.width = canvas_width
        self.height = canvas_height
    def create_visual(self, color):
        displacement = 0 # Used to move over the bars the correct amount
        move = self.width // len(self.array) # Amount to move over each time
        for i in range(len(self.array)):
            self.canvas.create_rectangle(displacement, self.height,
                            displacement + move, self.array[i], fill = color)
            displacement = displacement + move
    def create_rand_list(self, list_size):
        result = []
        minimum = 10
        for i in range(list_size):
            result.append(random.randrange(minimum, self.height))
        return result
    def refresh(self):
        self.canvas.delete("all")
        self.create_visual("red")
        self.canvas.update()
    def create_window(self):
        self.screen.title("Sorting Algorithm Visualizer")
        spin_variable = IntVar()
        spin_variable.set(100)
        def spin_callback():
            self.array = self.create_rand_list(int(spin.get()))
            self.refresh()
        spin = Spinbox(self.screen, textvariable = spin_variable, from_ = 5,
                    to = 500, command = spin_callback)
        option_variable = StringVar()
        option_variable.set("Insertion Sort")
        option_menu = OptionMenu(self.screen, option_variable,
                                "Insertion Sort", "Quick Sort", "Bubble Sort",
                                "Merge Sort", "Shell Sort", "Selection Sort",
                                "Heap Sort")
        option_menu.config(bg = "yellow")
        def button_callback():
            go_button["state"] = DISABLED
            generate_button["state"] = DISABLED
            spin["state"] = DISABLED
            option_menu["state"] = DISABLED
            if option_variable.get() == "Insertion Sort":
                insertion_sort(self)
            elif option_variable.get() == "Quick Sort":
                quick_sort(self, 0, len(self.array) - 1)
            elif option_variable.get() == "Bubble Sort":
                bubble_sort(self)
            elif option_variable.get() == "Merge Sort":
                merge_sort(self, 0, len(self.array) - 1)
            elif option_variable.get() == "Shell Sort":
                shell_sort(self)
            elif option_variable.get() == "Selection Sort":
                selection_sort(self)
            elif option_variable.get() == "Heap Sort":
                heap_sort(self)
            self.refresh()
            self.create_visual("green")
            go_button["state"] = "normal"
            generate_button["state"] = "normal"
            spin["state"] = "normal"
            option_menu["state"] = "normal"
        go_button = Button(self.screen, text = "GO!", command = button_callback,
                        bg = "yellow", activebackground = "white")
        def generate_cb():
            self.array = self.create_rand_list(int(spin.get()))
            self.refresh()
        generate_button = Button(self.screen, text = "Generate New List",
                        command = generate_cb, bg = "yellow",
                        activebackground = "white")
        label = Label(self.screen, text = "Amount of items:\n(MAX: 500)")
        generate_button.place(x = 180, y = 9)
        label.place(x = 300, y = 10)
        spin.place(x = 400, y = 12)
        option_menu.place(x = 550, y = 7)
        go_button.place(x = 675, y = 9)
        self.canvas = Canvas(self.screen, width = self.width, height = self.height)
        self.array = self.create_rand_list(100)
        self.refresh()
        self.canvas.place(x = 3, y = 50)
        self.screen.mainloop()

def insertion_sort(window):
    for i in range(1, len(window.array)):
        temp = window.array[i]
        j = i - 1
        while (j >= 0 and window.array[j] < temp):
            window.array[j + 1] = window.array[j]
            j -= 1
        window.array[j + 1] = temp
        time.sleep(0.05)
        window.refresh()
def quick_sort(window, low, high):
    if low < high:
        # Partition
        pi = window.array[high]
        i = low - 1
        for j in range(low, high):
            if window.array[j] > pi:
                i += 1
                window.array[i], window.array[j] = window.array[j], window.array[i]
                window.refresh()
        window.array[i + 1], window.array[high] = (window.array[high],
                                                    window.array[i + 1])
        partition = i + 1
        quick_sort(window, low, partition - 1)
        quick_sort(window, partition + 1, high)
def bubble_sort(window):
    for i in range(len(window.array) - 1):
        for j in range(len(window.array) - i - 1):
            if window.array[j] < window.array[j + 1]:
                window.refresh()
                window.array[j], window.array[j + 1] = (window.array[j + 1],
                                                        window.array[j])
def merge_sort(window, low, high):
    if low < high:
        middle = (low + high) // 2
        merge_sort(window, low, middle)
        merge_sort(window, middle + 1, high)
        # Merge
        i = low 
        j = middle + 1
        temp_arr = []   
        while i <= middle and j <= high:   
            if window.array[i] > window.array[j]: 
                temp_arr.append(window.array[i]) 
                i += 1
            else: 
                temp_arr.append(window.array[j]) 
                j += 1
        while i <= middle:   
            temp_arr.append(window.array[i]) 
            i += 1
        while j <= high:  
            temp_arr.append(window.array[j]) 
            j += 1
        j = 0       
        for i in range(low, high + 1):   
            window.array[i] = temp_arr[j] 
            j += 1 
            window.refresh()
def shell_sort(window):
    gap = len(window.array) // 2
    while gap > 0:
        for i in range(gap, len(window.array)):
            temp = window.array[i]
            j = i
            while (j >= gap and window.array[j - gap] < temp):
                window.array[j] = window.array[j - gap]
                j -= gap
            window.array[j] = temp
            window.refresh()
        gap = gap // 2
def selection_sort(window):
    for i in range(len(window.array) - 1):
        low = i
        for j in range(i + 1, len(window.array)):
            if window.array[j] > window.array[low]:
                low = j
        window.array[low], window.array[i] = window.array[i], window.array[low]
        time.sleep(0.04)
        window.refresh()
# Helper function to be used along with heap_sort()
def heap(array, length, num):
    high = num
    left = (2 * num) + 1
    right = (2 * num) + 2
    if left < length and array[left] < array[high]:
        high = left
    if right < length and array[right] < array[high]:
        high = right
    if not high == num:
        array[num],array[high] = array[high], array[num]
        heap(array, length, high)
def heap_sort(window):
    for i in range(len(window.array) // 2 - 1, -1, -1):
        heap(window.array, len(window.array), i)
        window.refresh()
    for i in range(len(window.array) - 1, 0, -1):
        window.array[0], window.array[i] = window.array[i], window.array[0]
        heap(window.array, i, 0)
        window.refresh()

def main():
    screen = Tk()
    screen.geometry("1010x565")
    gui = window(screen, 1000, 500)
    gui.create_window()

main()
