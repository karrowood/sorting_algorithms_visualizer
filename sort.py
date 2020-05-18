# Kyle Arrowood
# 5/17/2020
# A sorting visualizer
# This program will show how different sorting algorithms work on an unsorted
# list of random numbers. The user will select the algorithm and the amount of
# numbers to be sorted.

from tkinter import *
import random


class window:
    def __init__(self, screen, canvas_width, canvas_height):
        self.screen = screen
        self.width = canvas_width
        self.height = canvas_height
    def create_visual(self, array):
        displacement = 0 # Used to move over the bars the correct amount
        move = self.width // len(array) # Amount to move over each time
        for i in range(len(array)):
            self.canvas.create_rectangle(displacement, self.height, displacement + move, array[i], fill = "white")
            displacement = displacement + move
    def create_rand_list(self, list_size):
        result = []
        minimum = 10
        for i in range(list_size):
            result.append(random.randrange(minimum, self.height))
        return result
    def refresh(self, array):
        self.canvas.delete("all")
        self.create_visual(array)
    def create_window(self):
        self.screen.title("Sorting Algorithm Visualizer")
        spin_variable = IntVar()
        spin_variable.set(100)
        spin = Spinbox(self.screen, textvariable = spin_variable, from_ = 5, to = 500)
        #algorithms = ["Insertion Sort", "Quick Sort", "Bubble Sort", "Merge Sort"]
        option_variable = StringVar()
        option_variable.set("Insertion Sort")
        option_menu = OptionMenu(self.screen, option_variable,
                                "Insertion Sort", "Quick Sort", "Bubble Sort",
                                "Merge Sort")
        def button_callback():
            array = self.create_rand_list(int(spin.get()))
            self.refresh(array)
            #pass
        go_button = Button(self.screen, text = "GO!", command = button_callback)
        label = Label(self.screen, text = "Amount of items:\n(MAX: 500)")
        label.place(x = 300, y = 10)
        spin.place(x = 400, y = 12)
        option_menu.place(x = 550, y = 7)
        go_button.place(x = 675, y = 9)
        self.canvas = Canvas(self.screen, bg = "black", width = self.width, height = self.height)
        #array = self.create_rand_list(100)
        #self.refresh(array)
        self.canvas.place(x = 3, y = 50)
        self.screen.mainloop()

def main():
    screen = Tk()
    screen.geometry("1010x565")
    gui = window(screen, 1000, 500)
    gui.create_window()


main()