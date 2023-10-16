import tkinter as tk

#Importamos la biblioteca Tkinter bajo el alias tk para facilitar el acceso a sus funciones y clases.

def abrir_archivo():
    pass

def guardar_archivo():
    pass

def salir():
    pato.quit()

#Se definen tres funciones: abrir_archivo(), guardar_archivo(), y salir().
#Estas funciones se ejecutarán cuando se seleccionen las opciones del menú "Abrir", "Guardar" y "Salir", 
#respectivamente. En este código, las funciones no hacen nada (tienen la declaración pass), 
#por lo que debes reemplazar el cuerpo de estas funciones con el codigo que deseas ejecutar.

pato = tk.Tk()
pato.title("Barra de Menú")

#Se crea la ventana principal de la aplicación y se le asigna el título "Barra de Menú".

menubar = tk.Menu(pato)
pato.config(menu=menubar)

#Se crea un objeto Menu llamado menubar que actúa como la barra de menú de la ventana principal. 
#Luego, configuramos la ventana principal para utilizar esta barra de menú mediante root.config(menu=menubar)

archivo_menu = tk.Menu(menubar)
menubar.add_cascade(label="Archivo", menu=archivo_menu)

#Se crea un menú desplegable llamado "Archivo" y se lo agrega a la barra de menú principal. 
#La función add_cascade() se utiliza para agregar el menú "Archivo" a la barra de menú.

archivo_menu.add_command(label="Abrir", command=abrir_archivo)
archivo_menu.add_command(label="Guardar", command=guardar_archivo)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=salir)

#Se agregan opciones al menú "Archivo". 
#Cada opción tiene una etiqueta ("Abrir", "Guardar", "Salir") y una función asociada (command) 
#que se ejecutará cuando se seleccione la opción. En este caso, las funciones abrir_archivo(), 
#guardar_archivo(), y salir() se asignan a estas opciones.

ayuda_menu = tk.Menu(menubar)
menubar.add_cascade(label="Ayuda", menu=ayuda_menu)
ayuda_menu.add_command(label="Acerca de")

#Se agrega una única opción, 
#"Acerca de", al menú "Ayuda". En este caso, no se asigna una función a esta opción.

pato.mainloop()

#El bucle principal de la aplicación se inicia, 
#permitiendo que la ventana de la aplicación y la barra de menú sean interactivas.