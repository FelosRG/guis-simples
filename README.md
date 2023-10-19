# GUIS-SIMPLES
El proyecto **guis-simples**  nace de la necesidad de generar rápidamente apps en python para la creación de herramientas donde se requiera una interfaz más amigable que las aplicaciones basadas en consola.

Este proyecto **NO** es una librería si no más bien un conjunto de plantillas listas para ser personalizadas para convertirse en futuras herramientas prácticas para las tareas del trabajo.

* Plantillas compactas y simples para crear aplicaciones de un solo script.
* No requiere librerías externas pues solo usa *tkinter* 
* Implementación rápida de herramientas



## Guía de Implementación de herramientas

### Configuraciones globales
Cada una de las plantillas empiezan con una sección de variables de configuración globales que afectan al diseño y contenido de la app como el título de la ventana, la resolución inicial de la ventana, el estilo y tamaño de las fuentes utilizadas o la descripción de la app que se muestra en la aplicación.

``` py
TITULO = "Titulo de la ventana de la aplicación"
RESOLUCION = "300x500"
```

### Estructura de la aplicación

``` py

# Sección de configuraciones
# ...


import tkinter as tk

class Aplicacion():

    def __init__(self,):

        self.root = tk.Tk()
        # Contrucción de la interfaz gráfica.
        # (Esto ya está hecho en las plantillas)
        # ...
        self.root.mainloop()
        
    def script(self):
        # Espacio para escribir el código que ejecutará
        # la app por medio de un botón en la interfaz.
        # (Esto función es para que el usuario la implemente)
        # ...
        pass

    def printc(self, texto):
        "Imprime en la consoa de la aplicación"
        # Código de la función
        pass

    def printerror(self, texto):
        """
        Imprime en la consola con formato especial para
        indicar mensajes de error
        """
        # Código de la función
        pass


# Ejecutamos la aplicación
if __name__ == "__main__":
    app = Aplicacion()
```

