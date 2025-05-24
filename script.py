import tkinter as tk
from tkinter import ttk
datos = []
# Definición de la clase Aplicacion
class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurar la ventana principal
        self.title("Aplicación con múltiples pantallas")

        # Configurar el tamaño de la ventana
        self.geometry("400x500")

        # Crear contenedor de pantallas
        self.frames = {}

        # Crear pantallas
        for F in (Pantalla1, Pantalla2):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_pantalla(Pantalla1)

    def mostrar_pantalla(self, pantalla):
        frame = self.frames[pantalla]
        frame.tkraise()

class Pantalla1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Pantalla 1").pack(pady=20)

        def actualizar_tabla():
            # Limpiar la tabla antes de actualizar
            
            for item in tabla.get_children():
                tabla.delete(item)

            # Insertar nuevos datos
 
            for fila in datos:
                tabla.insert("", "end", values=fila)

            print(datos)

        tabla = ttk.Treeview(self, columns=("Nombre", "Edad"), show="headings")

        # Definir encabezados
        tabla.heading("Nombre", text="Nombre")
        tabla.heading("Edad", text="Edad")
        
        # Insertar datos
       
        for fila in datos:
            tabla.insert("", "end", values=fila)

        # Mostrar tabla
        tabla.pack(expand=True, fill="both")
        tk.Button(self, text="Refrescar tabla", command=actualizar_tabla).pack(pady=10)
        tk.Button(self, text="Formulario", command=lambda: master.mostrar_pantalla(Pantalla2)).pack()
 

class Pantalla2(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        def enviar_datos():
            datos.append((entry_nombre.get(), int(entry_edad.get())))
            nombre = entry_nombre.get()
            edad = entry_edad.get()
            print(f"Nombre: {nombre}, Edad: {edad}")

        # Etiquetas y campos de entrada
        tk.Label(self, text="Nombre:").pack(padx=10, pady=5)
        entry_nombre = tk.Entry(self)
        entry_nombre.pack(padx=10, pady=5)

        tk.Label(self, text="Edad:").pack(padx=10, pady=5)
        entry_edad = tk.Entry(self)
        entry_edad.pack(padx=10, pady=5)

  
        tk.Button(self, text="Enviar", command=enviar_datos).pack(pady=10)

        tk.Button(self, text="Tabla", command=lambda: master.mostrar_pantalla(Pantalla1)).pack()


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()