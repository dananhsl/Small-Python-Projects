from tkinter import *

window = Tk()
window.title("Miles - Km Converter")
window.minsize(width=600, height=300)
choose = Label(text="Please choose your type of conversion below:", font=("Times New Roman", 10),)
choose.grid(column=0, row=0)
error_message = Label(text="This is not a number.", font=("Times New Roman", 10))


def button_clicked():
    try:
        int(user_input.get())
        if radio_state.get() == 2:
            result["text"] = str(int(user_input.get()) / float(1.6))
        else:
            result["text"] = str(int(user_input.get()) * float(1.6))
    except ValueError:
        error_message.grid(column=3, row=17,)


my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(column=3, row=15, padx=30, pady=20)
equals = Label(text="equals")
equals.grid(column=1, row=11)
result = Label(text=0, font=("Times New Roman", 15))
result.grid(column=3, row=11, padx=30)
kilometer = Label(text="Km", font=("Times New Roman", 15))
kilometer.grid(column=4, row=11)
miles = Label(text="Miles", font=("Times New Roman", 15))
miles.grid(column=4, row=10)
user_input = Entry()
user_input.config(font=("Times New Roman", 16), width=5)
user_input.grid(column=3, row=10, padx=30, pady=20)


def radio_used():
    if radio_state.get() == 2:
        kilometer["text"] = "Miles"
        miles["text"] = "Km"
    else:
        kilometer["text"] = "Km"
        miles["text"] = "Miles"
    print(radio_state.get())


radio_state = IntVar()
radio_button_1 = Radiobutton(text="Miles to Km", value= 1, variable=radio_state, command=radio_used)
radio_button_2 = Radiobutton(text="Km to Miles", value= 2, variable=radio_state, command=radio_used)
radio_button_1.grid(column=0, row=1)
radio_button_2.grid(column=0, row=2)


window.mainloop()