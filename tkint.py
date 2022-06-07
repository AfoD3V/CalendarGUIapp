from tkinter import *


# key down
def click():
    entered_text = textentry.get()
    output.delete(0.0, END)
    if len(entered_text) > 0:
        test = entered_text
    else:
        test = "hola amigo"
    output.insert(END, test)


# Main
window = Tk()
window.title("Kalendarz")
window.configure(background="black")

# create label
Label(window, text="New Event: ", bg="black", fg="blue", font="none 12 bold").grid(row=1, column=0, sticky=W)

# text entry box
textentry = Entry(window, width=82, bg="white")
textentry.grid(row=1, column=1, sticky=W)

# submit button
Button(window, text="SUBMIT", width=0, command=click).grid(row=3, column=0, sticky=W)

# another label
Label(window, text="\nDefinition:", bg="black", fg="white", font="none 12 bold").grid(row=4, column=0, sticky=W)
# text box
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

# dictionary
my_compdictionary = {

}

# Run main loop
window.mainloop()
