# Долгожитель
# Демонстрирует текстовое поле, текстовую область и менеджер размещения Grid

from tkinter import *


class Application(Frame):
    """GUI-приложение, владеющее секретом долголетия"""

    def __init__(self, master):
        """Инициализирует рамку"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Создает кнопку, текстовое поле и текстовую область"""
        # метка инструкция
        self.inst_lbl = Label(self, text = "Чтобы узнать секрет долголетия, введите пароль")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)



root = Tk()
root.title("Количество щелчков")
root.geometry("200x50")
app = Application(root)
root.mainloop()
