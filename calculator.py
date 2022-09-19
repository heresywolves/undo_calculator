from telnetlib import STATUS


from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    # equation.set(expression)


if __name__ == "__main__":

    gui = Tk()
    gui.title('Simply a Calculator')
    gui.geometry('400x600')
    gui.configure(bg='black')
    gui.resizable(False, False)

    # Background
    bg = PhotoImage(file='GUI\\bg.png')
    background = Label(gui, image=bg)
    background.place(x=0, y=0)

    # Icon
    icon = PhotoImage(file='GUI\\icon.png')
    gui.iconphoto(True, icon)

    # Creating an equation variable
    equation = StringVar()

    # Entry box
    expression_field = Entry(gui, textvariable=equation,
                             bg='#191818', borderwidth=0, highlightthickness=0, fg='green')
    expression_field.grid(ipadx=80, ipady=80, padx=60, pady=50)

    # Execute tkinter
    gui.mainloop()
