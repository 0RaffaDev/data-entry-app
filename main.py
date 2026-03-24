import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook


version = "1.0.0"


#Crear Libro de Excel
wb = Workbook()
ws = wb.active
ws.append(["Nombre", "Apellido", "Edad", "Correo Electrónico"])
wb.save("datos.xlsx")

#Crear ventana principal
root = tk.Tk()

root.title("Formulario de Datos")
root.geometry("600x500")
root.configure(padx=20, pady=20, bg="#f0f0f0")

#Centrar la ventana en la pantalla
root.update_idletasks()

width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2
)
root.geometry(f"{width}x{height}+{x}+{y}")

#Establecer ícono de la aplicación (opcional)
#root.iconbitmap("icono.ico")  # Asegúrate de tener un archivo de ícono válido

#Configurar estilos
root.option_add("*Font", "Arial 12")
root.option_add("*Background", "#f0f0f0")

#Configurar colores
root.configure(bg="#f0f0f0")

#Configurar fuentes
root.option_add("*Font", "Arial 12")
#Configurar bordes
root.option_add("*Entry.BorderWidth", 2)
root.option_add("*Entry.Relief", "groove")

#Configurar tamaños
root.option_add("*Entry.Width", 30)
#Configurar colores de fondo
root.option_add("*Entry.Background", "#000000")
#Configurar colores de texto
root.option_add("*Entry.Foreground", "#ffffff")
#Configurar colores de botones
root.option_add("*Button.Background", "#4CAF50")
#Configurar colores de texto en botones
root.option_add("*Button.Foreground", "white")



#Estilos
label_style = {"font": ("Arial", 12), "bg": "#f0f0f0"}
entry_style = {"font": ("Arial", 12), "width": 30, "bd": 2, "relief": "groove", "bg": "#000000"}

#Crear widgets
label_nombre = tk.Label(root, text="Nombre:", **label_style)
entry_nombre = tk.Entry(root, **entry_style)
label_apellido = tk.Label(root, text="Apellido:", **label_style)
entry_apellido = tk.Entry(root, **entry_style)
label_edad = tk.Label(root, text="Edad:", **label_style)
entry_edad = tk.Entry(root, **entry_style)
label_correo = tk.Label(root, text="Correo Electrónico:", **label_style)
entry_correo = tk.Entry(root, **entry_style,  fg="#ffffff")
version_label = tk.Label(root, text=f"Versión: {version}", font=("Arial", 10), bg="#f0f0f0", fg="#888888")

#Función para guardar datos en Excel
def guardar_datos():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    correo = entry_correo.get()

    if not nombre or not apellido or not edad or not correo:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    ws.append([nombre, apellido, edad, correo])
    wb.save("datos.xlsx")
    messagebox.showinfo("Éxito", "Datos guardados correctamente.")
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
#Crear función para validar edad (opcional)
def validar_edad(event):
    edad = entry_edad.get()
    if not edad.isdigit():
        messagebox.showerror("Error", "Por favor, ingrese un número válido para la edad.")
        entry_edad.delete(0, tk.END)
entry_edad.bind("<FocusOut>", validar_edad)


#Crear botón para guardar datos
button_guardar = tk.Button(root, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", command=guardar_datos)


#Mostrar widgets
label_nombre.pack(pady=5)
entry_nombre.pack(pady=5)
label_apellido.pack(pady=5)
entry_apellido.pack(pady=5)
label_edad.pack(pady=5)
entry_edad.pack(pady=5)
label_correo.pack(pady=5)
entry_correo.pack(pady=5)
button_guardar.pack(pady=20)
version_label.pack(side=tk.BOTTOM, pady=10)



#Iniciar la aplicación
root.mainloop()