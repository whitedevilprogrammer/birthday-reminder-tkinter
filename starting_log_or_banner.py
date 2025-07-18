from tkinter import *
from PIL import ImageTk,Image
def Log_Or_Banner():
    root = Tk()
    app_width = 350
    app_height = 144
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
    img = ImageTk.PhotoImage(Image.open(fr))
    my_label = Label(image=img)
    my_label.pack()
    #time.sleep(2)
    root.after(4000, lambda: root.destroy())
    root.mainloop()
    #root.after(2,lambda:root.destroy())
Log_Or_Banner()


