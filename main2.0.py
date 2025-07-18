import notification_all_work
import date_before
import month_order
from plyer import notification
from tkinter import *
from PIL import ImageTk,Image
#from tkinter.ttk import Radiobutton
from tkinter import messagebox
import datetime

x = datetime.datetime.now()

#print(x.strftime("%Y"))

#print(dir(Tk))

def Ntmbl(): # New this month birthday list ...
    notification_name = []
    notification_date = []
    v = datetime.datetime.now()
    y = v.strftime('%B')
    #Label(win, text=f"{y} Birthday list",font=("Times New Roman", 15)).grid(row=1, column=0, padx=30, pady=25)
    v = datetime.datetime.now()
    m = v.strftime('%m')
    Real_year = v.strftime('%Y')
    # print(int(y) -1)
    # print(m)
    d = {}
    namess = []
    datess = []
    with open('all_brithday_list.txt', 'r') as f1:
        al = f1.readlines()
        for i in al:
            name = i.split(':')[0].upper()
            date = i.split(':')[-1][:-1]
            d[name] = date
            dates, months, years = date.split('/')
            D, M, Y = date_before.Remainder(dates, months, Real_year)
            # print(f'{D}/{M}/{Y}')
            if int(m) == int(months):
                namess.append(name);datess.append(date)
                notification_name.append(name)
                #print(name,f'{D}/{M}/{Y}')
                notification_date.append(f'{D}/{M}/{Y}')
                # print('Notification date',f'{D}/{M}/{Y}')
    # print(namess,datess)
    print(datess)
    print(namess)
    return (datess,namess,y)

def Remind(root): # this is menu bar Remind setting
    root.destroy()
    win = Tk()
    win.title('Remind')
    app_width = 260
    app_height = 200
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    win.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}') #win.geometry('640x200')
    win.iconbitmap('code.ico')
    l = LabelFrame(win, text = '',padx = 5,pady=5, bg='SkyBlue1')
    l.pack(padx=5,pady=5)
    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()
    v5 = IntVar()
    Checkbutton(l, text='Today',variable=v1,onvalue =1,offvalue=0,bg='SkyBlue1').grid(row=1,column=0) # radiobutton or message cliiked
    Checkbutton(l, text='1 Day before', variable=v2,onvalue=2, offvalue=0,bg='SkyBlue1').grid(row=2,column=0)
    Checkbutton(l, text='2 Day before', variable=v3, onvalue=3, offvalue=0,bg='SkyBlue1').grid(row=3,column=0)
    Checkbutton(l, text='3 Day before', variable=v4, onvalue=4, offvalue=0,bg='SkyBlue1').grid(row=4,column=0)
    Checkbutton(l, text='1 Week before', variable=v5, onvalue=5, offvalue=0,bg='SkyBlue1').grid(row=5,column=0)

    with open('remind_setting.txt', 'r') as default:
        al = default.readlines()
        v1.set(int(al[0]))
        v2.set(int(al[1]))
        v3.set(int(al[2]))
        v4.set(int(al[3]))
        v5.set(int(al[4]))
    #print(v3.set(3))
    def save_Remind():
        count = 0
        all_get_value = [v1,v2,v3,v4,v5]
        for i in all_get_value:
            #print(i.get())
            if i.get() == 0:
            #print(count)
                count += 1
        #print(count)
        if count != 5:
            with open('remind_setting.txt', 'w') as f:
                with open('remind_setting.txt', 'a') as f:
                    f.write(str(v1.get()) + '\n')
                    f.write(str(v2.get())+ '\n')
                    f.write(str(v3.get())+ '\n')
                    f.write(str(v4.get())+ '\n')
                    f.write(str(v5.get())+ '\n')
                    print(v1.get())
                    print(v2.get())
                    print(v3.get())
                    print(v4.get())
                    print(v5.get())
                    messagebox.showinfo(title='Info',message='Successfully saved')
        else:
            messagebox.showerror(title='Error',message='Please any one select the option')
    def home():
        win.destroy()
        root = Tk()
        main(root,first_time=2)

    Button(l, text='Save', command=save_Remind,bg='SkyBlue1').grid(row=6,column=0,padx = 10, pady= 10)
    Button(l, text='Return to home', command=home,bg='SkyBlue1').grid(row=6,column=1,padx = 10, pady= 10)
    win.mainloop()





def main(root,first_time=1):
    app_width = 600
    app_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    root.title('Birthday remainder')
    # menubar setting !
    menubar = Menu(root)
    setting = Menu(menubar,tearoff=0)
    menubar.add_cascade(label = 'Settings', menu = setting)
    setting.add_command(label = 'Remind',command = lambda: Remind(root))

    #root.overrideredirect(True) # no title bar and also no moving
    #root.resizable(0,0) # no maxima
    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}') #root.geometry('500x440')
    #root.eval('tk::PlaceWindow . center')
    #root.iconbitmap("@linux.xbm")
    root.iconbitmap('code.ico')
    l = LabelFrame(root,text = '',padx=10,pady=10,background='SkyBlue1')
    l.pack(padx=10,pady=10)
    title = Label(l, text='Welcome to Birthday remainder !', width=55, font=('Times New Roman', 25, ''), fg='DarkOrchid4',bg='SkyBlue1')
    title.pack()
    #bl = Button(root, text='This month Birthday list', width=55, command=lambda: Tmbl(root))
    #bl.pack(pady=10)
    bl = LabelFrame(l,text = '',padx=50,pady=10,background='SkyBlue1')
    bl.pack(padx=10,pady=10)
    bv = Button(bl, text='View all Birthday list !', font=('Times New Roman', 15, ''), command=lambda: Vab(root),
                fg='DarkOrchid4', bg='SkyBlue2')
    bv.pack(pady=10)
    ba = Button(bl,text = 'Add the Birthday date !',font=('Times New Roman', 15, ''), command = lambda : Abd(root), fg='DarkOrchid4',bg='SkyBlue2')
    ba.pack(pady=10)
    br = Button(bl,text = 'Remove the Birthday date !',font=('Times New Roman', 15, ''), command = lambda : Rbd(root), fg='DarkOrchid4',bg='SkyBlue2')
    br.pack(pady=10)

    #print(first_time)
    if first_time == 1:
        notification_all_work.Notificatios_proccess()
    #-------------------------------------
    # "this below coding is" >>> this month birthday list
    dates, names, months = Ntmbl()
    thism = Label(l, text=f"{months} Month Bithday list", width=55, font=('Times New Roman', 15,''), fg='chocolate',bg='SkyBlue1')
    thism.pack()
    sb = Scrollbar(l)
    sb.pack(side=RIGHT,fill=Y)
    mylist = Listbox(l,yscrollcommand=sb.set,font=("Times New Roman", 15))
    dates, names, months = Ntmbl() # this is function
    print(dates,names)
    #print(dates)
    for j in range(len(dates)):  # this month birthday list !!!
        if j == 0:
            pass
            # thism = Label(l, text=f"{months} Month Bithday list", width=55, font=('Times New Roman', 15,''), fg='chocolate',bg='SkyBlue1')
            # thism.pack()
            #mylist.insert(END, f"{months} Month Bithday list")
        #postion = dates.index(min(dates))
        mylist.insert(END,f"{'*' * 58}")
        mylist.insert(END,f"{j + 1}) {names[j]} : {dates[j]}")
        # Label(win,text = f"{'*' * 55}",font=("Times New Roman", 11)).grid(row=j+fcount,column = 0)
        # Label(win,text=f"{namess[postion].upper()} : {min(datess)}",font=("Times New Roman", 11)).grid(row=j+scount,column=0)
        mylist.pack(side=LEFT,fill=BOTH,expand=True)
        sb.config(command=mylist.yview)
        #names.remove(names[j])
        #dates.remove(dates[j])
    mylist.insert(END, f"{'*' * 58}")
    root.config(menu = menubar) # this is menubar !
    root.mainloop()

def Abd(root): # Adding Birthday date
    root.destroy()
    win = Tk()
    app_width = 720
    app_height = 210
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    win.title('Adding Birthday date !')
    win.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}') #win.geometry('640x200')
    win.iconbitmap('code.ico')
    #l1 = Label(win, text='Adding to Birthday date', width=55, font=('', 20, ''), fg='blue')
    #l1.pack()
    l = LabelFrame(win,text='',padx=5,pady=5,bg='SkyBlue1')
    l.pack(padx=5,pady=5)
    Label(l, text="Enter the Birthday person's name :",
          font=("Times New Roman", 15),fg = 'DarkOrchid4',bg='SkyBlue1').grid(row=1, column=0, padx=30, pady=25)
    value = Entry(l, textvariable="username", width=50)
    value.grid(row=1, column=1, padx=30, pady=25)

    Label(l, text="Enter day / month / year:",
          font=("Times New Roman", 15),fg = 'DarkOrchid4',bg='SkyBlue1').grid(row=2, column=0, padx=30, pady=25)
    value1 = Entry(l, width=50)
    value1.grid(row=2, column=1, padx=30, pady=25)
    def save():
        ds = False
        ms = False
        ys = False
        ry = False
        go = False
        ly = False
        #print(value.get())
        name = value.get().strip()
        date = value1.get().strip()
        v = datetime.datetime.now()
        y1 = v.strftime('%Y')
        m1 = v.strftime('%m')
        d1 = v.strftime('%d')
        #print(y1)
        if name != '':
            if date != '':
                try:
                    d, m, y = date.split('/')
                    go = True
                except ValueError:
                    messagebox.showerror('Error', 'formate is wrong ! example (12/8/2020)')
                    #print('formate is wrong ! example (12/12/2020)')
                #[print(i) for i in range(int(y1), int(y1) - 130, -1)]
                if go:
                    if int(y) in range(int(y1), int(y1) - 130, -1):
                        ys = True
                        if int(y1) == int(y):
                            ry = True
                        if int(y) % 4 == 0:
                            ly = True
                        if int(m) in range(1,13):
                            ms = True
                            if int(m) in (1,2,5,7,8,10,12):
                                if int(d) in range(1,32):
                                    ds = True
                                else:
                                    messagebox.showerror('Error', 'day is out of range !!')
                                    #print('day is out of range !!')
                            elif int(m) in (4,6,9,11):
                                if int(d) in range(1,31):
                                    print(' yes sssssssssssssssssssssss')
                                    ds = True
                                else:
                                    messagebox.showerror('Error', 'day is out of range !!')
                                    #print('day is out of range !!')
                            elif ly:
                                if int(d) in range(1,30):
                                    ds = True
                                else:
                                    messagebox.showerror('Error', 'day is out of range !!')
                                    #print('day is out of range !!')
                            elif not ly:
                                if int(d) in range(1,29):
                                    ds = True
                                else:
                                    messagebox.showerror('Error', 'day is out of range !!')
                                    #print('day is out of range !!')
                        else:
                            messagebox.showerror('Error', 'Out of range Month !!')
                            #print(' Out of month range !!')
                    else:
                        messagebox.showerror('Error', 'This is out of range year !')
                        #print('this is out of range year !')
            else:
                messagebox.showerror('Error', 'date is empty !!')
                #print('date is empty !!')
        else:
            messagebox.showerror('Error','Name is empty !')
            #print('name is empty !')
        if ry:
            ms = False
            ds = False
            if int(m) <= int(m1):
                ms = True
                if int(d) <= int(d1):
                    ds = True
                else:
                    messagebox.showerror('Error', 'day is out of range !!')
            else:
                messagebox.showerror('Error', 'Out of range Month !!')

        if ds and ms and ys:
            duplicate = True
            print(name)
            print(date)
            with open('all_brithday_list.txt', 'r') as f:
                al = f.readlines()
                for i in al:
                    #print(f'{name.upper()}:{date}\n' == i)
                    if f'{name.upper()}:{int(d)}/{int(m)}/{int(y)}\n' == i:
                        duplicate = False
                        messagebox.showerror('Error', 'all ready available in birthday list !')

            if duplicate:
                with open('all_brithday_list.txt', 'a') as f:
                    format = f'{name.upper()}:{int(d)}/{int(m)}/{int(y)}\n'
                    f.write(format)
                month_order.start_process()
                messagebox.showinfo('Info', 'Birthday name and date is successfully added')
            value.delete(0,END)
            value1.delete(0,END)
                #print('Birthday name and date is successfully add ...')

    def home():
        win.destroy()
        root = Tk()
        main(root,first_time=2)
    Button(l,text= 'Save',command=save,font=('Times New Roman', 13, ''), fg='DarkOrchid4',bg='SkyBlue2').grid(row=3,column=0)
    Button(l, text='Return to home',font=('Times New Roman', 13, ''), command=home, fg='DarkOrchid4',bg='SkyBlue2').grid(row=3, column=1)
    root.mainloop()

def Rbd(root):
    root.destroy()
    win = Tk()
    app_width = 690
    app_height = 160
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    win.title('Remove the Birthday date !')
    win.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')#win.geometry('580x160')
    win.iconbitmap('code.ico')
    l = LabelFrame(win,text='',padx=5,pady=5,bg='SkyBlue1')
    l.pack(padx=10,pady=10)
    Label(l, text="Remove the Birthday date and name select:",
          font=("Times New Roman", 15),fg = 'DarkOrchid4',bg='SkyBlue1').grid(row=1, column=0, padx=30, pady=25)
    with open('all_brithday_list.txt', 'r') as f:
        als = f.readlines()
        #print(als)
        al = []
        for one_value in als:
            al.append(one_value.upper())
    clicked = StringVar()
    clicked.set(al[0])
    option_menu = OptionMenu(l,clicked, *al)
    option_menu.grid(row=1, column=1, padx=10, pady=25)
    option_menu.config(bg='SkyBlue1',width= 30)
    def delete():
        #print(clicked.get())
        select = clicked.get()
        with open('all_brithday_list.txt', 'r') as f:
            al = f.readlines()
        with open('all_brithday_list.txt', 'w') as f:
            for i in al:
                #print(i)
                #print(select,i,select==i)
                if i != select:
                        f.write(i)
        with open('all_brithday_list.txt', 'r') as f:
            al = f.readlines()
        #print('Successfully removed !')
        r_index = option_menu['menu'].index(clicked.get()) # index of selected option
        option_menu['menu'].delete(r_index) # deleted the option
        clicked.set(al[0])
        messagebox.showinfo('Info','Successfully removed !')

    def home():
        win.destroy()
        root = Tk()
        main(root,first_time=2)

    Button(l, text='Delete', command=delete,font=('Times New Roman', 13, ''), fg='DarkOrchid4',bg='SkyBlue2').grid(row=3,column=0)
    Button(l, text='Return to home', command=home,font=('Times New Roman', 13, ''), fg='DarkOrchid4',bg='SkyBlue2').grid(row=3,column=1)
    root.mainloop()

def Vab(root):
    root.destroy()
    win = Tk()
    app_width = 530
    app_height = 340
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    win.title('View all Birthday list !')
    win.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')#win.geometry('580x160')
    win.iconbitmap('code.ico')
    hl = LabelFrame(win, text='', padx=5, pady=5, bg='SkyBlue1',)
    hl.pack(padx=10, pady=10)
    l = LabelFrame(hl, text='', padx=5, pady=5, bg='SkyBlue1',)
    l.pack(padx=10, pady=10)
    # title = Label(l, text='Welcome to Birthday remainder !', width=55, font=('Times New Roman', 25, ''),
    #               fg='DarkOrchid4', bg='SkyBlue1')
    # title.pack()

    sb = Scrollbar(l)
    sb.pack(side=RIGHT,fill=Y)
    mylist = Listbox(l,yscrollcommand=sb.set,font=("Times New Roman", 15),width= 43)
    with open('all_brithday_list.txt','r') as f:
        al = f.readlines()
    #print(dates)
    for j in range(len(al)):  # this month birthday list !!!
        mylist.insert(END,f"{'*' * 47}")
        mylist.insert(END,f"{j + 1}) {al[j]}")
        mylist.pack(side=LEFT,fill=BOTH,expand=True)
        sb.config(command=mylist.yview)
        #names.remove(names[j])
        #dates.remove(dates[j])
    mylist.insert(END, f"{'*' * 47}")

    def home():
        win.destroy()
        root = Tk()
        main(root,first_time=2)
    Button(hl, text='Return to home',font=('Times New Roman', 13, ''), command=home, fg='DarkOrchid4',bg='SkyBlue2').pack()
    root.mainloop()





def Log_Or_Banner():
    root = Tk()
    app_width = 874
    app_height = 236
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    root.overrideredirect(True)
    f = "happy_brithday.png"
    s = "Happy-Birthday-Logo-Png.png"
    t = "birthday_remainder.png"
    fr = "happy_b.jfif"
    my_logo = 'my_logo.png'
    img = ImageTk.PhotoImage(Image.open(my_logo))
    my_label = Label(image=img)
    my_label.pack()
    #time.sleep(2)
    root.after(4000, lambda: root.destroy())
    root.mainloop()
    #root.after(2,lambda:root.destroy())
if __name__ == '__main__':
    Log_Or_Banner()
    roots = Tk()
    main(roots,first_time=1)





