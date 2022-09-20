from telnetlib import STATUS


from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    # equation.set(expression)


def clear():
    pass


if __name__ == "__main__":

    gui = Tk()
    gui.title('Simply a Calculator')
    gui.geometry('400x650')
    gui.configure(bg='black')
    gui.resizable(False, False)

    # Background
    bg = PhotoImage(file='GUI\\bg.png')
    background = Label(gui, image=bg, border=0, borderwidth=0)
    background.place(x=0, y=0)

    # Icon
    icon = PhotoImage(file='GUI\\icon.png')
    gui.iconphoto(True, icon)

    # Creating an equation variable
    equation = StringVar()

    # Entry box
    expression_field = Entry(gui, textvariable=equation,
                             bg='#191818', borderwidth=0, highlightthickness=0, fg='green', font=("Times New Roman", 44),
                             width=8, justify="right")
    expression_field.grid(columnspan=4, ipadx=20, padx=60, pady=100)

    # Buttons
    button1_image = PhotoImage(file='GUI\\1.png')
    button1 = Button(gui, image=button1_image, bg='black', activebackground="black", anchor='center',
                     borderwidth=0, highlightthickness=0, command=lambda: press(1))
    button1.grid(row=3, column=0, rowspan=2)

    button2_image = PhotoImage(file='GUI\\2.png')
    button2 = Button(gui, image=button2_image, bg='black', activebackground="black", anchor='center',
                     borderwidth=0, highlightthickness=0, command=lambda: press(2))
    button2.grid(row=3, column=1, rowspan=2)

    button3_image = PhotoImage(file='GUI\\3.png')
    button3 = Button(gui, image=button3_image, bg='black', activebackground="black", anchor='center',
                     borderwidth=0, highlightthickness=0, command=lambda: press(3))
    button3.grid(row=3, column=2, rowspan=2)

    button4_image = PhotoImage(file='GUI\\4.png')
    button4 = Button(gui, image=button4_image, bg='black', activebackground="black", anchor='center',
                     borderwidth=0, highlightthickness=0, command=lambda: press(4))
    button4.grid(row=5, column=0, rowspan=2)

    button5_image = PhotoImage(file='GUI\\5.png')
    button5 = Button(gui, image=button5_image, bg='black', activebackground="black", anchor='center',
                     borderwidth=0, highlightthickness=0, command=lambda: press(5))
    button5.grid(row=5, column=1, rowspan=2)

    button6_image = PhotoImage(file='GUI\\6.png')
    button6 = Button(gui, image=button6_image, bg='black', activebackground="black", anchor='center',
                     borderwidth=0, highlightthickness=0, command=lambda: press(6))
    button6.grid(row=5, column=2, rowspan=2)

    button7_image = PhotoImage(file='GUI\\7.png')
    button7 = Button(gui, image=button7_image, bg='black', activebackground="black", anchor='center',
                     borderwidth=0, highlightthickness=0, command=lambda: press(7))
    button7.grid(row=7, column=0, rowspan=2, pady=15)

    button8_image = PhotoImage(file='GUI\\8.png')
    button8 = Button(gui, image=button8_image, bg='black', activebackground="black", anchor='center',
                     borderwidth=0, highlightthickness=0, command=lambda: press(8))
    button8.grid(row=7, column=1, rowspan=2, pady=15)

    button9_image = PhotoImage(file='GUI\\9.png')
    button9 = Button(gui, image=button9_image, bg='black', activebackground="black", anchor='center',
                     borderwidth=0, highlightthickness=0, command=lambda: press(9))
    button9.grid(row=7, column=2, rowspan=2, pady=15)

    plus_image = PhotoImage(file='GUI\\plus.png')
    plus = Button(gui, image=plus_image, bg='black', activebackground="black",
                  borderwidth=0, highlightthickness=0, command=lambda: press("+"))
    plus.grid(row=3, column=3, pady=5)

    minus_image = PhotoImage(file='GUI\\minus.png')
    minus = Button(gui, image=minus_image, bg='black', activebackground="black",
                   borderwidth=0, highlightthickness=0, command=lambda: press("-"))
    minus.grid(row=4, column=3, pady=5)

    multiply_image = PhotoImage(file='GUI\\multiply.png')
    multiply = Button(gui, image=multiply_image, bg='black', activebackground="black",
                      borderwidth=0, highlightthickness=0, command=lambda: press("*"))
    multiply.grid(row=5, column=3, pady=5)

    divide_image = PhotoImage(file='GUI\\divide.png')
    divide = Button(gui, image=divide_image, bg='black', activebackground="black",
                    borderwidth=0, highlightthickness=0, command=lambda: press("/"))
    divide.grid(row=6, column=3, pady=5)

    equal_image = PhotoImage(file='GUI\\equals.png')
    equal = Button(gui, image=equal_image, bg='black', activebackground="black",
                   borderwidth=0, highlightthickness=0, command=lambda: press("="), anchor='center', justify='center')
    equal.grid(row=2, column=3, pady=5)

    clear_image = PhotoImage(file='GUI\\C.png')
    clear = Button(gui, image=clear_image, bg='black', activebackground="black",
                   borderwidth=0, highlightthickness=0, command=clear)
    clear.grid(row=2, column=2, pady=5)

    undo_image = PhotoImage(file='GUI\\undo.png')
    undo = Button(gui, image=undo_image, bg='black', activebackground="black",
                  borderwidth=0, highlightthickness=0, command=lambda: press("="))
    undo.grid(row=2, column=0, columnspan=2)

    # Execute tkinter
    gui.mainloop()
