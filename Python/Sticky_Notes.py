import tkinter as tk


def cli():
    import time
    current_time = time.strftime("%H:%M")
  
    print("Welcome to Sticky Notes Application.")
    time.sleep(2)
    note_input = input("Type important notes here: ")
    note = ("%s") % note_input
    time.sleep(1)
   
    root = tk.Tk()
    root.title("Sticky_Notes")
    root.geometry("500x500")
    root.configure(background='pink')

    tk.Label(root, text=current_time, background = 'pink').pack()
  
    tk.Label(root, text=note , background = 'pink').pack()

    root.mainloop()

cli()

