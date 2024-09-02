import tkinter as tk

jendela = tk.Tk()
jendela.title("Tombol - Davina Maharani")

Button = tk.Button( 
    text = "Klik Saya!", 
    width = 20, 
    height = 10, 
    bg = "Red", 
    fg = "Black"
) 
Button.pack()
Button.mainloop()