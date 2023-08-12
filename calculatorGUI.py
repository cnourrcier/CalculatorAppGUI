# calculatorGUI.py

import tkinter as tk 

# Create the main window
window = tk.Tk()
window.title("Basic Calculator")

# Entry widget for user input
entry = tk.Entry(window, width=40)
entry.pack(pady=20)

# Function to perform the calculation
def calculate():
    try:
        user_input = entry.get()
        result = eval(user_input)
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error")

# Button for calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Label to display the result
result_label = tk.Label(window, text="")
result_label.pack(pady=20)

# Run the GUI event loop
window.mainloop()