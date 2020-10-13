# Простейший GUI
# Демнострирует создание окна
from tkinter import *

root = Tk()
root.title("Бесполезные кнопки")
root.geometry("100x100")
app = Frame(root)
app.grid()
bttn = Button(app, text="Я ничего не делаю!")
bttn.grid()
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text="И я тоже!")
bttn3 = Button(app)
bttn3.grid()
bttn3.configure(text="И я !")
root.mainloop()
