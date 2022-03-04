from tkinter import *
from NumericalFunctions import *
from tkinter import messagebox


def Clicked():
    options = [Input_Selected.get(), Output_Selected.get()]
    Input = Input_Box.get()
    try:
        Output = eval(options[0] + '_to_' + options[1] + '("' + Input + '")')
        Output_Box.configure(state='normal')
        Output_Box.delete(0, END)
        Output_Box.insert(END, Output)
    except:
        messagebox.showerror('Error', 'Invalid Input')


body = Tk()
body.title('Numbering System Converter')
body.geometry('405x200')
body.iconbitmap('numbers.ico')
body.resizable(width=FALSE, height=FALSE)
Input_Label = Label(body, text='Input').grid(row=0, column=0, sticky='W', pady=5, padx=10)
Output_Label = Label(body, text='Output').grid(row=2, column=0, sticky='W', pady=5, padx=10)
Input_Box = Entry(body, width=40, bd=5)
Input_Box.grid(row=1, column=0, padx=10, pady=5, columnspan=2)
Output_Box = Entry(body, width=40, bd=5)
Output_Box.configure(state='disabled')
Output_Box.grid(row=3, column=0, padx=10, pady=5, columnspan=2)

Input_Selection_Label = Label(body, text='Select Type').grid(row=0, column=3, pady=5, padx=10)
Output_Selection_Label = Label(body, text='Select Type').grid(row=2, column=3, pady=5, padx=10)
Input_Options = [
    'Binary',
    'Decimal',
    'Octal',
    'Hexadecimal'
]
Output_Options = [
    'Binary',
    'Decimal',
    'Octal',
    'Hexadecimal'
]
Input_Selected = StringVar()
Input_Selected.set('Decimal')
Output_Selected = StringVar()
Output_Selected.set('Binary')
Input_Menu = OptionMenu(body, Input_Selected, *Input_Options).grid(row=1, column=3, pady=5, padx=10)
Output_Menu = OptionMenu(body, Output_Selected, *Output_Options).grid(row=3, column=3, pady=5, padx=10)
Convert_Button = Button(body, text='Convert', width=10, command=Clicked).grid(row=4, column=3, pady=15, padx=10)
body.mainloop()