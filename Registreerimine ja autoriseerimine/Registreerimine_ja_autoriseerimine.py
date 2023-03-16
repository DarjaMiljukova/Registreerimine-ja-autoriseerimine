from random import*
from string import*
import string
from tkinter import *

users = {"juhataja": "parool"}

def cha_pass():
    user = entry_username.get()
    old_passw = entry_passw.get()
    new_passw = entry_passw.get()

    if user not in users:
        lbl_status.config(text='Kasutajanime ei leitud.')
    elif users[user] != old_passw:
        lbl_status.config(text='Vale salasõna.')
    else:
        users[user] = new_passw
        lbl_status.config(text='Salasõna muutmine õnnestus.')

def validate_input():
    user = entry_username.get()
    passw = entry_passw.get()
    if not user:
        lbl_status.config(text='Kasutajanimi ei tohi olla tühi.')
        return False
    elif not passw:
        lbl_status.config(text='Parool ei tohi olla tühi.')
        return False
    elif len(passw) < 8:
        lbl_status.config(text='Parool peab olema vähemalt 8 tähemärki pikk.')
        return False
    elif not any(c.isupper() for c in passw):
        lbl_status.config(text='Parool peab sisaldama vähemalt ühte suurtähte.')
        return False
    elif not any(c.islower() for c in passw):
        lbl_status.config(text='Parool peab sisaldama vähemalt ühte väiketähte.')
        return False
    elif not any(c.isdigit() for c in passw):
        lbl_status.config(text='Parool peab sisaldama vähemalt ühte numbrit.')
        return False
    elif not any(c in string.punctuation for c in passw):
        lbl_status.config(text='Parool peab sisaldama vähemalt ühte erimärki.')
        return False
    else:
        lbl_status.config(text='')
        return True

def registreemi():
    if not validate_input():
        return
    user = entry_username.get()
    passw = entry_passw.get()
    if user in users:
        lbl_status.config(text='Kasutajanimi on juba võetud.')
    else:
        users[user] = passw
        lbl_status.config(text='Kasutaja registreerimine õnnestus.')

def log():
    if not validate_input():
        return
    user = entry_username.get()
    passw = entry_passw.get()
    if user not in users:
        lbl_status.config(text='Kasutajanime ei leitud.')
    elif users[user] != passw:
        lbl_status.config(text='Vale salasõna.')
    else:
        lbl_status.config(text='Sisselogimine õnnestus.')

def gen_pass():
    while True:
        length = 12
        chars = string.ascii_letters + string.digits + string.punctuation
        parool = "".join(random.choice(chars) for _ in range(length))
        if (any(char.isupper() for char in parool) and
            any(char.islower() for char in parool) and
            any(char.isdigit() for char in parool) and
            any(char in string.punctuation for char in parool)):
            entry_passw.delete(0, END)
            entry_passw.insert(0, parool)
            break

def rec_pass():
    user = entry_username.get()
    if user not in users:
        lbl_status.config(text='Kasutajanime ei leitud.')
    else:
        parool = users[user]
        lbl_status.config(text=f'Sinu parool on {parool}.')

def cha_pass():

    if not validate_input():
        return
    user = entry_username.get()
    passw = entry_passw.get()
    if user not in users:
        lbl_status.config(text='Kasutajanime ei leitud.')
    else:
        users[user] = passw
        lbl_status.config(text='Salasõna muutmine õnnestus.')



aken = Tk()
aken.geometry("600x600")
aken.title("Registreerimine ja autoriseerimine")

lbl_username = Label(aken, text="Kasutajanimi: ", font="Arial 20", bg="mediumslateblue")
lbl_username.pack(pady=8)
entry_username = Entry(aken, font="Arial 20", bg="slategrey", fg="darkslateblue")
entry_username.pack()

lbl_pass = Label(aken, text="Salasõna: ", font="Arial 20", bg="mediumslateblue")
lbl_pass.pack(pady=8)
entry_passw = Entry(aken, show="*", font="Arial 20", bg="slategrey", fg="darkslateblue")
entry_passw.pack()

btn_reg = Button(aken, text="Registreerimine", command=registreemi, font="Arial 20", bg="mediumslateblue")
btn_reg.pack(pady=10)
btn_login = Button(aken, text="Logi sisse", command=log, font="Arial 20", bg="mediumslateblue")
btn_login.pack()



btn_generate = Button(aken, text="Parooli loomine", command=gen_pass, font="Arial 20", bg="mediumslateblue")
btn_generate.pack(pady=10)

btn_recover = Button(aken, text="Parooli taastamine", command=rec_pass, font="Arial 20", bg="mediumslateblue")
btn_recover.pack(pady=10)

btn_change = Button(aken, text="Muuda salasõna", command=cha_pass, font="Arial 20", bg="mediumslateblue")
btn_change.pack(pady=10)

aken.config(bg="midnightblue")
aken.mainloop()
