from random import choice as cho
from tkinter import Button as but, Label as lab, Entry as ent, mainloop, Tk as Tk
from pyperclip import copy

root = Tk()
root.geometry("650x500+430+150")
root.title("PasswordsGenerator [Versión 1.1]")

ini = lab(root,text='>>>Ingrese la cantidad de caracteres que tendra la contraseña<<<',fg='black')
ini.place(x=125,y=20)

number = ent(root, bg='white',fg='black')
number.place(x=230,y=50)

def generator(num):
    result = ''
    text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$*"-_=.,:;/\\|~`\'()[]{}'

    for i in range(int(num)):
        result += cho(text)
    return result

def click():
    try:
        textR = generator(number.get())
        text = lab(root,text=f'the password was generated successfully',fg='blue')
        text.place(x=180,y=170)
    except:
        textX = lab(root,text=f'ERROR: Usted solo puede ingresar numeros, Por favor vuelva a intentarlo',fg='red')
        textX.place(x=120,y=170)

    result = ent(root,bg='white',fg='black',width=50)
    result.insert(0,textR)
    result.place(x=170,y=200)

    copyx = lambda text: copy(text)
    butC = but(root,text='Copy',command=copyx(textR))
    butC.place(x=275,y=225)

button = but(root,text='Trigger', command=click)
button.place(x=260,y=80)

root.mainloop()