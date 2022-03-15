from tkinter import *

#akna seaded
aken = Tk()
aken.title('Käibemaksukalkulaator')
aken.geometry("400x250")

kast = Label(aken, text="Hind käibemaksuta:", font="Tahoma 12",)
kast.place(x=3,y=5)

määr = Label(aken, text="Käibemaksumäär:", font="Tahoma 12")
määr.place(x=3, y=45)

kriips = Label(aken, text="__________________________________________", font="Tahoma 12")
kriips.place(x=5, y=70)

maks = Label(aken, text="Käibemaks:", font="Tahoma 12")
maks.place(x=3, y=110)

hind2 = Label(aken, text="Hind käibemaksuga:", font="Tahoma 12")
hind2.place(x=3, y=140)

sisestus = Entry(aken)
sisestus.place(x=230, y=10)

var = IntVar()
nupp = Radiobutton(aken,text="9%", variable=var, value=1)
nupp.place(x=220, y=40)
nupp = Radiobutton(aken,text="20%", variable=var, value=2)
nupp.place(x=220, y=60)

ok = Button(aken, text="OK", font="Tahoma 12", command=OK)
ok.place(x=350, y=200)

#funktsioonid

hind = sisestus.get()



