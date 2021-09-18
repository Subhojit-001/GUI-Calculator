from tkinter import *

def click(event):
    global input_text
    text = event.widget.cget("text")
    if text == "=":
        if input_text.get().isdigit():
            value = int(input_text.get())
        else:
            try:
                value = eval(input_text.get())

            except Exception as e:
                print(e)
                value = "Error"

        input_text.set(value)
        input_field.update()

    elif text == "C":
        input_text.set("")
        input_field.update()

    else:
        input_text.set(input_text.get() + text)
        input_field.update()

root = Tk()
root.geometry("312x324")
root.resizable(0, 0)
root.title("Calculator by Subhojit")
root.wm_iconbitmap("1.ico")

input_text = StringVar()
input_text.set("")

input_frame = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()

# first row

clear = Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",)
clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
clear.bind("<Button-1>", click)

divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
divide.grid(row=0, column=3, padx=1, pady=1)
divide.bind("<Button-1>", click)

# second row

seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
seven.grid(row=1, column=0, padx=1, pady=1)
seven.bind("<Button-1>", click)

eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
eight.grid(row=1, column=1, padx=1, pady=1)
eight.bind("<Button-1>", click)

nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
nine.grid(row=1, column=2, padx=1, pady=1)
nine.bind("<Button-1>", click)

multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
multiply.grid(row=1, column=3, padx=1, pady=1)
multiply.bind("<Button-1>", click)

# third row

four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
four.grid(row=2, column=0, padx=1, pady=1)
four.bind("<Button-1>", click)

five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
five.grid(row=2, column=1, padx=1, pady=1)
five.bind("<Button-1>", click)

six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
six.grid(row=2, column=2, padx=1, pady=1)
six.bind("<Button-1>", click)

minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
minus.grid(row=2, column=3, padx=1, pady=1)
minus.bind("<Button-1>", click)

# fourth row

one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
one.grid(row=3, column=0, padx=1, pady=1)
one.bind("<Button-1>", click)

two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
two.grid(row=3, column=1, padx=1, pady=1)
two.bind("<Button-1>", click)

three =Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
three.grid(row=3, column=2, padx=1, pady=1)
three.bind("<Button-1>", click)

plus =Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
plus.grid(row=3, column=3, padx=1, pady=1)
plus.bind("<Button-1>", click)

# fourth row

zero = Button(btns_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
zero.grid(row=4, column=0, padx=1, pady=1)
zero.bind("<Button-1>", click)

dzero = Button(btns_frame, text="00", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
dzero.grid(row=4, column=1, padx=1, pady=1)
dzero.bind("<Button-1>", click)

point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
point.grid(row=4, column=2, padx=1, pady=1)
point.bind("<Button-1>", click)

equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
equals.grid(row=4, column=3, padx=1, pady=1)
equals.bind("<Button-1>", click)

root.mainloop()