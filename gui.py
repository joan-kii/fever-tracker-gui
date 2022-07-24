from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QDialogButtonBox, QLabel, QPushButton, QLineEdit # type: ignore
from PyQt5.QtGui import QCursor, QFont # type: ignore
from PyQt5 import QtCore

from functions import new_track


# Main Layout
main_layout = QVBoxLayout()


# Header Layout
header = QHBoxLayout()
header.setAlignment(QtCore.Qt.AlignTop)


# Grid
grid = QGridLayout()
grid.setRowMinimumHeight(0, 50)

# Form
form = QFormLayout()


# Helpers

def pipeline(txt: str):

    """
    Manage render frames
    :return: None
    """
    if txt == "Create Tracker":
        frame_2()
    elif txt == "home":
        frame_1()


def create_button(txt: str, l_margin: int, r_margin: int):

    """
    Create buttons
    :return: None
    """

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

    """
    Create logo
    :return: None
    """

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
    main_layout.addLayout(header)

# Delete layouts

def delete_widgets():

    """
    Hide the widgets and delete the layouts
    :return: None
    """

    if main_layout is not None:
        while main_layout.count() > 1:
            current_layout = main_layout.takeAt(1)
            while current_layout.count():
                current_widget = current_layout.takeAt(0).widget()
                if current_widget is not None:
                    current_widget.hide()
                else:
                    current_layout.deleteLater()


# Frames

def frame_1():

    """
    Render frame 1
    :return: None
    """

    delete_widgets()
    
    # Create buttons
    button_1 = create_button("Create Tracker", 10, 10)
    button_2 = create_button("Open Tracker", 10, 10)

    # Add items to grid
    grid.addWidget(button_1, 0, 0)
    grid.addWidget(button_2, 0, 1)

    # Add layout to main layout
    main_layout.addLayout(grid)


def frame_2():

    """
    Render frame 2
    :return: None
    """

    delete_widgets()

    # Create Form
    form_title = QLabel("Create Tracker")
    form_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    form_title.setStyleSheet(
        """
        font-size: 18px; 
        font-weight: bold;
        color: "white"; 
        """
    )
    form.addRow(form_title)
    name = QLineEdit()
    form.addRow(QLabel("Patient Name: "), name)

    temp = QLineEdit()
    form.addRow(QLabel("Temperature: "), temp)

    medicine = QLineEdit()
    form.addRow(QLabel("Medicine: "), medicine)

    dose = QLineEdit()
    form.addRow(QLabel("Dose: "), dose)

    def get_info():
        new_track(name.text(), temp.text(), medicine.text(), dose.text())
        frame_1()

    button_group = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    button_group.accepted.connect(get_info)
    button_group.rejected.connect(frame_1)
    form.addRow(button_group)

    # Add layouts to main layout
    main_layout.addLayout(form)

# Seguir aquí (crear frame_3, open track)