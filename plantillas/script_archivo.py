# CONFIGURACIONES DE LA VENTANA DE LA APLICACIÓN

NOMBRE_DEL_PROGRAMA = "Título de la app"
DESCRIPCION = """ Aquí va la descripción de lo que hace el script """
RESOLUCION = "700x520"

FONT_SECCIONES = "Helvetica 14 bold"
FONT_NORMAL    = "Helvetica 11"
FONT_BOLD      = "Helvetica 11 bold"

# -------------------------------------
#--------------------------------------
import pathlib
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()

class Aplicacion():
    """
    Define la aplicación principal
    """
    def __init__(self) -> None:

        self.root = tk.Tk()
        self.path_archivo = None # Tomará el path al indicarlo con el archivo.

        # Configuraciones básicas
        self.root.geometry(RESOLUCION)

        # Label Descripción
        self.label_descripcion = tk.Label(
            self.root, 
            text = "Descripción",
            font = FONT_SECCIONES,
        )
        self.label_descripcion.pack(side=tk.TOP,pady=(10, 5))

        # TextBox Descripción
        self.text_descripcion = tk.Text(
            self.root, height=7, width=80,
            font= FONT_NORMAL,
        )
        self.text_descripcion.pack(side=tk.TOP,pady=(5, 10))
        self.text_descripcion.insert("1.0",DESCRIPCION)
        self.text_descripcion.configure(state="disable")
        
        # Botón seleccionar archivo
        self.boton_archivo = tk.Button(
            self.root, 
            text = "Seleccionar Archivo",
            command = self.seleccionar_archivo,
            font= FONT_BOLD,
        )
        self.boton_archivo.pack(side=tk.TOP, pady=(10, 3))

        # Entry donde se coloca el archivo seleccionado
        self.entry_archivo = tk.Entry(
            self.root, width=80,
            font = FONT_NORMAL,
        )
        self.entry_archivo.pack(side=tk.TOP, pady=(3, 10))
        
        # Botón de ejecutar script
        self.boton_script = tk.Button(
            self.root, 
            text = "Ejecutar script",
            command = self.script,
            font = FONT_BOLD,
        )
        self.boton_script.pack(side=tk.TOP, pady=(10, 10))

        # Label consola
        self.label_consola = tk.Label(
            self.root, 
            text = "Consola",
            font = FONT_SECCIONES,
        )
        self.label_consola.pack(side=tk.TOP, pady=(10, 0))

        # Texto consola
        self.consola = tk.Text(
            self.root, height=7, width=75,
            bg = "black" , fg = "white",
            font= FONT_NORMAL,
            wrap = "word", 
        )
        self.consola.pack(side=tk.LEFT, expand=True, pady=(0, 10))

        # Condiguramos tags
        self.consola.tag_config("error", foreground="red")

        # Scrollbar consola
        self.scroll_bar_consola = tk.Scrollbar(self.root)
        self.scroll_bar_consola.pack(side=tk.RIGHT,fill=tk.BOTH, pady=(10, 10))
        self.consola.config(yscrollcommand=self.scroll_bar_consola.set)
        self.scroll_bar_consola.config(command=self.consola.yview)
        

        # Definimos aquí variables de la aplicación
        # ...
        # ...
        # ------------------------------------------
        
        self.root.mainloop()

    def script(self) -> None:
        """
        Script que será ejecutado al presionar el botón.
        """
        if self.path_archivo is None:
            messagebox.showerror("Error", "No se ha seleccionado un archivo.")
        else:
            pass
            
            # Definimos aquí el script
            # ...
            # ...
            # ------------------------

    def seleccionar_archivo(self) -> None:
        self.path_archivo = askopenfilename(initialdir=str(SCRIPT_DIR))
        self.entry_archivo.config(state="normal")
        self.entry_archivo.delete(0,tk.END)
        self.entry_archivo.insert(0,self.path_archivo)
        self.entry_archivo.config(state="readonly")
        
    def printc(self, texto, end:str="\n") -> None:
        """
        Imprime en la consola de la aplicación
        """
        self.consola.insert(tk.END, str(texto) + end)
        self.consola.yview_moveto("1.0")

    def printerror(self, texto) -> None:
        self.consola.insert(tk.END, str(texto) + "\n", "error")
        self.consola.yview_moveto("1.0")



if __name__ == "__main__":
    app = Aplicacion()