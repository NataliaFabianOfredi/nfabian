from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.pelicula as peli

class Peliculas2(ttk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.select_id = -1    #fijar para que
        self.title("REGISTRO DE PELICULAS")
        #setting window size
        width=345
        height=421
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GButton_351=ttk.Button(self)
        GButton_351["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_351["font"] = ft
        GButton_351["fg"] = "#000000"
        GButton_351["justify"] = "center"
        GButton_351["text"] = "Aceptar"
        GButton_351.place(x=60,y=340,width=70,height=25)
        GButton_351["command"] = self.GButton_351_command

        GButton_117=ttk.Button(self)
        GButton_117["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_117["font"] = ft
        GButton_117["fg"] = "#000000"
        GButton_117["justify"] = "center"
        GButton_117["text"] = "Cancelar"
        GButton_117.place(x=190,y=340,width=70,height=25)
        GButton_117["command"] = self.GButton_117_command

        GLabel_897=ttk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_897["font"] = ft
        GLabel_897["fg"] = "#333333"
        GLabel_897["justify"] = "center"
        GLabel_897["text"] = "Nombre:"
        GLabel_897.place(x=50,y=100,width=70,height=25)

        GListBox_488=ttk.Listbox(self)
        GListBox_488["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_488["font"] = ft
        GListBox_488["fg"] = "#333333"
        GListBox_488["justify"] = "center"
        GListBox_488.place(x=140,y=100,width=119,height=30)

        GLabel_47=ttk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_47["font"] = ft
        GLabel_47["fg"] = "#333333"
        GLabel_47["justify"] = "center"
        GLabel_47["text"] = "Clasificación:"
        GLabel_47.place(x=60,y=160,width=70,height=25)

        GListBox_286=ttk.Listbox(self)
        GListBox_286["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_286["font"] = ft
        GListBox_286["fg"] = "#333333"
        GListBox_286["justify"] = "center"
        GListBox_286.place(x=140,y=150,width=119,height=30)

        GLabel_28=ttk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_28["font"] = ft
        GLabel_28["fg"] = "#333333"
        GLabel_28["justify"] = "center"
        GLabel_28["text"] = "Genero"
        GLabel_28.place(x=50,y=210,width=70,height=25)

        GLineEdit_858=ttk.Entry(self)
        GLineEdit_858["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_858["font"] = ft
        GLineEdit_858["fg"] = "#333333"
        GLineEdit_858["justify"] = "center"
        GLineEdit_858["text"] = "Entry"
        GLineEdit_858.place(x=140,y=210,width=119,height=30)

        GLabel_645=ttk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_645["font"] = ft
        GLabel_645["fg"] = "#333333"
        GLabel_645["justify"] = "center"
        GLabel_645["text"] = "Precio:"
        GLabel_645.place(x=50,y=270,width=70,height=25)

        GLineEdit_680=ttk.Entry(self)
        GLineEdit_680["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_680["font"] = ft
        GLineEdit_680["fg"] = "#333333"
        GLineEdit_680["justify"] = "center"
        GLineEdit_680["text"] = "Entry"
        GLineEdit_680.place(x=140,y=270,width=122,height=30)

       # self.mainloop()

    def GButton_351_command(self):
        print("command")


    def GButton_117_command(self):
        print("command")


