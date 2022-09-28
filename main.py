import tkinter as tk
from os import path
from time import strftime
from diccionarios import *
from tkinter import messagebox

carpeta = path.dirname(path.realpath(__file__)[0:-7])

ventana = tk.Tk()
ventana.title('Wasap')
ventana.geometry("480x640")
ventana.resizable(0,0)
ventana.iconphoto(False, tk.PhotoImage(file=carpeta+'/img/icono.png'))

#region variables

textos = español
colores = colores_claro
mensaje = tk.StringVar()
mensaje_strip = ''
lista_chat_c = []
paso = 0
chat_c = ''
posicion_chat = 0
primer_chat = 0
posiciones_label_chat_c = (553, 469, 385, 301, 217, 133, 49, 553, 469, 385, 301, 217, 133, 49)
posiciones_label_chat_u = (511, 427, 343, 259, 175, 91, 7, 511, 427, 343, 259, 175, 91, 7)
estados = [0, 0, 0, 0, 0, 0, 0]
tema = 0

#endregion

#region menu

def ver_foto():
    button_foto_grande.place(relx=0)
    button_foto.config(command=volver)
    entry_mensaje.config(state='disabled')
    button_enviar.config(state='disabled')
    button_reiniciar.config(state='disabled')

def volver():
    button_foto_grande.place(relx=1)
    button_foto.config(command=ver_foto)
    entry_mensaje.config(state='normal')
    button_enviar.config(state='normal')
    button_reiniciar.config(state='normal')

def cambiar_lenguaje():
    messagebox.showerror('Error', 'No hay otros idiomas instalados actualmente')

def cambiar_tema():
    global tema
    if tema == 0:
        colores = colores_oscuro
        tema = 1
    else:
        colores = colores_claro
        tema = 0

    label_superior.config(bg=colores['arriba'])
    button_foto.config(bg=colores['arriba'])
    button_foto_grande.config(bg=colores['arriba'])
    label_clotilde.config(bg=colores['arriba'])
    label_en_linea.config(bg=colores['arriba'])
    button_lenguaje.config(bg=colores['arriba'])
    button_tema .config(bg=colores['arriba'])
    button_reiniciar.config(bg=colores['arriba'])
    button_enviar.config(bg=colores['label_c'])
    img_fondo.config(file=carpeta+colores['fondo'])
    img_carita.config(file=carpeta+colores['carita'])
    label_carita.config(bg=colores['label_c'])
    entry_mensaje.config(bg=colores['label_c'], fg=colores['letra_chat'], insertbackground=colores['letra_chat'], disabledbackground=colores['label_c'], disabledforeground=colores['letra_chat'], )

    for i in lista_label_chat_c[0]:
        i.config(bg=colores['label_c'], fg=colores['letra_chat'])

    for i in lista_label_chat_c[1]:
        i.config(bg=colores['label_c'], fg=colores['hora'])

    for i in lista_label_chat_u[0]:
        i.config(bg=colores['label_u'], fg=colores['letra_chat'])

    for i in lista_label_chat_u[1]:
        i.config(bg=colores['label_u'], fg=colores['hora'])

    for i in lista_label_chat_u[2]:
        i.config(bg=colores['label_u'])

def reiniciar():
    global paso
    if estados[0] != 0:
        entry_mensaje.delete(0, tk.END)
        mensaje_strip = textos['reiniciar']
        entry_mensaje.insert(0, mensaje_strip)
        estados[1] = 1
        paso = 1
        enviar()
        estados[1] = 0

def enviar():
    global mensaje_strip
    mensaje_strip = mensaje.get().strip().lower()
    if mensaje_strip != '':
        match paso:
            case 0:
                paso_0(estados[0])
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

def enviar_mensaje(event):
    enviar()

#endregion

#region funciones

def actualizar_chat(c):
    global posicion_chat
    global primer_chat

    hora = strftime('%H:%M')

    if primer_chat > -1:
        lista_label_chat_c[0][primer_chat].place(relx=0)
        lista_label_chat_c[1][primer_chat].place(relx=0)

        lista_label_chat_u[0][primer_chat].place(relx=0)
        lista_label_chat_u[1][primer_chat].place(relx=0)
        lista_label_chat_u[2][primer_chat].place(relx=0)

        if primer_chat == 0:
            primer_chat = 7
        primer_chat -= 1

    lista_label_chat_c[0][posicion_chat].configure(text=c)
    lista_label_chat_c[1][posicion_chat].configure(text=hora)

    lista_label_chat_u[0][posicion_chat].configure(text=entry_mensaje.get())
    lista_label_chat_u[1][posicion_chat].configure(text=hora)
        
    for i in range(7):
        lista_label_chat_c[0][i].place(y = posiciones_label_chat_c[i-posicion_chat+7])
        lista_label_chat_c[1][i].place(y = posiciones_label_chat_c[i-posicion_chat+7])

        lista_label_chat_u[0][i].place(y = posiciones_label_chat_u[i-posicion_chat+7])
        lista_label_chat_u[1][i].place(y = posiciones_label_chat_u[i-posicion_chat+7])
        lista_label_chat_u[2][i].place(y = posiciones_label_chat_u[i-posicion_chat+7])

    if posicion_chat == 0:
        posicion_chat = 6
    else:
        posicion_chat -= 1

    entry_mensaje.delete(0, tk.END)

def verificar_palabras(texto, palabras):
    for i in palabras:
        if texto == i:
            return True
    else:
        return False

def paso_0(estado):
    global paso
    actualizar_chat(textos['c_0' + str(estado)])
    estados[0] = 1
    paso = 1

def paso_1():
    global paso
    if verificar_palabras(mensaje_strip, ['sí', 'si', 'no']) or mensaje_strip == textos['reiniciar'].lower():
        if mensaje_strip == 'sí' or mensaje_strip == 'si' or mensaje_strip == textos['reiniciar'].lower():
            actualizar_chat(textos['c_1'+str(estados[1])])
            paso = 2
        else:
            paso = 0
            estados[0] = 0
            actualizar_chat(textos['c_12'])
    else:
        actualizar_chat(textos['c_13'])
        
def paso_2():
    global paso
    actualizar_chat(textos['c_20'])
    paso = 3

def paso_3():
    global paso
    actualizar_chat(textos['c_30'])
    paso = 4

def paso_4():
    global paso
    if verificar_palabras(mensaje_strip, ['mayor', 'es mayor', 'menor', 'es menor']):
        if mensaje_strip == 'mayor' or mensaje_strip == 'es mayor':
            actualizar_chat(textos['c_40'])
            estados[4] = 1
            paso = 5
        else:
            actualizar_chat(textos['c_41'])
            estados[4] = 2
            paso = 5
    else:
        actualizar_chat(textos['c_42'])

def paso_5():
    global paso
    try:
        if int(mensaje_strip) < 99 and int(mensaje_strip) > 0:
            actualizar_chat(textos['c_50'])
            estados[5] = int(mensaje_strip)
            paso = 6
        else:
            actualizar_chat(textos['c_51'])
    except:
        actualizar_chat(textos['c_52'])

def paso_6():
    global paso
    try:
        if int(mensaje_strip) < 18 and int(mensaje_strip) > 2:
            estados[6] = int(mensaje_strip)

            num_0 = int((estados[5]) / 9)
            num_1 = int((estados[6] - num_0) / 2)
            num_2 = int((estados[6] + num_0) / 2)

            if estados[4] == 1:
                numero_adivinado = str(num_1) + str(num_2)
            else:
                numero_adivinado = str(num_2) + str(num_1)

            actualizar_chat(textos['c_60'] + numero_adivinado)
            paso = 0
        else:
            actualizar_chat(textos['c_61'])
    except:
        actualizar_chat(textos['c_62'])

#endregion

img_fondo = tk.PhotoImage(file=carpeta+colores['fondo'])
img_visto = tk.PhotoImage(file=carpeta+'/img/visto.png')

label_fondo = tk.Label(ventana, image=img_fondo)
label_fondo.place(x = -2, y = 0)

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

label_hora_c_0 = tk.Label(ventana, text='', bg=colores['label_c'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_c_1 = tk.Label(ventana, text='', bg=colores['label_c'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_c_2 = tk.Label(ventana, text='', bg=colores['label_c'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_c_3 = tk.Label(ventana, text='', bg=colores['label_c'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_c_4 = tk.Label(ventana, text='', bg=colores['label_c'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_c_5 = tk.Label(ventana, text='', bg=colores['label_c'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_c_6 = tk.Label(ventana, text='', bg=colores['label_c'], fg=colores['hora'], font=('Calibri Bold', 8))

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

label_hora_u_0 = tk.Label(ventana, text='', bg=colores['label_u'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_u_1 = tk.Label(ventana, text='', bg=colores['label_u'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_u_2 = tk.Label(ventana, text='', bg=colores['label_u'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_u_3 = tk.Label(ventana, text='', bg=colores['label_u'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_u_4 = tk.Label(ventana, text='', bg=colores['label_u'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_u_5 = tk.Label(ventana, text='', bg=colores['label_u'], fg=colores['hora'], font=('Calibri Bold', 8))
label_hora_u_6 = tk.Label(ventana, text='', bg=colores['label_u'], fg=colores['hora'], font=('Calibri Bold', 8))

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
    label_chat_u_1,
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
img_foto_grande = tk.PhotoImage(file=carpeta+'/img/foto_grande.png')
img_lenguaje = tk.PhotoImage(file=carpeta+'/img/lenguaje.png')
img_reiniciar = tk.PhotoImage(file=carpeta+'/img/reiniciar.png')
img_tema = tk.PhotoImage(file=carpeta+'/img/tema.png')
img_carita = tk.PhotoImage(file=carpeta+colores['carita'])

label_superior = tk.Label(ventana, bg=colores['arriba'])
label_superior.place(x = 0, y = 0, width=480, height=57)

button_foto = tk.Button(ventana, image=img_foto, bg=colores['arriba'], cursor='hand2', border=0, command=ver_foto)
button_foto.place(x = 13, y = 7)

button_foto_grande = tk.Button(ventana, bg=colores['arriba'], image=img_foto_grande, border=0, cursor='hand2', command=volver)
button_foto_grande.place(x = 240, y = 112, anchor=tk.N, relx=1)

label_clotilde = tk.Label(ventana, text='Clotilde', bg=colores['arriba'], fg=colores['letra_arriba'], font=('Calibri Bold', 15))
label_clotilde.place(x = 60, y = 11)

label_en_linea = tk.Label(ventana, text=textos['en_linea'], bg=colores['arriba'], fg=colores['letra_arriba'], font=('Calibri', 10))
label_en_linea.place(x = 61, y = 33)

button_lenguaje = tk.Button(ventana, image=img_lenguaje, bg=colores['arriba'], border=0, cursor='hand2', command=cambiar_lenguaje)
button_lenguaje.place(x = 379, y = 29, width=22, anchor=tk.E)

button_tema = tk.Button(ventana, image=img_tema, bg=colores['arriba'], border=0, cursor='hand2', command=cambiar_tema)
button_tema.place(x = 423, y = 29, width=22, anchor=tk.E)

button_reiniciar = tk.Button(ventana, image=img_reiniciar, bg=colores['arriba'], border=0, cursor='hand2', command=reiniciar)
button_reiniciar.place(x = 467, y = 29, width=22, anchor=tk.E)

entry_mensaje = tk.Entry(ventana, textvariable=mensaje, bg=colores['label_c'], fg=colores['letra_chat'], disabledbackground=colores['label_c'], disabledforeground=colores['letra_chat'], insertbackground=colores['letra_chat'], font=('Calibri', 14), border=0)
entry_mensaje.bind('<Return>', enviar_mensaje)
entry_mensaje.place(x = 39, y = 635, width=394, height=40, anchor=tk.SW)

label_carita = tk.Label(ventana, image=img_carita, bg=colores['label_c'], justify='center')
label_carita.place(x = 5, y = 635, width=34, height=40, anchor=tk.SW)

button_enviar = tk.Button(ventana, image=img_enviar, bg=colores['label_c'], border=0, command=enviar, cursor='hand2')
button_enviar.place(x = 475, y = 635, height=40, anchor=tk.SE)

#endregion

ventana.mainloop()