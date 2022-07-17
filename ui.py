from tkinter import *

WIDTH = 10
HEIGHT = 5

NUMBERS = "0123456789."
OPERATORS = "+-*/"


class UI:
    def __init__(self):
        self.first_num = ""
        self.operator = ""
        self.second_num = ""

        # Window
        self.window = Tk()
        self.window.title("Calculator")
        self.window.config(width=400, height=600)

        self.window.bind("<KeyPress>", self.on_key)

        # Label
        self.user_entry = Label(text=self.first_num, width=int(WIDTH * 4.5), height=HEIGHT, bg="grey", fg="white")
        self.user_entry.grid(row=0, column=0, columnspan=4)

        # Numbers Buttons
        self.zero_button = Button(text="0", width=int(WIDTH * 2.2), height=HEIGHT)
        self.zero_button.grid(row=5, column=0, columnspan=2)

        self.decimal_button = Button(text=".", width=WIDTH, height=HEIGHT)
        self.decimal_button.grid(row=5, column=2)

        self.one_button = Button(text="1", width=WIDTH, height=HEIGHT)
        self.one_button.grid(row=4, column=0)

        self.two_button = Button(text="2", width=WIDTH, height=HEIGHT)
        self.two_button.grid(row=4, column=1)

        self.three_button = Button(text="3", width=WIDTH, height=HEIGHT)
        self.three_button.grid(row=4, column=2)

        self.four_button = Button(text="4", width=WIDTH, height=HEIGHT)
        self.four_button.grid(row=3, column=0)

        self.five_button = Button(text="5", width=WIDTH, height=HEIGHT)
        self.five_button.grid(row=3, column=1)

        self.six_button = Button(text="6", width=WIDTH, height=HEIGHT)
        self.six_button.grid(row=3, column=2)

        self.seven_button = Button(text="7", width=WIDTH, height=HEIGHT)
        self.seven_button.grid(row=2, column=0)

        self.height_button = Button(text="8", width=WIDTH, height=HEIGHT)
        self.height_button.grid(row=2, column=1)

        self.nine_button = Button(text="9", width=WIDTH, height=HEIGHT)
        self.nine_button.grid(row=2, column=2)

        # Operators Buttons
        self.divide_button = Button(text="÷", width=WIDTH, height=HEIGHT, bg="orange", fg="white")
        self.divide_button.grid(row=1, column=3)

        self.multiplication_button = Button(text="×", width=WIDTH, height=HEIGHT, bg="orange", fg="white")
        self.multiplication_button.grid(row=2, column=3)

        self.minus_button = Button(text="-", width=WIDTH, height=HEIGHT, bg="orange", fg="white")
        self.minus_button.grid(row=3, column=3)

        self.plus_button = Button(text="+", width=WIDTH, height=HEIGHT, bg="orange", fg="white")
        self.plus_button.grid(row=4, column=3)

        self.equal_button = Button(text="=", width=WIDTH, height=HEIGHT, bg="orange", fg="white")
        self.equal_button.grid(row=5, column=3)

        # Other Buttons
        self.reset_button = Button(text="AC", width=WIDTH, height=HEIGHT)
        self.reset_button.grid(row=1, column=0)

        self.more_or_less_button = Button(text="+/-", width=WIDTH, height=HEIGHT)
        self.more_or_less_button.grid(row=1, column=1)

        self.percent_button = Button(text="%", width=WIDTH, height=HEIGHT)
        self.percent_button.grid(row=1, column=2)

        self.window.mainloop()

    def on_key(self, event):
        if event.char in OPERATORS and len(self.second_num) == 0:
            self.operator = event.char
        if event.char in NUMBERS:
            if len(self.operator) == 0:
                self.first_num += event.char
                self.user_entry.config(text=self.first_num)
            else:
                self.second_num += event.char
                self.user_entry.config(text=self.second_num)
