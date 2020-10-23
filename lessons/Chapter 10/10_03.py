# Счетчик щелчков
# Демонстрирует связывание событий с обработчиками

from tkinter import *

class Application(Frame):
    """GUI-приложение, которое подсчитывает количество нажатий кнопок"""
    def __init__(self, master):
        """Инициализирует рамку"""
        super(Application, self).__init__(master)
        self.grid()
