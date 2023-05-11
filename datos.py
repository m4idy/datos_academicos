from tkinter import *
from tkinter import messagebox, ttk

def abrir_datos():
    if AM.get()=="medico":
        global toplevel_datos_medicos
        toplevel_datos_medicos = Toplevel()
        toplevel_datos_medicos.title("Datos medicos")
        toplevel_datos_medicos.resizable(False, False)
        toplevel_datos_medicos.geometry("500x600")
        toplevel_datos_medicos.config(bg="white")
        
        # etiqueta para nombre
        lb_c = Label(toplevel_datos_medicos, text = "Nombre = ")
        lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
        lb_c.place(x=30, y=30)
        # caja de texto para nombre
        entry_c = Entry(toplevel_datos_medicos,textvariable=c)
        entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6) 
        entry_c.focus_set()
        entry_c.place(x=100,y=50)
        # etiqueta para edad
        lb_h= Label(toplevel_datos_medicos, text = "Edad = ")
        lb_h.config(bg="white", fg="blue", font=("Helvetica", 18))
        lb_h.place(x=30, y=60)
        # caja de texto edad
        entry_h = Entry(toplevel_datos_medicos,textvariable=c)
        entry_h.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6) 
        entry_h.focus_set()
        entry_h.place(x=210,y=60)
        # etiqueta para peso
        lb_k = Label(toplevel_datos_medicos, text = "peso = ")
        lb_k.config(bg="white", fg="blue", font=("Helvetica", 18))
        lb_k.place(x=30, y=90)
        # caja de texto peso
        entry_k = Entry(toplevel_datos_medicos, textvariable=c)
        entry_k.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6) 
        entry_k.focus_set()
        entry_k.place(x=210,y=60)
        # etiqueta para altura
        lb_p = Label(toplevel_datos_medicos, text = "altura = ")
        lb_p.config(bg="white", fg="blue", font=("Helvetica", 18))
        lb_p.place(x=30, y=120)
        # caja de texto altura
        entry_p = Entry(toplevel_datos_medicos, textvariable=c)
        entry_p.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6) 
        entry_p.focus_set()
        entry_p.place(x=210,y=60)
        # boton para convertir
        bt_aceptar = Button(toplevel_datos_medicos,text="Aceptar", command=aceptar)
        bt_aceptar.place(x=100, y=150, width=100, height=30)
    elif AM.get()=="academico":
        global toplevel_datos_academicos
        toplevel_datos_academicos = Toplevel()
        toplevel_datos_academicos.title("Datos Academicos")
        toplevel_datos_academicos.resizable(False, False)
        toplevel_datos_academicos.geometry("300x200")
        toplevel_datos_academicos.config(bg="white")
    
    else:
        t_resultados.insert(INSERT, "Debe seleccionar una opción")

# aceptar
def aceptar():
    global cent
    cent = int(c.get())
    cent = int(c.get())
    toplevel_datos_medicos.destroy()


def analizar():
    return
def borrar():
   messagebox.showinfo("Informe estudiantil", "Los datos serán borrados")
   t_resultados.delete("1.0","end")
   
def salir():
    messagebox.showinfo("Informe estudiantil", "La app se va a cerrar")
    ventana_principal.destroy()


ventana_principal = Tk() 

# titulo de la ventana
ventana_principal.title("Infome estudiantil")

# tamaño de la ventana en pixeles
ventana_principal.geometry("600x600")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg="grey")

AM=StringVar()
c=StringVar()

#-----------------------------
# Frame entrada datos
#-----------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white" , width=580 , height=180)
frame_entrada.place(x=10 , y=10)
# logo de la app
logo = PhotoImage(file="img\informemedico.png") 
lb_logo = Label(frame_entrada, image=logo, bg="white" )
lb_logo.place(x=11, y=20)

# etiqueta para el titulo
lb_titulo = Label(frame_entrada, text="INFORME ESTUDIANTIL")
lb_titulo.config(bg="white", fg="purple", font=("hervetica", 20))
lb_titulo.place(x=240, y=10)

# radiobutton para kelvin
rb_m = Radiobutton(frame_entrada, text="Informe medico", variable=AM, value="medico")
rb_m.config(bg="white", fg="red", font=("Times new roman", 18))
rb_m.place(x=240, y=70)

# radiobutton para farenheit
rb_a = Radiobutton(frame_entrada, text="Informe academico", variable=AM, value="academico")
rb_a.config(bg="white", fg="red", font=("Times new roman", 18))
rb_a.place(x=240, y=110)

#--------------------------------
# frame operaciones
#--------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=580, height=120)
frame_operaciones.place(x=10, y=200)

# boton para convertir
bt_datos = Button(frame_operaciones,text="Datos", command= abrir_datos)
bt_datos.place(x=25, y=35, width=100, height=30)

# boton para convertir
bt_analizar = Button(frame_operaciones,text="Analizar", command=analizar)
bt_analizar.place(x=170, y=35, width=100, height=30)

# boton para convertir
bt_borrar = Button(frame_operaciones,text="borrar", command=borrar)
bt_borrar.place(x=315, y=35, width=100, height=30)

# boton para convertir
bt_salir = Button(frame_operaciones,text="Salir", command=salir)
bt_salir.place(x=460, y=35, width=100, height=30)

#--------------------------------
# frame resultados
#--------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=580, height=250)
frame_resultados.place(x=10, y=340)

# area de texto para los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="green yellow", font=("Courier", 18))
t_resultados.place(x=10,y=10,width=555,height=230)


ventana_principal.mainloop()