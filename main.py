from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import datetime

x = datetime.datetime.now()

print(x.strftime("%Y"))

print(dir(Tk))
def main(root):
    root.title('Birthday remainder')
    root.geometry('600x400')
    #root.iconbitmap("@linux.xbm")
    root.iconbitmap('code.ico')
    l = Label(root,text = 'Welcome to Birthday remainder !',width= 55,font=('',20,''),fg='blue')
    l.pack()
    ba = Button(root,text = 'Add the Birthday date !', width = 55, command = lambda : Abd(root))
    ba.pack()
    br = Button(root,text = 'Remove the Birthday date !', width = 55)
    br.pack()
    root.mainloop()
def valid_date(day,month,year):
    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False
    return isValidDate
def Abd(root): # Adding Birthday date
    root.destroy()
    win = Tk()
    win.title('Adding Birthday date !')
    win.geometry('600x400')
    win.iconbitmap('code.ico')
    #l1 = Label(win, text='Adding to Birthday date', width=55, font=('', 20, ''), fg='blue')
    #l1.pack()

    # label text for title
    Label(win, text="Adding to Birthday !",
              bg='green', fg="white",
              font=("Times New Roman", 30))
    Label(win, text="Enter the Birthday person's name :",
          font=("Times New Roman", 10)).grid(row=1, column=0,padx=30, pady=25)
    value = Entry(win,text="Enter the Birthday person's name",textvariable="username",width = 50)
    value.grid(row=1, column=1,padx=30, pady=25)

    # label
    Label(win, text="Select the Date:",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=5, padx=30, pady=25)

    b = StringVar()
    date = Combobox(win, width=50, textvariable=b)
    # Adding combobox drop down list
    date['values'] = [i for i in range(1, 32)]
    date.grid(column=1, row=5)
    date.current()

    Label(win, text="Select the Month :",
              font=("Times New Roman", 10)).grid(column=0,
                                                 row=6, padx=30, pady=25)

    # Combobox creation
    n = StringVar()
    monthchoosen = Combobox(win, width=50, textvariable=n)
    # Adding combobox drop down list
    monthchoosen['values'] = [i for i in range(1,13)]

    monthchoosen.grid(column=1, row=6)
    monthchoosen.current()


    Label(win, text="Select the year :",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=7, padx=30, pady=25)
    v = StringVar()
    years_choice = Combobox(win, width=50, textvariable=v)
    x = datetime.datetime.now()
    years = x.strftime("%Y")

    years_choice['values'] = [i for i in range(int(years),int(years)-130,-1)]
    years_choice.grid(column=1, row=7)
    years_choice.current()


    def Save():
        Label(win,text=value.get().upper()).grid(row = 11, column = 1)
        Label(win, text=date.get()).grid(row=12, column=1)
        Label(win, text=monthchoosen.get()).grid(row=13, column=1)
        Label(win, text=years_choice.get()).grid(row=14, column=1)

        correctDate = None
        try:
            newDate = datetime.datetime(years_choice.get(), monthchoosen().get(), date.get())
            correctDate = True
        except ValueError:
            correctDate = False
        print(str(correctDate))

    Button(win,text = 'Save', command = Save).grid(column=0,row=9, padx=30, pady=25)

    # Excecute Tkinter
    root.mainloop()


root = Tk()
main(root)





