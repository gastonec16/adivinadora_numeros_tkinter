import tkinter as tk
from os import path
from time import strftime
from diccionarios import *

carpeta = path.dirname(path.realpath(__file__)[0:-7])

ventana = tk.Tk()
ventana.title('Guasap')
ventana.geometry("480x640")
# ventana.resizable(0,0)

#region variables

textos = español
colores = colores_claro

hora = strftime('%H:%M')
mensaje = tk.StringVar()
lista_chat_c = []
lista_chat_c = []
paso = 0
chat_c = ''
posicion_chat = 0
primer_chat = 0

#endregion

#region funciones

def actualizar_chat(u, c):
    global posicion_chat
    global primer_chat

    if primer_chat <= 6:
        lista_label_chat_c[0][primer_chat].place(relx=0)
        lista_label_chat_c[1][primer_chat].place(relx=0)

        lista_label_chat_u[0][primer_chat].place(relx=0)
        lista_label_chat_u[1][primer_chat].place(relx=0)
        lista_label_chat_u[2][primer_chat].place(relx=0)

        primer_chat += 1

    for i in range(posicion_chat, posicion_chat+7):
        if i == posicion_chat:
            lista_label_chat_c[0][posicion_chat].configure(text=c)
            lista_label_chat_c[1][posicion_chat].configure(text=hora)

            lista_label_chat_u[0][posicion_chat].configure(text=u)
            lista_label_chat_u[1][posicion_chat].configure(text=hora)
        
        lista_label_chat_c[0][i-posicion_chat].configure(text=c)
        lista_label_chat_c[0][i-posicion_chat].place(y = 553-(i-posicion_chat)*84)
        lista_label_chat_c[1][i-posicion_chat].configure(text=hora)
        lista_label_chat_c[1][i-posicion_chat].place(y = 553-(i-posicion_chat)*84)

        lista_label_chat_u[0][i-posicion_chat].configure(text=u)
        lista_label_chat_u[0][i-posicion_chat].place(y = 511-(i-posicion_chat)*84)
        lista_label_chat_u[1][i-posicion_chat].configure(text=hora)
        lista_label_chat_u[1][i-posicion_chat].place(y = 511-(i-posicion_chat)*84)
        lista_label_chat_u[2][i-posicion_chat].place(y = 511-(i-posicion_chat)*84)

    print(posicion_chat)
    if posicion_chat >= 6:
        posicion_chat = 0
    else:
        posicion_chat += 1

def paso_0():
    chat_c = textos['saludo']
    # lista_label_chat_c[posicion_chat] = chat_c
    actualizar_chat(entry_mensaje.get(), chat_c)

def paso_1():
    pass

def paso_2():
    pass

def paso_3():
    pass

def paso_4():
    pass

def paso_5():
    pass

def paso_6():
    pass

def paso_7():
    pass

def paso_8():
    pass

def paso_9():
    pass

def paso_10():
    pass

def enviar():
    mensaje_strip = mensaje.get().strip()
    if mensaje_strip != '':
        match paso:
            case 0:
                paso_0()
            case 1:
                paso_1()
            case 2:
                paso_2()
            case 3:
                paso_3()
            case 4:
                paso_4()
            case 5:
                paso_5()
            case 6:
                paso_6()
            case 7:
                paso_7()
            case 8:
                paso_8()
            case 9:
                paso_9()
            case 10:
                paso_10()


img_fondo = tk.PhotoImage(file=carpeta+colores['fondo'])
img_visto = tk.PhotoImage(file=carpeta+'/img/visto.png')

label_fondo = tk.Label(ventana, image=img_fondo)
label_fondo.place(x = 0, y = 0)

#region labels_chat

label_chat_c_0 = tk.Label(ventana, text='', bg=colores['label_c'], fg=colores['letra_chat'], font=('Calibri', 13))
label_chat_c_1 = tk.Label(ventana, text='', bg=colores['label_c'], fg=colores['letra_chat'], font=('Calibri', 13))
label_chat_c_2 = tk.Label(ventana, text='', bg=colores['label_c'], fg=colores['letra_chat'], font=('Calibri', 13))
label_chat_c_3 = tk.Label(ventana, text='', bg=colores['label_c'], fg=colores['letra_chat'], font=('Calibri', 13))
label_chat_c_4 = tk.Label(ventana, text='', bg=colores['label_c'], fg=colores['letra_chat'], font=('Calibri', 13))
label_chat_c_5 = tk.Label(ventana, text='', bg=colores['label_c'], fg=colores['letra_chat'], font=('Calibri', 13))
label_chat_c_6 = tk.Label(ventana, text='', bg=colores['label_c'], fg=colores['letra_chat'], font=('Calibri', 13))

label_chat_c_0.place(x = 40, height=33, relx=1)
label_chat_c_1.place(x = 40, height=33, relx=1)
label_chat_c_2.place(x = 40, height=33, relx=1)
label_chat_c_3.place(x = 40, height=33, relx=1)
label_chat_c_4.place(x = 40, height=33, relx=1)
label_chat_c_5.place(x = 40, height=33, relx=1)
label_chat_c_6.place(x = 40, height=33, relx=1)

label_hora_c_0 = tk.Label(ventana, text=hora, bg=colores['label_c'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_c_1 = tk.Label(ventana, text=hora, bg=colores['label_c'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_c_2 = tk.Label(ventana, text=hora, bg=colores['label_c'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_c_3 = tk.Label(ventana, text=hora, bg=colores['label_c'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_c_4 = tk.Label(ventana, text=hora, bg=colores['label_c'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_c_5 = tk.Label(ventana, text=hora, bg=colores['label_c'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_c_6 = tk.Label(ventana, text=hora, bg=colores['label_c'], fg=colores['hora'], font=('Calibri Bold', 8))

label_hora_c_0.place(x = 9, width=31, height=33, relx=1)
label_hora_c_1.place(x = 9, width=31, height=33, relx=1)
label_hora_c_2.place(x = 9, width=31, height=33, relx=1)
label_hora_c_3.place(x = 9, width=31, height=33, relx=1)
label_hora_c_4.place(x = 9, width=31, height=33, relx=1)
label_hora_c_5.place(x = 9, width=31, height=33, relx=1)
label_hora_c_6.place(x = 9, width=31, height=33, relx=1)

label_chat_u_0 = tk.Label(ventana, text='', bg=colores['label_u'], fg=colores['letra_chat'], font=('Calibri', 13))
label_chat_u_1 = tk.Label(ventana, text='', bg=colores['label_u'], fg=colores['letra_chat'], font=('Calibri', 13))
label_chat_u_2 = tk.Label(ventana, text='', bg=colores['label_u'], fg=colores['letra_chat'], font=('Calibri', 13))
label_chat_u_3 = tk.Label(ventana, text='', bg=colores['label_u'], fg=colores['letra_chat'], font=('Calibri', 13))
label_chat_u_4 = tk.Label(ventana, text='', bg=colores['label_u'], fg=colores['letra_chat'], font=('Calibri', 13))
label_chat_u_5 = tk.Label(ventana, text='', bg=colores['label_u'], fg=colores['letra_chat'], font=('Calibri', 13))
label_chat_u_6 = tk.Label(ventana, text='', bg=colores['label_u'], fg=colores['letra_chat'], font=('Calibri', 13))

label_chat_u_0.place(x = 422, height=33, anchor=tk.NE, relx=1)
label_chat_u_1.place(x = 422, height=33, anchor=tk.NE, relx=1)
label_chat_u_2.place(x = 422, height=33, anchor=tk.NE, relx=1)
label_chat_u_3.place(x = 422, height=33, anchor=tk.NE, relx=1)
label_chat_u_4.place(x = 422, height=33, anchor=tk.NE, relx=1)
label_chat_u_5.place(x = 422, height=33, anchor=tk.NE, relx=1)
label_chat_u_6.place(x = 422, height=33, anchor=tk.NE, relx=1)

label_hora_u_0 = tk.Label(ventana, text=hora, bg=colores['label_u'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_u_1 = tk.Label(ventana, text=hora, bg=colores['label_u'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_u_2 = tk.Label(ventana, text=hora, bg=colores['label_u'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_u_3 = tk.Label(ventana, text=hora, bg=colores['label_u'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_u_4 = tk.Label(ventana, text=hora, bg=colores['label_u'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_u_5 = tk.Label(ventana, text=hora, bg=colores['label_u'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_u_6 = tk.Label(ventana, text=hora, bg=colores['label_u'], fg=colores['hora'], font=('Calibri Bold', 8))

label_hora_u_0.place(x = 453, width=31, height=33, anchor=tk.NE, relx=1)
label_hora_u_1.place(x = 453, width=31, height=33, anchor=tk.NE, relx=1)
label_hora_u_2.place(x = 453, width=31, height=33, anchor=tk.NE, relx=1)
label_hora_u_3.place(x = 453, width=31, height=33, anchor=tk.NE, relx=1)
label_hora_u_4.place(x = 453, width=31, height=33, anchor=tk.NE, relx=1)
label_hora_u_5.place(x = 453, width=31, height=33, anchor=tk.NE, relx=1)
label_hora_u_6.place(x = 453, width=31, height=33, anchor=tk.NE, relx=1)

label_visto_0 = tk.Label(ventana, image=img_visto, bg=colores['label_u'])
label_visto_1 = tk.Label(ventana, image=img_visto, bg=colores['label_u'])
label_visto_2 = tk.Label(ventana, image=img_visto, bg=colores['label_u'])
label_visto_3 = tk.Label(ventana, image=img_visto, bg=colores['label_u'])
label_visto_4 = tk.Label(ventana, image=img_visto, bg=colores['label_u'])
label_visto_5 = tk.Label(ventana, image=img_visto, bg=colores['label_u'])
label_visto_6 = tk.Label(ventana, image=img_visto, bg=colores['label_u'])

label_visto_0.place(x = 471, height=33, anchor=tk.NE, relx=1)
label_visto_1.place(x = 471, height=33, anchor=tk.NE, relx=1)
label_visto_2.place(x = 471, height=33, anchor=tk.NE, relx=1)
label_visto_3.place(x = 471, height=33, anchor=tk.NE, relx=1)
label_visto_4.place(x = 471, height=33, anchor=tk.NE, relx=1)
label_visto_5.place(x = 471, height=33, anchor=tk.NE, relx=1)
label_visto_6.place(x = 471, height=33, anchor=tk.NE, relx=1)

lista_label_chat_c = [[
    label_chat_c_0,
    label_chat_c_1,
    label_chat_c_2,
    label_chat_c_3,
    label_chat_c_4,
    label_chat_c_5,
    label_chat_c_6
], [
    label_hora_c_0,
    label_hora_c_1,
    label_hora_c_2,
    label_hora_c_3,
    label_hora_c_4,
    label_hora_c_5,
    label_hora_c_6
]]

lista_label_chat_u = [[
    label_chat_u_0,
    label_hora_u_1,
    label_chat_u_2,
    label_chat_u_3,
    label_chat_u_4,
    label_chat_u_5,
    label_chat_u_6
], [
    label_hora_u_0,
    label_hora_u_1,
    label_hora_u_2,
    label_hora_u_3,
    label_hora_u_4,
    label_hora_u_5,
    label_hora_u_6
], [
    label_visto_0,
    label_visto_1,
    label_visto_2,
    label_visto_3,
    label_visto_4,
    label_visto_5,
    label_visto_6
]]

#endregion

#region base

img_enviar = tk.PhotoImage(file=carpeta+'/img/enviar.png')
img_foto = tk.PhotoImage(file=carpeta+'/img/foto.png')
img_lenguaje = tk.PhotoImage(file=carpeta+'/img/lenguaje.png')
img_reiniciar = tk.PhotoImage(file=carpeta+'/img/reiniciar.png')
img_tema = tk.PhotoImage(file=carpeta+'/img/tema.png')
img_carita = tk.PhotoImage(file=carpeta+colores['carita'])

label_superior = tk.Label(ventana, bg=colores['arriba'])
label_superior.place(x = 0, y = 0, width=480, height=57)

label_foto = tk.Label(ventana, image=img_foto, bg=colores['arriba'])
label_foto.place(x = 13, y = 7)

label_clotilde = tk.Label(ventana, text='Clotilde', bg=colores['arriba'], fg=colores['letra_arriba'], font=('Calibri Bold', 15))
label_clotilde.place(x = 60, y = 11)

label_en_linea = tk.Label(ventana, text=textos['en_linea'], bg=colores['arriba'], fg=colores['letra_arriba'], font=('Calibri', 10))
label_en_linea.place(x = 61, y = 33)

button_lenguaje = tk.Button(ventana, image=img_lenguaje, bg=colores['arriba'], border=0)
button_lenguaje.place(x = 379, y = 29, width=22, anchor=tk.E)

button_tema = tk.Button(ventana, image=img_tema, bg=colores['arriba'], border=0)
button_tema.place(x = 423, y = 29, width=22, anchor=tk.E)

button_reiniciar = tk.Button(ventana, image=img_reiniciar, bg=colores['arriba'], border=0)
button_reiniciar.place(x = 467, y = 29, width=22, anchor=tk.E)

entry_mensaje = tk.Entry(ventana, textvariable=mensaje, bg=colores['label_c'], fg=colores['letra_chat'], font=('Calibri', 14), border=0)
entry_mensaje.place(x = 39, y = 635, width=394, height=40, anchor=tk.SW)

label_carita = tk.Label(ventana, image=img_carita, bg=colores['label_c'], justify='center')
label_carita.place(x = 5, y = 635, width=34, height=40, anchor=tk.SW)

button_enviar = tk.Button(ventana, image=img_enviar, bg=colores['label_c'], border=0, command=enviar)
button_enviar.place(x = 475, y = 635, height=40, anchor=tk.SE)

#endregion





ventana.mainloop()