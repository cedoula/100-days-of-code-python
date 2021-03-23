#This program uses tkinter library to make a mile to km converter GUI
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400,height=150)
window.config(padx=20, pady=20)

#Labels
miles_label = Label(text="Miles", font=("Arial", 24))
miles_label.grid(column=2, row=0)
label1 = Label(text="is equal to", font=("Arial", 24))
label1.grid(column=0, row=1)
km_label= Label(text="0", font=("Arial", 24))
km_label.grid(column=1, row=1)
label2 = Label(text="Km", font=("Arial", 24))
label2.grid(column=2, row=1)

def button_clicked():
    km_label["text"] = "{:.1f}".format(float(miles_input.get()) * 1.609)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entry
miles_input = Entry()
miles_input.config(width=10, justify="center", font=("Arial", 24))
miles_input.grid(column=1,row=0)





window.mainloop()