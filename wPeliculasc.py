from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.pelicula as Peli
from wPelicula import Pelicula

class Peliculas(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.select_id = -1        
        self.title("LISTADO DE PELICULAS")        
        width=800
        height=500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_464=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#333333"
        GLabel_464["justify"] = "center"
        GLabel_464.place(x=10,y=10,width=70,height=25)
        GLabel_464["text"] = "Películas:"

        tv = ttk.Treeview(self, columns=("NOMBRE", "CLASID", "GENERO","PRECIO"), name="tvPeliculas")
        tv.column("#0", width=78)
        tv.column("NOMBRE", width=100, anchor=CENTER)
        tv.column("CLASID", width=150, anchor=CENTER)
        tv.column("GENERO", width=150, anchor=CENTER)
        tv.column("PRECIO", width=150, anchor=CENTER)
       

        tv.heading("#0", text="PID", anchor=CENTER)
        tv.heading("NOMBRE", text="NOMBRE", anchor=CENTER)
        tv.heading("CLASID", text="CLASID", anchor=CENTER)
        tv.heading("GENERO", text="GENERO", anchor=CENTER)
        tv.heading("PRECIO", text="PRECIO", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.place(x=10,y=40,width=750,height=300)          
        
        self.refrescar()

        ft = tkFont.Font(family='Times',size=10)
        btn_agregar = Button(self)
        btn_agregar["bg"] = "#f0f0f0"        
        btn_agregar["font"] = ft
        btn_agregar["fg"] = "#000000"
        btn_agregar["justify"] = "center"
        btn_agregar["text"] = "Agregar"
        btn_agregar.place(x=530,y=10,width=70,height=25)
        btn_agregar["command"] = self.agregar

        btn_editar = Button(self)
        btn_editar["bg"] = "#f0f0f0"        
        btn_editar["font"] = ft
        btn_editar["fg"] = "#000000"
        btn_editar["justify"] = "center"
        btn_editar["text"] = "Editar"
        btn_editar.place(x=610,y=10,width=70,height=25)
        btn_editar["command"] = self.editar
        
        btn_eliminar = Button(self)
        btn_eliminar["bg"] = "#f0f0f0"        
        btn_eliminar["font"] = ft
        btn_eliminar["fg"] = "#000000"
        btn_eliminar["justify"] = "center"
        btn_eliminar["text"] = "Eliminar"
        btn_eliminar.place(x=690,y=10,width=70,height=25)
        btn_eliminar["command"] = self.eliminar

        btn_salir = Button(self)
        btn_salir["bg"] = "#f0f0f0"        
        btn_salir["font"] = ft
        btn_salir["fg"] = "#000000"
        btn_salir["justify"] = "center"
        btn_salir["text"] = "SALIR"
        btn_salir.place(x=690,y=360,width=100,height=30)
        btn_salir["command"] = self.salir

    def obtener_fila(self, event):
        tvPeliculas = self.nametowidget("tvPeliculas")
        current_item = tvPeliculas.focus()
        if current_item:
            data = tvPeliculas.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        Pelicula (self, True)

    def editar(self): 
        Pelicula (self, True, self.select_id)

    def eliminar(self):
        answer =  tkMsgBox.askokcancel(self.master.master.title(), "¿Está seguro de eliminar este registro?")   
        if answer:
            Pelicula.eliminar(self.select_id)
            self.refrescar()

    def salir(self):
        self.destroy()
    

    # https://www.youtube.com/watch?v=n0usdtoU5cE

    def refrescar(self):        
        tvPeliculas = self.nametowidget("tvPeliculas")
        for record in tvPeliculas.get_children():
            tvPeliculas.delete(record)
        peliculas = Peli.listar()
        for pelicula in peliculas:
            tvPeliculas.insert("", END, text=pelicula[0], values=(pelicula[1], pelicula[2], pelicula[3], pelicula[4])) 