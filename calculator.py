import tkinter as tk

root = tk.Tk()
root.title("Kalkulator")
root.geometry("320x450")
root.resizable(False, False)

# Layar input
entry = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=10
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Fungsi tombol
def klik(teks):
    entry.insert(tk.END, teks)

def hasil():
    try:
        hasilnya = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(hasilnya))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

# Tombol kalkulator
tombol = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for i, row in enumerate(tombol):
    for j, item in enumerate(row):

        if item == "=":
            cmd = hasil
        else:
            cmd = lambda x=item: klik(x)

        btn = tk.Button(
            root,
            text=item,
            font=("Arial", 20),
            command=cmd,
            width=5,
            height=2
        )

        btn.grid(row=i+1, column=j, sticky="nsew")

# Tombol clear
clear_btn = tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 18),
    command=clear
)

clear_btn.grid(row=5, column=0, columnspan=4, sticky="nsew")

# Biar semua tombol sama besar
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()