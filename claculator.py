
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("My Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#0B0B0C")

# Display
expression = ""

display = tk.Entry(
    root,
    font=("Arial", 25),
    bg="#303134",
    fg="white",
    justify="right",
    bd=0
)
display.pack(fill="both", padx=15, pady=20, ipady=20)


# Button functions
def press(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

# Create button frame
frame = tk.Frame(root, bg="#202124")
frame.pack(expand=True, fill="both", padx=10, pady=10)

for row_index, row in enumerate(buttons):
    for col_index, char in enumerate(row):

        if char == "=":
            command = calculate
            color = "#34A853"
        elif char in ["+", "-", "*", "/"]:
            command = lambda x=char: press(x)
            color = "#4285F4"
        else:
            command = lambda x=char: press(x)
            color = "#3C4043"

        button = tk.Button(
            frame,
            text=char,
            font=("Arial", 20, "bold"),
            bg=color,
            fg="white",
            activebackground="#5F6368",
            bd=0,
            command=command
        )

        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=5,
            pady=5
        )

# Clear button
clear_button = tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 16, "bold"),
    bg="#EA4335",
    fg="white",
    bd=0,
    command=clear
)
clear_button.pack(fill="x", padx=15, pady=10, ipady=10)

# Make buttons expand
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
    frame.grid_rowconfigure(i, weight=1)

# Run application
root.mainloop()
