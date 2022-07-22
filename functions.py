from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtCore


# Elements

widgets: dict[str, list[str]] = {
    "logo": [] 
}

# Helpers

def clear_widgets() -> None:
    """
    Clear all the widget in the view
    :return: None
    """
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for _ in range(0, len(widgets[widget])):
            widgets[widget].pop()

def create_buttons(txt: str, l_margin: int, r_margin: int) -> None:
    button = QPushButton(txt)
    button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(485)
    button.setStyleSheet(
        """
        border: 4px solid '#ff595e';
        color: white;
        font-family: 'shanti';
        font-size: 16px;
        border-radius: 25px;
        padding: 15px 0;
        margin-top: 20px;
        }
        *:hover{
            background: '#ff595e';
        }
        """
    )

    button.clicked
            

# Frames

def frame_1():
    clear_widgets()
    image = QPixmap(".assets/logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)


