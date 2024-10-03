import tkinter as tk

def button(frame, text, row=None, column=None, padx=None, pady=None, colspan=None, columnspan=None, command=None):
    button = tk.Button(frame, text=text, command=command)
    button.grid(row=row, column=column, padx=padx, pady=pady, colspan=colspan, columnspan=columnspan)
    return button

def input_entry(frame, row=None, column=None, padx=None, pady=None, show=None):
    entry = tk.Entry(frame, show=show)
    entry.grid(row=row, column=column, padx=padx, pady=pady)
    return entry

def label(frame, text, font=None, row=None, column=None, padx=None, pady=None, columnspan=None):
    label = tk.Label(frame, text=text, font=font)
    label.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan)
    return label