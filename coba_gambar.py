import tkinter as tk

jendela = tk.Tk()
jendela.title("Gambar Label - Davina Maharani")

logo = tk.PhotoImage(file='gambar/smkn9mail.png')
logo_label = tk.Label(image=logo)
logo_label.pack()
tk.mainloop()