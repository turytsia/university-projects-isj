########################################################
# Project name: GUI for calculator
# Package: Calculator
# File: gui.py
# Date: 04.04.2022
# Last changes: 27.04.2022
# Author: Strelba do nohy (Aliaksei Klimau -- xklima34)
#########################################################
# @package Calculator
# @file gui.py
# @author Strelba do nohy (Aliaksei Klimau -- xklima34)
# @brief GUI for calculator
##########################################################
from glob import glob
import tkinter as tk
from tkinter import *


import input_output
import re




# @param string for input symbols 
calculation = ""


# @brief function adds symbol to calculation string 
# @param symbol - letter or number called by pushing the bottom
# @return of the push of the bottom write the symbol to the screen
def add_to_calculation(symbol):
    global calculation
    calculation = text_result.get(1.0, "end-1c")
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


# @brief function that saves result of calculation
# @return the function prints out
def evaluate_calculation(self):
    global calculation
    calculation = text_result.get(1.0, "end-1c")
    try:
        if input_output.check_brackets(calculation):
            clear_field()
            text_result.insert(1.0, "Error")
        else:
            calculation = "(" + calculation + ")"
            br=0
            for ind in calculation:
                if ind=="(":
                    br+=1
            result = input_output.brackets(calculation, br)
            if re.match(r' /', result):
                result = "-" + result[2:]
            else:
                result = result[1:]
            result = result[:-1]
            if re.search(r'\.', result):
                if result[-1]=="0":
                    result=re.sub(r'\.[0-9]+', '', result)
        calculation = result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

    return "break"

# @brief clears string with calculation


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    text_result.insert(1.0, "")
    pass

# @param window for interface
root = tk.Tk()
root.geometry("500x400")

# @brief row and column configure make buttons sreatchable
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)
text_result = tk.Text(root, height=2, width=22, font=("Arial", 24))
text_result.grid(columnspan=10, sticky="nswe")

tk.Grid.rowconfigure(root, 1, weight=1)
tk.Grid.columnconfigure(root, 1, weight=1)

tk.Grid.rowconfigure(root, 3, weight=1)
tk.Grid.columnconfigure(root, 3, weight=1)
tk.Grid.rowconfigure(root, 4, weight=1)
tk.Grid.columnconfigure(root, 4, weight=1)
tk.Grid.rowconfigure(root, 5, weight=1)
tk.Grid.columnconfigure(root, 5, weight=1)
tk.Grid.rowconfigure(root, 6, weight=1)
tk.Grid.columnconfigure(root, 6, weight=1)

# @brief buttons for numbers and symbols
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=3, column=1, sticky="nswe")
tk.Grid.rowconfigure(root, 2, weight=1)
tk.Grid.columnconfigure(root, 2, weight=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=3, column=2, sticky="nswe")
tk.Grid.rowconfigure(root, 3, weight=1)
tk.Grid.columnconfigure(root, 3, weight=1)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=3, column=3, sticky="nswe")
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=4, column=1, sticky="nswe")
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=4, column=2, sticky="nswe")
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=4, column=3, sticky="nswe")
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=5, column=1, sticky="nswe")
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=5, column=2, sticky="nswe")
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=5, column=3, sticky="nswe")
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=6, column=1, sticky="nswe")
btn_dot = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 14))
btn_dot.grid(row=6, column=2, sticky="nswe")
btn_left_parenthesis = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_left_parenthesis.grid(row=2, column=1, sticky="nswe")
btn_right_parenthesis = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_right_parenthesis.grid(row=2, column=2, sticky="nswe")

# @brief buttons for operations
btn_equal = tk.Button(root, text="=", command=lambda: evaluate_calculation(0), width=5, font=("Arial", 14), bg="#0098ED")
btn_equal.grid(row=6, column=3, sticky="nswe")

btn_clear = tk.Button(root, text="C", command=clear_field, width=6, font=("Arial", 14), bg='#CB0535')
btn_clear.grid(row=2, column=5, sticky="nswe")

btn_factorial = tk.Button(root, text="x!", command=lambda: add_to_calculation("!"), width=6, font=("Arial", 14))
btn_factorial.grid(row=3, column=5, sticky="nswe")

btn_log = tk.Button(root, text="log\u02E3", command=lambda: add_to_calculation("log"), width=6, font=("Arial", 14))
btn_log.grid(row=4, column=5, sticky="nswe")

btn_root = tk.Button(root, text="√", command=lambda: add_to_calculation("√"), width=5, font=("Arial", 14))
btn_root.grid(row=2, column=3, sticky="nswe")

btn_power = tk.Button(root, text="x\u02b8", command=lambda: add_to_calculation("^"), width=5, font=("Arial", 14))
btn_power.grid(row=2, column=4, sticky="nswe")

btn_devide = tk.Button(root, text="÷", command=lambda: add_to_calculation("÷"), width=5, font=("Arial", 14))
btn_devide.grid(row=3, column=4, sticky="nswe")

btn_multiplie = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_multiplie.grid(row=4, column=4, sticky="nswe")

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=5, column=4, sticky="nswe")

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=6, column=4, sticky="nswe")

# @param defines min size for calculator window
root.wm_minsize(400, 250)

# @param bind enter-key
root.bind('<Return>', evaluate_calculation)

root.mainloop()
######################################################################################################################################
#End of file gui.py