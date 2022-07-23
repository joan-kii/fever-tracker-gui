from turtle import mainloop
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QPushButton, QLineEdit # type: ignore
from PyQt5.QtGui import QCursor, QFont # type: ignore
from PyQt5 import QtCore


# Elements

widgets: dict[str, list[str]] = {
    "button_1": [],
    "button_2": [],
    "frame_title": [],
    "patient_name_label": [],
    "patient_name_field": [],
}

# Main Layout

main_layout = QVBoxLayout()


# Header Layout

header = QHBoxLayout()
header.setAlignment(QtCore.Qt.AlignTop)


# Grid

grid = QGridLayout()
grid.setRowMinimumHeight(0, 50)


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
            
# Create logo

def create_logo():
    logo = logo = QLabel("Fever Tracker")
    logo.setFont(QFont("Lucida Handwriting"))
    logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    logo.setStyleSheet(
        """
        font-size: 40px; 
        font-weight: bold;
        color: "white"; 
        """
    )
    
    header.addWidget(logo)

# Frames

def frame_1():
    clear_widgets() 
    create_logo()
    
    # Create buttons
    button_1 = create_button("Create Tracker", 10, 10)
    button_2 = create_button("Open Tracker", 10, 10)

    # Add widgets
    widgets["button_1"].append(button_1)
    widgets["button_2"].append(button_2)

    # Add items to grid
    grid.addWidget(widgets["button_1"][-1], 1, 0)
    grid.addWidget(widgets["button_2"][-1], 1, 1)

    # Add layouts to main layout
    main_layout.addLayout(header)
    main_layout.addLayout(grid)


def frame_2():
    clear_widgets()

    # Seguir aquí (crear form y cambiar grid por form, crear gitignore)
    # Create Form
    frame_title = QLabel("Create Tracker")
    frame_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    frame_title.setStyleSheet(
        """
        font-size: 18px; 
        font-weight: bold;
        color: "white"; 
        """
    )

    patient_name_label = QLabel("Patient Name: ")
    patient_name_field = QLineEdit()

    # Add widgets
    widgets["frame_title"].append(frame_title)
    widgets["patient_name_label"].append(patient_name_label)
    widgets["patient_name_field"].append(patient_name_field)

    # Add items to layout
    grid.addWidget(widgets["frame_title"][-1])
    grid.addWidget(widgets["patient_name_label"][-1], 1, 0)
    grid.addWidget(widgets["patient_name_field"][-1], 1, 1)
