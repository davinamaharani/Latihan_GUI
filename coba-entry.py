import tkinter as tk

jendela = tk.Tk()
jendela.title("Entry - Davina Maharani")

tk.Label(text="Nama Depan").grid(row=0) 
tk.Label(text="Nama Belakang").grid(row=1)

e1 = tk.Entry() 
e2 = tk.Entry()
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1)

def show(): 
  tk.Label(text=e1.get()).grid(row=3,column=0) 
  tk.Label(text=e2.get()).grid(row=3,column=1 )
  
e1 = tk.Entry() 
e2 = tk.Entry() 
b1 = tk.Button(text="show", command=show)
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
b1.grid(row=2, column=1)
tk.mainloop()