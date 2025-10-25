import tkinter

import math

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0",".","√", "="],
    ["^","sin°", "cos°", "tan°"],
    ["ln", "log", "π", "del"]
]

right_symbols = ["÷", "x", "-", "+", "=","^"]
top_symbols = ["AC", "+/-", "%","√","sin°", "cos°","tan°", "ln","log","π","del"]

row_count = len(button_values)
column_count = len(button_values[0])
color_green = "#27907A"
color_white = "#FCFEFC"
color_red = "#FF0018"
color_black = "#111111"


window = tkinter.Tk()
window.title("Armin's Calculator")
window.resizable(False,False)

 
frame = tkinter.Frame(window)
label = tkinter.Label(frame, text= "0", font=("Arial", 45), background= color_green, 
                      foreground= color_white, anchor="w", width= column_count)

label.grid(row = 0, column=0, columnspan=column_count, sticky="we")
for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text = value, font=("Arial", 30),
                                width= column_count - 1, height= 1,
                                command= lambda value = value: button_clicked(value) )
        if value in top_symbols:
            button.config(foreground=color_green, background=color_black)
        elif value in right_symbols:
            button.config(foreground= color_green, background= color_black)
        else:
            button.config(foreground= color_green, background= color_black)
        button.grid(row=row+1, column = column)

frame.pack()

A = "0"
Operator = None
B = None

def clear_all():
    global A, B, Operator
    A = "0"
    Operator = None
    B = None

def remove_zero_decimal(num):

    if num % 1 == 0:
        num = int(num)
    return str(num)

def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, Operator

    if value in right_symbols:
        if value == "=":
            if A is not None and Operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)
                if Operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif Operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif Operator == "x":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif Operator == "÷":
                    if numB == 0:
                        label["text"] = "Error"
                    else:
                        label["text"] = remove_zero_decimal(numA / numB)
                elif Operator == "√":
                    if numA < 0:
                        label["text"] = "Error" 
                    else:
                        label["text"] = remove_zero_decimal(numA ** 0.5)  
                elif Operator == "^":

                    label["text"] = remove_zero_decimal(numA ** numB)
                
                
                
                
                clear_all()

        elif value in "+-x÷^":
            if Operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"


            Operator = value

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
        elif value == "√":
            num = float(label["text"])
            if num < 0:
                 label["text"] = "Error"
            else:
                result = float(label["text"]) ** 0.5
                label["text"] = remove_zero_decimal(result)
        elif value == "sin°":
                result = math.sin(math.radians(float(label["text"])))
                label["text"] = remove_zero_decimal(result)
        elif value == "cos°":
                result = math.cos(math.radians(float(label["text"])))
                label["text"] = remove_zero_decimal(result)
        elif value == "tan°":
                    num = float(label["text"])
                    if num % 180 == 90:
                        label["text"] = "Error"
                    else:
                        result = math.tan(math.radians(float(label["text"])))
                        if abs(result) < 1e-10:
                            result = 0
                        label["text"] = remove_zero_decimal(result)
        elif value == "ln":
                num = float(label["text"])
                if num <= 0:
                    label["text"] = "Error"
                else:
                    result = math.log(float(label["text"]))
                    label["text"] = remove_zero_decimal(result)
        elif value == "log":
            num = float(label["text"])
            if num <= 0:
                    label["text"] = "Error"
            else:
                result = math.log10(float(label["text"]))
                label["text"] = remove_zero_decimal(result)
        elif value == "π":
                result = 3.141592653589793
                (label["text"]) = remove_zero_decimal(result)

        elif value == "del":
            text = label["text"]
            if len(text) > 1:
                        label["text"] = text[:-1]
            else:
                        label["text"] = "0"
             
             
                
    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value

        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value

        

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()