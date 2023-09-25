import tkinter as tk
# Define the main window for the calculator
window = tk.Tk()
window.title("Calculator")
# Define the display for the calculator
display = tk.Entry(window, width=30)
display.grid(row=0, column=0, columnspan=4)
# Define the buttons for the calculator
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]
# Create a function to handle button clicks
def button_click(button):
    if button == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, button)
# Add the buttons to the window
for row in range(4):
    for column in range(4):
        tk.Button(window, text=buttons[row][column], command=lambda b=buttons[row][column]: button_click(b)).grid(row=row+1, column=column)
# Start the main loop for the calculator
window.mainloop()