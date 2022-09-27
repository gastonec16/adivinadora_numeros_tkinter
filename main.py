import tkinter as tk
from os import path
from time import strftime

carpeta = path.dirname(path.realpath(__file__)[0:-7])

ventana = tk.Tk()
ventana.title('Guasap')
ventana.geometry("480x640")
# ventana.resizable(0,0)


#region diccionarios

español={
    'c_1': 'Pensá un número de dos cifras (que no sean iguales)',
    'c_2': 'Invertí el orden de las cifras',
    'c_3': '¿El nuevo número es mayor o menor que el primero?',
    'c_4': 'Restá el número que pensaste del nuevo número',
    'c_5': 'Sumá las cifras del número que pensaste al principio',
    'c_6': 'Decime los números que obtuviste',
    'c_7': 'Pensaste el',
    'u_1': 'Ya está',
    'u_2': 'Es mayor',
    'u_3': 'Es menor',
    'u_4': 'el primero y',
    'u_5': 'el segundo',

    'en_linea': 'En línea'
}

colores_claro = {
    'arriba': '#008069',
    'letra_arriba': '#FFFFFF',
    'label_c': '#FFFFFF',
    'label_u': '#E7FFDB',
    'letra_chat': '#111B21',
    'hora': '#54656F',
    'fondo': '/img/fondo_claro.png',
    'carita': '/img/carita_clara.png'
}
colores_oscuro = {
    'arriba': '#202C33',
    'letra_arriba': '#E9EDEF',
    'label_c': '#202C33',
    'label_u': '#005C4B',
    'letra_chat': '#E9EDEF',
    'hora': '#8696A0',
    'fondo': '/img/fondo_oscuro.png',
    'carita': '/img/carita_oscura.png'
}

#endregion

#region variables

textos = español
colores = colores_claro

mensaje = tk.StringVar()
lista_chat_c = []
lista_chat_c = []

#endregion

#region labels_chat

lista_label_chat_c = []
lista_label_chat_u = []

hora = strftime('%H:%M')

img_fondo = tk.PhotoImage(file=carpeta+colores['fondo'])
img_visto = tk.PhotoImage(file=carpeta+'/img/visto.png')

label_fondo = tk.Label(ventana, image=img_fondo)
label_fondo.place(x = 0, y = 0)

class LabelChatC:
    def __init__(self, text, y):
        self.label_chat_c = tk.Label(ventana, text=text, bg=colores['label_c'], fg=colores['letra_chat'], font=('Calibri', 13))
        self.label_chat_c.place(x = 40, y = y, height=33)
        label_hora_c = tk.Label(ventana, text=hora, bg=colores['label_c'], fg=colores['hora'], font=('Calibri Bold', 8))
        label_hora_c.place(x = 9, y = y, width=31, height=33)

class LabelChatU:
    def __init__(self, text, y):
        label_chat_u = tk.Label(ventana, text=text, bg=colores['label_u'], fg=colores['letra_chat'], font=('Calibri', 13))
        label_chat_u.place(x = 422, y = y, height=33, anchor=tk.NE)

        label_visto = tk.Label(ventana, image=img_visto, bg=colores['label_u'])
        label_visto.place(x = 471, y = y, height=33, anchor=tk.NE)

        label_hora_u = tk.Label(ventana, text=hora, bg=colores['label_u'], fg=colores['hora'], font=('Calibri Bold', 8))
        label_hora_u.place(x = 453, y = y, width=31, height=33, anchor=tk.NE)

labelsita = LabelChatC(textos['c_1'], 256)

labelsita = LabelChatC(textos['c_5'], 320)

labelsita2 = LabelChatU('holiasdiasdasdlasdlasld', 295)

# for i in range(7):
#     labelsina = LabelChatC(str(i)+'asd'+textos['c_5'], 553 - i * 84)
#     lista_label_c.append(labelsina)

# for i in range(7):
#     labelsina = LabelChatU(str(i)+'asd'+textos['c_1'], 511 - i * 84)
#     lista_label_c.append(labelsina)

#inicializo labels de chat
for i in range(7):
    label_chat_c = LabelChatC('', -35 - i * 84)
    lista_label_chat_c.append(label_chat_c)

for i in range(7):
    label_chat_u = LabelChatU('', -77 - i * 84)
    lista_label_chat_c.append(label_chat_u)

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
entry_mensaje.place(x = 39, y = 635, width=400, height=40, anchor=tk.SW)

label_carita = tk.Label(ventana, image=img_carita, bg=colores['label_c'], justify='center')
label_carita.place(x = 5, y = 635, width=34, height=40, anchor=tk.SW)

button_enviar = tk.Button(ventana, image=img_enviar, bg=colores['label_c'], border=0)
button_enviar.place(x = 475, y = 635, height=40, anchor=tk.SE)

#endregion




ventana.mainloop()