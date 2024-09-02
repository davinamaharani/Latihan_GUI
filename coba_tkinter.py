import tkinter as tk

jendela = tk.Tk()
jendela.title("Hallo - Davina Maharani")
label = tk.Label(text="Hallo Davina", fg='White', bg='Black') 
label.pack()
nama = tk.Label(text="Kamu Umur Berapa", fg='Green', bg='Yellow')
nama.pack()
label.mainloop()