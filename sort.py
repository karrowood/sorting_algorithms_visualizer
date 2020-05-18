# Kyle Arrowood
# 5/18/2020
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
    def create_visual(self):
        displacement = 0 # Used to move over the bars the correct amount
        move = self.width // len(self.array) # Amount to move over each time
        for i in range(len(self.array)):
            self.canvas.create_rectangle(displacement, self.height, displacement + move, self.array[i], fill = "white")
            displacement = displacement + move
    def create_rand_list(self, list_size):
        result = []
        minimum = 10
        for i in range(list_size):
            result.append(random.randrange(minimum, self.height))
        return result
    def refresh(self):
        self.canvas.delete("all")
        self.create_visual()
        self.canvas.update()
    
    def create_window(self):
        self.screen.title("Sorting Algorithm Visualizer")
        spin_variable = IntVar()
        spin_variable.set(100)
        def spin_callback():
            self.array = self.create_rand_list(int(spin.get()))
            self.refresh()
        spin = Spinbox(self.screen, textvariable = spin_variable, from_ = 5, to = 500, command = spin_callback)
        #algorithms = ["Insertion Sort", "Quick Sort", "Bubble Sort", "Merge Sort"]
        option_variable = StringVar()
        option_variable.set("Insertion Sort")
        option_menu = OptionMenu(self.screen, option_variable,
                                "Insertion Sort", "Quick Sort", "Bubble Sort",
                                "Merge Sort")
        def button_callback():
            #self.array = self.create_rand_list(int(spin.get()))
            if option_variable.get() == "Insertion Sort":
                insertion_sort(self)
            elif option_variable.get() == "Quick Sort":
                pass
            elif option_variable.get() == "Bubble Sort":
                bubble_sort(self)
            elif option_variable.get() == "Merge Sort":
                pass
            # Add Part that changes color
        go_button = Button(self.screen, text = "GO!", command = button_callback)
        label = Label(self.screen, text = "Amount of items:\n(MAX: 500)")
        label.place(x = 300, y = 10)
        spin.place(x = 400, y = 12)
        option_menu.place(x = 550, y = 7)
        go_button.place(x = 675, y = 9)
        self.canvas = Canvas(self.screen, bg = "black", width = self.width, height = self.height)
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
        time.sleep(0.01)
        window.refresh()
def quick_sort(window):
    pass
def bubble_sort(window):
    for i in range(len(window.array) - 1):
        for j in range(len(window.array) - i - 1):
            if window.array[j] < window.array[j + 1]:
                temp = window.array[j]
                window.array[j] = window.array[j + 1]
                window.array[j + 1] = temp
            time.sleep(0.01)
            window.refresh()



def main():
    screen = Tk()
    screen.geometry("1010x565")
    gui = window(screen, 1000, 500)
    gui.create_window()


main()
