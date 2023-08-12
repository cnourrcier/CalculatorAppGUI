# calculatorGUI.py

import tkinter as tk 

# Create the main window
window = tk.Tk()
window.title("Basic Calculator")

# Entry widget for user input
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4, pady=10)


# Function to update the entry widget with button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))


# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)


# Function to perform the calculation
def calculate():
    try:
        user_input = entry.get()
        result = eval(user_input)
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error")

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and layout buttons
for i, button_text in enumerate(buttons):
    button =tk.Button(window, text=button_text, command=lambda txt=button_text: button_click(txt))
    row = i // 4 + 1
    column = i % 4
    padx_val = 10
    pady_val = 5

    button.grid(row=row, column=column, padx=padx_val, pady=pady_val)


# Clear button
clear_button = tk.Button(window, text="C", command=clear)
clear_button.grid(row=5, column=0, padx=10, pady=5, columnspan=2)

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=5, column=2, padx=10, pady=5, columnspan=2)

# Label to display the result
result_label = tk.Label(window, text="")
result_label.grid(row=6, column=0, columnspan=4, pady=10)

# Run the GUI event loop
window.mainloop()