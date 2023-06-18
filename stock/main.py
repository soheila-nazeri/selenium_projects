import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from tkinter import messagebox
from  dbconfig import test_mysql_connection as testdb
from dbconfig import CreateDatabase  as Create
from Symbol import insertSymbol
from symbolInfo import insertSymbolInfo
from daily import insertSymbolDaily 


#Functions
def max_size_windows(name_of_window):
    name_of_window.update_idletasks()
    name_of_window.state('zoomed')

def exit_programm():
    if messagebox.askokcancel("خروج", "آیا میخواهید از برنامه خارج شوید ؟"):
        main_window.destroy()
#===================== ok
def CreateDatabase():
    if Create():
        messagebox.showinfo("Test Connection","دیتابیس ایجاد شد ....")
    else:
        messagebox.showinfo("Test Connection","فرآیند ایجاد با خطا مواجه شد....")
#===================== ok
def test_Connection():
    if (testdb()):
        messagebox.showinfo("Test Connection","ارتباط برقرار است....")
    else:
        messagebox.showinfo("Test Connection","ارتباط با سرور برقرار نیست....")
    
#===================== ok
def GetSymbol():
    if testdb()== False:
        messagebox.showinfo("Test Connection","ارتباط با سرور برقرار نیست....")
        exit 
    insertSymbol()

def GetSymbolIdentityInfo():
    if testdb()== False:
        messagebox.showinfo("Test Connection","ارتباط با سرور برقرار نیست....")
        exit 
    insertSymbolInfo()

def GetSymbolDaily():
    if testdb()== False:
        messagebox.showinfo("Test Connection","ارتباط با سرور برقرار نیست....")
        exit 
    insertSymbolDaily()


def show_about():
    messagebox.showinfo("توضیحات برنامه ....")
def show_help():
    messagebox.showinfo("نسخه نرم افزار", "نسخه 1.0")

# Das Hauptfenster des Programms
main_window = tk.Tk()
main_window.title("نرم افزار بورس اوراق بهادار")
main_window.iconbitmap('bourse.ico')
max_size_windows(main_window)
# Hitergrund
bg_image = Image.open("bourse.png")
bg_photo = ImageTk.PhotoImage(bg_image)

# picture background
bg_label = tk.Label(main_window, image=bg_photo)
bg_label.place(x=0.2, y=0.2, relwidth=1, relheight=1, anchor="nw")


# Menu erstellen
menu_bar = tk.Menu(main_window)
main_window.config(menu=menu_bar)

#Menu about help
about_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="درباره ما", menu=about_menu)
about_menu.add_command(label="اطلاعات", command=show_help)


#Buttons
Button_DataBase = tk.Button(main_window,text='ایجاد دیتابیس', command=CreateDatabase, height=1, width=20)
Button_DataBase.place(relx=0.99, rely=0.05, anchor='ne')

Button_Connection = tk.Button(main_window,text='تست دیتابیس', command=test_Connection, height=1, width=20)
Button_Connection.place(relx=0.99, rely=0.09, anchor='ne')

Button_Symbol = tk.Button(main_window,text='دریافت اطلاعات نمادها', command=GetSymbol, height=1, width=20)
Button_Symbol.place(relx=0.99, rely=0.13, anchor='ne')

Button_Symbol = tk.Button(main_window,text='دریافت اطلاعات شناسه ها', command=GetSymbolIdentityInfo, height=1, width=20)
Button_Symbol.place(relx=0.99, rely=0.17, anchor='ne')

Button_Symbol = tk.Button(main_window,text='دریافت اطلاعات لحظه ای بازار', command=GetSymbolDaily, height=1, width=20)
Button_Symbol.place(relx=0.99, rely=0.21, anchor='ne')

Button_About = tk.Button(main_window,text='درباره', command=show_about, height=1, width=20)
Button_About.place(relx=0.99, rely=0.25, anchor='ne')

Button_Help = tk.Button(main_window,text='راهنمایی', command=show_help, height=1, width=20)
Button_Help.place(relx=0.99, rely=0.29, anchor='ne')

Button_Exit = tk.Button(main_window,text='خروج', command=exit_programm, height=1, width=20)
Button_Exit.place(relx=0.99, rely=0.34, anchor='ne')

main_window.mainloop()



