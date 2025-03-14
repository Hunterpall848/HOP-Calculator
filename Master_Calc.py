import tkinter as tk
import webbrowser as web
import os

calculation = ""

#Appends an Int or Op to the text row:

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete (1.0, "end")
    text_result.insert (1.0, calculation)
    secretbttn()


#Evaluates text in text row:

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "error")
    

#Clears text in text row:

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    secretbttn()

#Secret Button Call:

def secretbttn():
    global calculation
    if calculation == "80085":
        btnsecret.grid(row=6, column = 2)
    elif calculation == "69":
        btnsecret2.grid(row = 6, column = 2)
    else:
        btnsecret.grid_remove()
        btnsecret2.grid_remove()

#GUI creation:

root = tk.Tk()
root.geometry("300x265")
root.configure(background="grey")
root.title ("HOP Calculator")
root.iconbitmap("calc.ico")

#Upper text column:

text_result = tk.Text(root, height=2, width=16, font=("Arial",24))
text_result.grid(columnspan=5)



#Integer Buttons:

btn1 = tk.Button (root, text="1", command = lambda: add_to_calculation(1),
                  width = 5, font=("Ariel", 14), background="black", foreground="white")
btn1.grid(row = 2, column = 1)
btn2 = tk.Button (root, text="2", command = lambda: add_to_calculation(2),
                  width = 5, font=("Ariel", 14), background="black", foreground="white")
btn2.grid(row = 2, column = 2)
btn3 = tk.Button (root, text="3", command = lambda: add_to_calculation(3),
                  width = 5, font=("Ariel", 14), background="black", foreground="white")
btn3.grid(row = 2, column = 3)
btn4 = tk.Button (root, text="4", command = lambda: add_to_calculation(4),
                  width = 5, font=("Ariel", 14), background="black", foreground="white")
btn4.grid(row = 3, column = 1)
btn5 = tk.Button (root, text="5", command = lambda: add_to_calculation(5),
                  width = 5, font=("Ariel", 14), background="black", foreground="white")
btn5.grid(row = 3, column = 2)
btn6 = tk.Button (root, text="6", command = lambda: add_to_calculation(6),
                  width = 5, font=("Ariel", 14), background="black", foreground="white")
btn6.grid(row = 3, column = 3)
btn7 = tk.Button (root, text="7", command = lambda: add_to_calculation(7),
                  width = 5, font=("Ariel", 14), background="black", foreground="white")
btn7.grid(row = 4, column = 1)
btn8 = tk.Button (root, text="8", command = lambda: add_to_calculation(8),
                  width = 5, font=("Ariel", 14), background="black", foreground="white")
btn8.grid(row = 4, column = 2)
btn9 = tk.Button (root, text="9", command = lambda: add_to_calculation(9),
                  width = 5, font=("Ariel", 14), background="black", foreground="white")
btn9.grid(row = 4, column = 3)
btn0 = tk.Button (root, text="0", command = lambda: add_to_calculation(0),
                  width = 5, font=("Ariel", 14), background="black", foreground="white")
btn0.grid(row = 5, column = 2)

#Operation Buttons:

btnadd = tk.Button (root, text="+", command = lambda: add_to_calculation("+"),
                  width = 5, font=("Ariel", 14))
btnadd.grid(row = 2, column = 4)
btnsubtract = tk.Button (root, text="-", command = lambda: add_to_calculation("-"),
                  width = 5, font=("Ariel", 14))
btnsubtract.grid(row = 3, column = 4)
btnmult = tk.Button (root, text="*", command = lambda: add_to_calculation("*"),
                  width = 5, font=("Ariel", 14))
btnmult.grid(row = 4, column = 4)
btndiv = tk.Button (root, text="/", command = lambda: add_to_calculation("/"),
                  width = 5, font=("Ariel", 14))
btndiv.grid(row = 5, column = 4)
btnequal = tk.Button (root, text="=", command = lambda: evaluate_calculation(),
                  width = 5, font=("Ariel", 14))
btnequal.grid(row = 5, column = 3)
btnclear = tk.Button (root, text = "C", command = lambda: clear_field(), width = 5,
                    font = ("Ariel", 14))
btnclear.grid(row = 5, column = 1)

#Hidden Buttons:

btnsecret = tk.Button (root, text = "......", background= "orange", command = lambda: web.open ('https://www.pornhub.com/'), width = 5, font = ("Ariel", 10))
btnsecret.grid(row = 6, column = 2)
btnsecret.grid_remove()
btnsecret2 = tk.Button (root, text = "H31P M3", background= "red", command = lambda: web.open ('https://open.spotify.com/track/7DhcrTPFcGIccQ2cGc5Jbq'), width = 8, font = ("Ariel", 10))
btnsecret2.grid(row = 6, column = 2)
btnsecret2.grid_remove()


root.mainloop()