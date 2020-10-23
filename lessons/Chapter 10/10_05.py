# Киноман
# Демонстрирует применение флажков

from tkinter import *


class Application(Frame):
    """GUI-приложение, владеющее секретом долголетия"""

    def __init__(self, master):
        """Инициализирует рамку"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Создает элементы, с помощью которых пользователь будет выбирать."""
        # метка описание
        Label(self,
              text = "Укажите Ваши любимые жанры в кино"
              ).grid(row=0, column=0, sticky=W)

        # метка инструкция
        Label(self,
              text="Выберите все, что вам по вкусу:"
              ).grid(row=1, column=0, sticky=W)

root = Tk()
root.title("Долгожитель")
root.geometry("300x150")
app = Application(root)
root.mainloop()
