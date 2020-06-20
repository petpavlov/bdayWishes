#author Petar Pavlov ot 5a klas

from tkinter import *

#
root = Tk()
root.resizable(0, 0)
root.title("Happy B-day, Ines")


#images
#root.iconbitmap(default="icon.ico")
home = PhotoImage(file=".img\\home.png")
icon = PhotoImage(file=".img\\cake.png")
icon1 = PhotoImage(file=".img\\cake1.png")
icon2 = PhotoImage(file=".img\\cake2.png")
icon3 = PhotoImage(file=".img\\cake3.png")


#home
Label(root, image=home).grid(row=0, column=0, columnspan=4)
Label(root, text="You have new birthday wishes from",
      font="Ariel 25 bold", fg="white", bg="pink", wraplength=600).grid(row=0, column=0, columnspan=4, sticky=S)
Label(root, text="HAPPY BIRTHDAY!!",
      font="Ariel 25 bold", fg="white", bg="pink", wraplength=600).grid(row=0, column=0, columnspan=4, sticky=N)


#wishes
def whishesNikola():
    Label(root, image=icon).grid(row=0, column=0, columnspan=4)
    Label(root, text="Създавай приложения без стрес,\n"
                     "В предизвикателства кодиран е твоят прогрес.\n"
                     "Но друга е тематиката днес,\n"
                     "Честит рожден ден Инес!!!\n"
                     "Бъде вдъхновяваща с финес,\n"
                     "А в гаража чисто нов мерцедес!!!\n"
                     "\n"
                     "Към втори куплет залитам,\n"
                     "Продължавай танцувай в ритъм!\n"
                     "Определи на играта правилата,\n"
                     "щастлива ти е съдбата!\n"
                     "Сама си нагласи месечната заплата,\n"
                     "по-голяма от средногодишната в страната.",
          font="Ariel 16 bold", bg="pink", fg="blue", wraplength=700)\
        .grid(row=0, column=0, columnspan=4, sticky=S)

def whishesStoyan():
    Label(root, image=icon1).grid(row=0, column=0, columnspan=4)
    Label(root, text=""
                     "<head>\n"
                     "<title> Честит рожден ден !!! </title>\n"
                     "<body>\n"
                     "Бъди най-вече жива и здрава!(некоронясана \U0001f451 \U0001f37a)\n"
                     "Остани все така усмихната и красива!\n"
                     "Останалото ще си го вземеш!\n"
                     "</body>\n"
                     "</head>",
          font="Ariel 17 bold", fg="purple", bg="pink", wraplength=800, justify=LEFT)\
        .grid(row=0, column=0, columnspan=4, sticky=S)

def whishesVenci():
    Label(root, image=icon2).grid(row=0, column=0, columnspan=4)
    Label(root, text="Честит Рожден Ден, бате! Искам най-вече да си жива и здрава "
                     "и чисто по детски много щастлива! Нови дестинации, нови кодове "
                     "и веселооо прекарване !!! \U0001f4af \U0001f382 \N{double exclamation mark}",
          font="Ariel 18 bold", fg="black", bg="white", wraplength=600)\
        .grid(row=0, column=0, columnspan=4, sticky=S)

def whishesPetar():
    Label(root, image=icon3).grid(row=0, column=0, columnspan=4)
    Label(root, text="Още един цикъл на земята, още един age++; \U0001f604 \n"
                     "Пожелавам ти да научиш още нови и интересни неща "
                     "и да успееш да ги предадеш на другите! \U0001f4d6",
          font="Ariel 18 bold", fg="brown", bg="white", wraplength=600).grid(row=0, column=0, columnspan=4, sticky=S)


#buttons
btn_Nikola = Button(root, text="Никола", command=whishesNikola, padx=5, pady=5).grid(row=1, column=0)
btn_Stoyan = Button(root, text="Стоян", command=whishesStoyan, padx=5, pady=5).grid(row=1, column=1)
btn_Venci = Button(root, text="Венци", command=whishesVenci, padx=5, pady=5).grid(row=1, column=2)
btn_Petar = Button(root, text="Петър", command=whishesPetar, padx=5, pady=5).grid(row=1, column=3)


root.mainloop()