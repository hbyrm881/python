import tkinter as tk
import math

x = 0
def yaz_1():
    entry.insert(tk.END,"1")



pencere = tk.Tk()
pencere.title("Hesap Makinasi")
pencere.geometry("400x500")

entry = tk.Entry(pencere,width=20,font=("Arial",18))
entry.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

buton1 = tk.Button(pencere, text="1", width=5, height=1, font=("Arial", 18), command=yaz_1)
buton1.grid(row=1, column=0)



pencere.mainloop()