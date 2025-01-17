"""
import sys
import math
import random
import threading
import time
import re
import sqlite3
import csv
"""

from tkinter import *
from tkinter import ttk


class Calculator:
    calc_value = 0.0
    div_trigger = False
    multi_trigger = False
    add_trigger = False
    sub_trigger = False

    def button_press(self, value):
        if value == " ":
            entry_val = ''
        else:
            entry_val = self.number_entry.get()
            entry_val += value
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, entry_val)

    @staticmethod
    def is_float(str_val):
        try:
            float(str_val)
            return True
        except ValueError:
            return False

    def math_button_press(self, value):
        if self.is_float(str(self.number_entry.get())):
            self.add_trigger = False
            self.sub_trigger = False
            self.multi_trigger = False
            self.div_trigger = False
            self.calc_value = float(self.entry_value.get())
            if value == "/":
                print("/ Pressed")
                self.div_trigger = True
            elif value == "*":
                print("* Pressed")
                self.multi_trigger = True
            elif value == "+":
                print("+ Pressed")
                self.add_trigger = True
            else:
                print("- Pressed")
                self.sub_trigger = True

            self.number_entry.delete(0, "end")

    def equal_button_press(self):
        if self.add_trigger or self.sub_trigger or self.multi_trigger or self.div_trigger:
            if self.add_trigger:
                solution = self.calc_value + float(self.entry_value.get())
            elif self.sub_trigger:
                solution = self.calc_value - float(self.entry_value.get())
            elif self.multi_trigger:
                solution = self.calc_value * float(self.entry_value.get())
            else:
                solution = self.calc_value / float(self.entry_value.get())

            print(self.calc_value, " ", float(self.entry_value.get()), " ", solution)
            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, solution)

    def __init__(self, root):
        print("Hello")
        self.entry_value = StringVar(root, value="")
        root.title("Calculator")
        root.geometry("830x285")
        root.resizable(width=True, height=True)
        style = ttk.Style()
        style.configure("TButton",
                        font="Serif 18",
                        padding=10)

        style.configure("TEntry",
                        font="Serif 18",
                        padding=10)
        self.number_entry = ttk.Entry(root,
                                      textvariable=self.entry_value, width=50)
        self.number_entry.grid(row=0, columnspan=4)

        # ---------1st row ----------
        self.button7 = ttk.Button(root, text="7", command=lambda: self.button_press('7')).grid(row=1, column=0)
        self.button8 = ttk.Button(root, text="8", command=lambda: self.button_press('8')).grid(row=1, column=1)
        self.button9 = ttk.Button(root, text="9", command=lambda: self.button_press('9')).grid(row=1, column=2)
        self.button_div = ttk.Button(root, text="/", command=lambda: self.math_button_press('/')).grid(row=1, column=3)

        # ---------2nd row ----------
        self.button4 = ttk.Button(root, text="4", command=lambda: self.button_press('4')).grid(row=2, column=0)
        self.button5 = ttk.Button(root, text="5", command=lambda: self.button_press('5')).grid(row=2, column=1)
        self.button6 = ttk.Button(root, text="6", command=lambda: self.button_press('6')).grid(row=2, column=2)
        self.button_multi = ttk.Button(
            root, text="*", command=lambda: self.math_button_press('*')
        ).grid(row=2, column=3)

        # ---------3rd row ----------
        self.button1 = ttk.Button(root, text="1", command=lambda: self.button_press('1')).grid(row=3, column=0)
        self.button2 = ttk.Button(root, text="2", command=lambda: self.button_press('2')).grid(row=3, column=1)
        self.button3 = ttk.Button(root, text="3", command=lambda: self.button_press('3')).grid(row=3, column=2)
        self.button_add = ttk.Button(root, text="+", command=lambda: self.math_button_press('+')).grid(row=3, column=3)

        # ---------4th row ----------
        self.button_clear = ttk.Button(root, text="AC", command=lambda: self.button_press(' ')).grid(row=4, column=0)
        self.button0 = ttk.Button(root, text="0", command=lambda: self.button_press('0')).grid(row=4, column=1)
        self.button_equal = ttk.Button(root, text="=", command=lambda: self.equal_button_press()).grid(row=4, column=2)
        self.button_sub = ttk.Button(root, text="-", command=lambda: self.math_button_press('-')).grid(row=4, column=3)


main_root = Tk()
calc = Calculator(main_root)
main_root.mainloop()
