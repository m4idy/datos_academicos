from tkinter import *
from tkinter import messagebox, ttk

ventana_principal = Tk() 

# titulo de la ventana
ventana_principal.title("Infome estudiantil")

# tamaño de la ventana en pixeles
ventana_principal.geometry("600x600")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg="white")

#-----------------------------
# variables de crontol
#-----------------------------
ed = ["15", "16", "17", "18", "19", "20","21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38","39", "40"]
ed_selected = StringVar()

nombre= StringVar()
edad= StringVar()

#-----------------------------
# Frame entrada datos
#-----------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white" , width=580 , height=180)
frame_entrada.place(x=10 , y=10)

cmb_kf = ttk.Combobox(frame_entrada, textvariable=ed_selected, values=ed, font=("Helvetica", 12))
cmb_kf.place(x=80, y=125 , width=80 , height=20)

# logo de la app
logo = PhotoImage(file="img\informe medico.png") 
lb_logo = Label(frame_entrada, image=logo, bg="white" )
lb_logo.place(x=11, y=20)

# etiqueta para el titulo
lb_titulo = Label(frame_entrada, text="INFORME ESTUDIANTIL")
lb_titulo.config(bg="white", fg="purple", font=("hervetica", 20))
lb_titulo.place(x=240, y=10)

# etiqueta para el primer numero
lb_nombre = Label(frame_entrada, text="NOMBRE: ")
lb_nombre.config(bg="white", fg="light green", font=("hervetica", 20))
lb_nombre.place(x=200, y=60)

# caja de texto (Entry) para el primer numero
Entry_nombre=Entry(frame_entrada, textvariable=nombre)
Entry_nombre.config(bg= "white", fg="green", font=("courier",20))
Entry_nombre.focus_set()
Entry_nombre.place(x=330, y=60, width=100, height=30)

cmb_kf = ttk.Combobox(frame_entrada, textvariable=ed_selected, values=ed, font=("Helvetica", 12))
cmb_kf.place(x=300, y=100 , width=100 , height=30)

# etiqueta para el segundo numero
lb_edad = Label(frame_entrada, text="EDAD: ")
lb_edad.config(bg="white", fg="light green", font=("hervetica", 20))
lb_edad.place(x=200, y=100)



ventana_principal.mainloop()