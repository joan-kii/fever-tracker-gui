from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtCore


# Elements

widgets: dict[str, list[str]] = {
    "logo": [] 
}

# Helpers

def clear_widgets():
    """
    Clear all the widget in the view
    :return: None
    """
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for _ in range(0, len(widgets[widget])):
            widgets[widget].pop()
            

# Frames

def frame_1():
    clear_widgets()
    image = QPixmap(".assets/logo.png")
