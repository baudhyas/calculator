from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo


class Calculator(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.parent = master

        self.gui()
        self.parent.resizable(width=False, height=False)

    def gui(self):
        self.style_button = Style()
        self.style_button.configure('But.TButton', font=('calibri', 10, 'bold'),
                                    background='#a3dbf0', width=8, foreground='black')
        self.style_button.map('But.TButton',
                              foreground=[('disabled', 'yellow'),
                                          ('pressed', 'black'),
                                          ('active', 'blue')],
                              background=[('disabled', 'magenta'),
                                          ('pressed', '!focus', 'cyan'),
                                          ('active', 'red')],
                              highlightcolor=[('focus', 'green'),
                                              ('!focus', 'red')])

        self.entry = Entry(self.parent, width=40)
        self.entry.configure()
        self.entry.grid(row=0, column=0, columnspan=5)

        # buttons
        self.button_1 = Button(self.parent, text='1', style='But.TButton',
                               command=lambda: self.button_click(1))
        self.button_2 = Button(self.parent, text='2', style='But.TButton',
                               command=lambda: self.button_click(2))
        self.button_3 = Button(self.parent, text='3', style='But.TButton',
                               command=lambda: self.button_click(3))
        self.button_4 = Button(self.parent, text='4', style='But.TButton',
                               command=lambda: self.button_click(4))
        self.button_5 = Button(self.parent, text='5', style='But.TButton',
                               command=lambda: self.button_click(5))
        self.button_6 = Button(self.parent, text='6', style='But.TButton',
                               command=lambda: self.button_click(6))
        self.button_7 = Button(self.parent, text='7', style='But.TButton',
                               command=lambda: self.button_click(7))
        self.button_8 = Button(self.parent, text='8', style='But.TButton',
                               command=lambda: self.button_click(8))
        self.button_9 = Button(self.parent, text='9', style='But.TButton',
                               command=lambda: self.button_click(9))
        self.button_0 = Button(self.parent, text='0', style='But.TButton',
                               command=lambda: self.button_click(0))
        self.equal = Button(self.parent, text='=',
                            command=self.equal, style='But.TButton')
        self.clear = Button(self.parent, text='clear', style='But.TButton',
                            command=lambda: self.entry.delete(0, END))

        # operations button
        self.add = Button(self.parent, text='+', style='But.TButton',
                          command=lambda: self.button_click('+'))
        self.sub = Button(self.parent, text='-', style='But.TButton',
                          command=lambda: self.button_click('-'))
        self.mul = Button(self.parent, text='*', style='But.TButton',
                          command=lambda: self.button_click('*'))
        self.div = Button(self.parent, text='/', style='But.TButton',
                          command=lambda: self.button_click('/'))

        # positions
        self.button_1.grid(row=3, column=0, ipady=4)
        self.button_2.grid(row=3, column=1, ipady=4)
        self.button_3.grid(row=3, column=2, ipady=4)
        self.button_4.grid(row=2, column=0, ipady=4)
        self.button_5.grid(row=2, column=1, ipady=4)
        self.button_6.grid(row=2, column=2, ipady=4)
        self.button_7.grid(row=1, column=0, ipady=4)
        self.button_8.grid(row=1, column=1, ipady=4)
        self.button_9.grid(row=1, column=2, ipady=4)
        self.button_0.grid(row=4, column=0, ipady=4)

        self.clear.grid(row=4, column=1, ipady=4)
        self.equal.grid(row=4, column=2, ipady=4)

        # # opetator buttons location
        self.add.grid(row=1, column=4, ipady=4)
        self.sub.grid(row=2, column=4, ipady=4)
        self.mul.grid(row=3, column=4, ipady=4)
        self.div.grid(row=4, column=4, ipady=4)

    def button_click(self, parameter):
        data = self.entry.get()
        data += f'{parameter}'
        self.entry.delete(0, END)
        self.entry.insert(0, data)

    def equal(self):
        data = self.entry.get()
        if len(data) != 0:
            try:
                ans = eval(data)
                self.entry.delete(0, END)
                self.entry.insert(0, f'{ans}')
            except Exception as e:
                showinfo("Error", "Invalid Expression")


if __name__ == '__main__':
    root = Tk()
    root.title("Calculator")
    app = Calculator(root)
    app.mainloop()
