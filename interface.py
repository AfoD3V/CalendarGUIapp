from tkinter import *

root = Tk()
root.title("Simple Menu")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#e.insert(0, "")




def button_add():
    return

new_event_button = Button(root, text="New event", padx=40, pady=20, command=button_add)









root.mainloop()
