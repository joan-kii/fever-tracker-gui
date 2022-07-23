from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QLineEdit # type: ignore
from PyQt5.QtGui import QCursor, QFont # type: ignore
from PyQt5 import QtCore # type: ignore


# Elements

widgets: dict[str, list[str]] = {
    "logo": [],
    "button_1": [],
    "button_2": [],
    "frame_title": [],
    "patient_name": []
}

# Grid

grid = QGridLayout()

# Helpers

def pipeline(txt: str) -> None:
    """
    Manage render frames
    :return: None
    """
    if txt == "Create Tracker":
        frame_2()

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
    button.setFixedWidth(300)
    button.setStyleSheet(
        "*{margin-left: " + str(l_margin) + "px;" +
        "margin-right: " + str(r_margin) + "px;" +
        """
        margin: 20px 0 100px;
        padding: 15px 0;
        color: white;
        font-family: 'Lucida Bright';
        font-size: 16px;
        border-radius: 25px;
        border: 4px solid '#ff595e';
        }
        *:hover{
            background: '#ff595e';
        }
        """
    )

    button.clicked.connect(lambda _: pipeline(button.text()))
    return button
            

# Frames

def frame_1():
    clear_widgets() 

    # Create logo
    logo = QLabel("Fever Tracker")
    logo.setFont(QFont("Lucida Handwriting"))
    logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    logo.setStyleSheet(
        """
        font-size: 40px; 
        font-weight: bold;
        color: "white"; 
        """
    )
    
    # Create buttons
    button_1 = create_button("Create Tracker", 10, 10)
    button_2 = create_button("Open Tracker", 10, 10)

    # Add widgets
    widgets["logo"].append(logo)
    widgets["button_1"].append(button_1)
    widgets["button_2"].append(button_2)

    # Add items to grid
    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button_1"][-1], 1, 0, 1, 1)
    grid.addWidget(widgets["button_2"][-1], 1, 1, 1, 1)


def frame_2():
    clear_widgets()

    frame_title = QLabel("Create Tracker")
    frame_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    frame_title.setStyleSheet(
        """
        font-size: 18px; 
        font-weight: bold;
        color: "white"; 
        """
    )

    patient_name = QLineEdit()
    # Seguir aquí (crear form create track)

    # Add widgets
    widgets["frame_title"].append(frame_title)
    widgets["patient_name"].append(patient_name)

    # Add items to grid
    grid.addWidget(widgets["frame_title"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["patient_name"][-1], 1, 0, 1, 2)
