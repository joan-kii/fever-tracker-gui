from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtCore


# Elements

widgets: dict[str, list[str]] = {
    "logo": [],
    "logo_text": [],
    "button_1": [],
    "button_2": []
}

# Grid

grid = QGridLayout()

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

def create_button(txt: str, l_margin: int, r_margin: int) -> None:
    button = QPushButton(txt)
    button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(485)
    button.setStyleSheet(
        "*{margin-left: " + str(l_margin) + "px;" +
        "margin-right: " + str(r_margin) + "px;" +
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

    button.clicked.connect(lambda _: frame_2(button))
    return button
            

# Frames

def frame_1():
    clear_widgets() 

    # Create logo
    image = QPixmap("./assets/logo.png")
    image = image.scaled(80, 80, QtCore.Qt.KeepAspectRatio)
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    logo.setStyleSheet("margin-top: 60px;")

    # Create text logo
    logo_text = QLabel("Fever Tracker")
    logo_text.setStyleSheet(
        """
        font-family: 'Shanti'; 
        font-size: 25px; 
        color: 'white'; 
        margin: 100px 0px;
        """
    )
    
    # Create buttons
    button_1 = create_button("Create Tracker", 85, 5)
    button_2 = create_button("Open Tracker", 5, 85)

    # Add widgets
    widgets["logo"].append(logo)
    widgets["logo_text"].append(logo_text)
    widgets["button_1"].append(button_1)
    widgets["button_2"].append(button_2)

    # Add items to grid
    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 1)
    grid.addWidget(widgets["logo_text"][-1], 0, 1, 2, 1)
    grid.addWidget(widgets["button_1"][-1], 1, 0, 1, 1)
    grid.addWidget(widgets["button_2"][-1], 1, 1, 1, 1)


def frame_2():
    clear_widgets()
    image = QPixmap(".assets/logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)
