from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.pelicula as peli
import bll.clasificacion as clasi 

class Pelicula(Toplevel):
    def __init__(self, master=None, isAdmin = False, peli_id = None):        
        super().__init__(master)
        self.master = master
        self.peli_id = peli_id       
        self.title("Registro de pelicula")        
        width=443
        height=423
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        
        GLabel_243 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_243["font"] = ft
        GLabel_243["fg"] = "#333333"
        GLabel_243["anchor"] = "e"
        GLabel_243["text"] = "Nombre:"
        GLabel_243.place(x=10,y=10,width=124,height=30)

        GLineEdit_871 = Entry(self, name="txtNombre")
        GLineEdit_871["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_871["font"] = ft
        GLineEdit_871["fg"] = "#333333"
        GLineEdit_871["justify"] = "left"
        GLineEdit_871["text"] = ""
        GLineEdit_871.place(x=140,y=10,width=284,height=30)

        GLabel_599 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_599["font"] = ft
        GLabel_599["fg"] = "#333333"
        GLabel_599["anchor"] = "e"
        GLabel_599["text"] = "Identificacion:"
        GLabel_599.place(x=10,y=50,width=122,height=30)

        GLineEdit_911 = Entry(self, name="txtIdentificacion")# poner un combo
        GLineEdit_911["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_911["font"] = ft
        GLineEdit_911["fg"] = "#333333"
        GLineEdit_911["justify"] = "left"
        GLineEdit_911["text"] = ""
        GLineEdit_911.place(x=140,y=50,width=285,height=30)   

        clasifi = dict(clasi.listar())
        
        cb_clasi = ttk.Combobox(self, state="readonly", values=list(clasifi.values()), name="cbClasi")
        
        cb_clasi.place(x=10,y=50,width=162,height=30)


        GLabel_737 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_737["font"] = ft
        GLabel_737["fg"] = "#333333"
        GLabel_737["anchor"] = "e"
        GLabel_737["text"] = "Genero:"
        GLabel_737.place(x=10,y=130,width=121,height=30)

        GLineEdit_234 = Entry(self, name="txtGenero")
        GLineEdit_234["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_234["font"] = ft
        GLineEdit_234["fg"] = "#333333"
        GLineEdit_234["justify"] = "left"
        GLineEdit_234["text"] = ""
        GLineEdit_234.place(x=140,y=130,width=133,height=30)

        GLabel_454 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_454["font"] = ft
        GLabel_454["fg"] = "#333333"
        GLabel_454["anchor"] = "e"
        GLabel_454["text"] = "Precio:"
        GLabel_454.place(x=10,y=170,width=124,height=30)

        GLineEdit_384 = Entry(self, name="txtPrecio")
        GLineEdit_384["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_384["font"] = ft
        GLineEdit_384["fg"] = "#333333"
        GLineEdit_384["justify"] = "left"
        GLineEdit_384["text"] = ""
        GLineEdit_384.place(x=140,y=170,width=285,height=30)

# # 
        GButton_825 = Button(self)
        GButton_825["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_825["font"] = ft
        GButton_825["fg"] = "#000000"
        GButton_825["justify"] = "center"
        GButton_825["text"] = "Aceptar"
        GButton_825.place(x=270,y=370,width=70,height=25)
        GButton_825["command"] = self.aceptar
        
        GButton_341 = Button(self)
        GButton_341["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_341["font"] = ft
        GButton_341["fg"] = "#000000"
        GButton_341["justify"] = "center"
        GButton_341["text"] = "Cancelar"
        GButton_341.place(x=350,y=370,width=70,height=25)
        GButton_341["command"] = self.GButton_341_command

        if peli_id is not None:
            pelicula = Pelicula.obtener_id(peli_id)
            if pelicula is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos de la pelicula, reintente nuevamente")
               self.destroy()
            else:
                GLineEdit_871.insert(0, pelicula[1])
                #GLineEdit_911.insert(0, pelicula[2])
                GLineEdit_234.insert(0, pelicula[3])
                GLineEdit_234.insert(0, pelicula[4])
                GLineEdit_911["state"] = "desable"           
                cb_clasi.set(pelicula[2])

    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def GButton_341_command(self):
        self.destroy()

    def aceptar(self):
        try:            
            nombre = self.get_value("txtNombre")            
            identificacion = self.get_value("txtIdentificacion")            
            genero = self.get_value("txtGenero")
            precio = self.get_value("txtPrecio")            
            

            # TODO validar los datos antes de ingresar


            if self.peli_id is None:
                print("Alta de Pelicula")
                if not peli.existe(peli):# verr!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    peli.agregar( nombre, identificacion, genero, precio)
                    tkMsgBox.showinfo(self.master.title(), "Registro agregado!!!!!!")                
                    try:
                        self.master.refrescar()
                    except Exception as ex:
                        print(ex)
                    self.destroy()                
                else:
                    tkMsgBox.showwarning(self.master.title(), "La Pelicula existente en nuestros registros")
            else:
                print("Actualizacion de pelicula")
                peli.actualizar(self.PID, nombre, identificacion,  genero, precio) 
                tkMsgBox.showinfo(self.master.title(), "Registro modificado!!!!!!")                
                self.master.refrescar()
                self.destroy()  

        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))


