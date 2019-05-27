from tkinter import *
from tkinter import ttk

'''
Nuestra aplicacion principal realmente es una ventana tkinter
en la que iremos metiendo cosas (widgets), por lo tanto
la clase principal mas que crear un objeto de tipo Tk deberia
heredar de dicha clase
'''
class MainApp(Tk):
    size ="1024x768"
    
    def __init__(self):        
        Tk.__init__(self)
        
        self.geometry(self.size)
        self.title("Mi Ventana")
        self.configure(bg="blue")
    
    def start(self):
        self.mainloop()
    

if __name__ == "__main__":
    app = MainApp()
    print(mainWindow.variable)
    app.start()
    