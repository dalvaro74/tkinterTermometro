from tkinter import *
from tkinter import ttk

class MainApp(Tk):
    size ="210x150"
    entrada = None
    tipoUnidad = None
    __prevTemp = ""
    
    def __init__(self):        
        Tk.__init__(self)
        
        self.geometry(self.size)
        self.title("Mi Ventana")
        self.configure(bg="#F0F0F0")
        #Para evitar que la pantalla se pueda redimensionar a mano
        self.resizable(0,0)
        
        self.temperatura = StringVar(value="")
        self.temperatura.trace("w",self.validateTemperature)
        self.tipoUnidad = StringVar(value="C")
        
        self.createLayout()
    
    def createLayout(self):
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=40, y=10)
        
        self.lbUnidad = ttk.Label(self, text="Grados").place(x=40,y=45)
        self.rb1 = ttk.Radiobutton(self, text="Farenheit", variable = self.tipoUnidad, value="F", command=self.selected).place(x=60, y=65)
        self.rb2 = ttk.Radiobutton(self, text="Celsius", variable = self.tipoUnidad, value="C",command=self.selected).place(x=60, y=85)
        
    
    def start(self):
        self.mainloop()
        
    
    def validateTemperature(self, *args):
        newTemp = self.temperatura.get()
        print("Nuevo valor:",newTemp, "vs valor anterior",self.__prevTemp)
        try:
            float(newTemp)
            self.__prevTemp = newTemp
            print("Fija valor anterior a:",self.__prevTemp)
        except:
            self.temperatura.set(self.__prevTemp)
            print("Volvemos al valor anterior:",self.__prevTemp)
    
    def selected(self,*args):
        resultado = 0
        toUnidad = self.tipoUnidad.get()
        grados = float(self.temperatura.get())
        if toUnidad == 'F':
            resultado = grados * 9/5 +32
        elif toUnidad == 'C':
            resultado = (grados -32) * 5/9
        else:
            resultado = grados
        self.temperatura.set(float("{:6.2f}".format(resultado)))
    

if __name__ == "__main__":
    app = MainApp()
    app.start()
