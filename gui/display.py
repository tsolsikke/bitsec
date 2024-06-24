import tkinter as tk
from ..core.py.cpp_wrapper import func_001, func_002

def display_info():
    val1 = int(entry1.get())
    val2 = int(entry2.get())
    result = func_001(val1, val2)
    func_002(f"The sum of {val1} and {val2} is {result}")
    result_label.config(text=f"Result: {result}")

root = tk.Tk()
root.title("BitSec GUI")

tk.Label(root, text="Value 1").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Value 2").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

tk.Button(root, text="Calculate", command=display_info).pack(pady=20)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=5)

root.mainloop()
