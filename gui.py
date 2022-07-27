from cProfile import label
import os
from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, 
    QDialogButtonBox, QLabel, QPushButton, QLineEdit,
    QVBoxLayout, QListWidget, QTableWidget, QTableWidgetItem,
    QMessageBox)
from PyQt5.QtGui import QCursor
from PyQt5 import QtCore

from functions import new_track, open_track, add_row, convert_track


# Main Layout
main_layout = QVBoxLayout()


# Header Layout
header = QHBoxLayout()
header.setAlignment(QtCore.Qt.AlignTop)

# Row layout
row_layout = QHBoxLayout()

# Grid
grid = QGridLayout()
grid.setRowMinimumHeight(0, 50)

# Form
form = QFormLayout()

# List
list_layout = QVBoxLayout() 


# Helpers

def create_button(txt, fn, file=None,):

    """
    Create buttons
    :return: None
    """

    button = QPushButton(txt)
    button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(300)
    if file:
        button.clicked.connect(lambda _: fn(file))
    else:
        button.clicked.connect(lambda _: fn())

    return button
            
# Create logo

def create_logo():

    """
    Create logo
    :return: None
    """

    logo = logo = QLabel("Fever Tracker")
    logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    logo.setStyleSheet(
        """
        font-family: 'Lucida Handwriting';
        font-size: 40px; 
        font-weight: bold;
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

# Convert to pdf

def convert_to_pdf(file):

    """
    Convert track to pdf an alert the user
    :return: None 
    """

    convert_track(file)

    msg = QMessageBox()
    msg.setText("PDF created!")
    msg.setIcon(QMessageBox.Information)

    # Add message to layout
    main_layout.addWidget(msg)


# Frames

def frame_1():

    """
    Render frame 1 - main view
    :return: None
    """

    delete_widgets()
    
    # Create buttons
    button_1 = create_button("Create Tracker", frame_2)
    button_2 = create_button("Open Tracker", frame_3)

    # Add items to grid
    grid.addWidget(button_1, 0, 0)
    grid.addWidget(button_2, 0, 1)
    grid.setContentsMargins(0, 0, 0, 200)

    # Add layout to main layout
    main_layout.addLayout(grid)


def frame_2():

    """
    Render frame 2 - create new tracker form
    :return: None
    """

    delete_widgets()

    # Create Form
    form_title = QLabel("Create Tracker")
    form_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    form_title.setStyleSheet(
        """
        margin-bottom: 40px;
        font-size: 22px;
        """
    )
    form.addRow(form_title)

    name = QLineEdit()
    name.setFixedWidth(320)
    label_name = QLabel("Patient Name: ")
    label_name.setFixedWidth(120)
    label_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
    form.addRow(label_name, name)

    temp = QLineEdit()
    temp.setFixedWidth(320)
    label_temp = QLabel("Temperature: ")
    label_temp.setFixedWidth(120)
    label_temp.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
    form.addRow(label_temp, temp)

    medicine = QLineEdit()
    medicine.setFixedWidth(320)
    label_medicine = QLabel("Medicine: ")
    label_medicine.setFixedWidth(120)
    label_medicine.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
    form.addRow(label_medicine, medicine)

    dose = QLineEdit()
    dose.setFixedWidth(320)
    label_dose = QLabel("Dose: ")
    label_dose.setFixedWidth(120)
    label_dose.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
    form.addRow(label_dose, dose)

    def get_info():
        new_track(name.text(), temp.text(), medicine.text(), dose.text())
        frame_1()

    button_group = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    button_group.setCenterButtons(True)
    button_group.setStyleSheet("width: 300px;")
    button_group.button(QDialogButtonBox.Ok).setText("Create")
    button_group.accepted.connect(get_info)
    button_group.rejected.connect(frame_1)
    form.addRow(button_group)

    # Add layout to main layout
    form.setContentsMargins(250, 0, 250, 50)
    main_layout.addLayout(form)

# Frame 3

def frame_3():

    """
    Render frame 3 - choose csv file to open
    :return: None
    """

    delete_widgets()

    # Get csv files
    csv_files = os.listdir("./csv_files/")
    csv_files_formatted = []

    for csv_file in csv_files:
        new_csv_filename = csv_file.strip(".csv").split("_")
        new_csv_filename = new_csv_filename[0].title() + " " + new_csv_filename[1]
        csv_files_formatted.append(new_csv_filename)
    
    def open_csv_file(list_item):
        file_to_open = list_item.text().split(" ")
        file_to_open = file_to_open[0].lower() + "_" + file_to_open[1] + ".csv"
        frame_4(file_to_open)


    # Create csv files list
    list_widget = QListWidget()
    list_widget.setFixedSize(500, 300)
    list_widget.addItems(csv_files_formatted)
    list_widget.itemClicked.connect(open_csv_file)

    # Create Cancel button
    cancel_button = create_button("Cancel", frame_1)

    # Add widgets to layouts
    list_layout.addWidget(list_widget)
    list_layout.setContentsMargins(250, 0, 250, 30)
    row_layout.addWidget(cancel_button)
    
    # Add layout to main layout
    main_layout.addLayout(list_layout)
    main_layout.addLayout(row_layout)


# Frame 4

def frame_4(file):

    """
    Render frame 4 - data table and add row/convert to pdf options
    :return: None
    """

    # Seguir aquí (styles table y add row)

    delete_widgets()

    data = open_track(file)

    # Create table
    table = QTableWidget()
    table.setRowCount(len(data) - 1)
    table.setColumnCount(len(data[0]))

    header_labels = []
    for column_header in data[0]:
        header_labels.append(column_header)

    # Delete headers before loop over data
    data.pop(0)
    for x, row in enumerate(data):
        for y, cell in enumerate(row):
            cell_data = QTableWidgetItem(cell)
            table.setItem(x, y, cell_data)

    table.setHorizontalHeaderLabels(header_labels)
    table.resizeColumnsToContents()
    table.resizeRowsToContents()

    # Create buttons
    add_row_button = create_button("Add temperature", frame_5, file=file)
    convert_to_pdf_button = create_button("Convert to pdf", convert_to_pdf, file=file)
    cancel = create_button("Cancel", frame_1)

    # Add widget to layout
    list_layout.addWidget(table)
    row_layout.addWidget(add_row_button)
    row_layout.addWidget(convert_to_pdf_button)
    row_layout.addWidget(cancel)

    # Add layout to main layout
    main_layout.addLayout(list_layout)
    main_layout.addLayout(row_layout)


# Frame 5

def frame_5(file):
    
    """
    Render add row form
    :return: None  
    """

    delete_widgets()

    # Create Form
    form_title = QLabel("Add Temperature")
    form_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    form_title.setStyleSheet(
        """
        font-size: 18px;
        """
    )
    form.addRow(form_title)
    temp = QLineEdit()
    label_temp = QLabel("Temperature: ")
    form.addRow(label_temp, temp)

    medicine = QLineEdit()
    label_medicine = QLabel("Medicine: ")
    form.addRow(label_medicine, medicine)

    dose = QLineEdit()
    label_dose = QLabel("Dose: ")
    form.addRow(label_dose, dose)

    def get_info():
        add_row(file, temp.text(), medicine.text(), dose.text())
        frame_4(file)

    button_group = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    button_group.accepted.connect(get_info)
    button_group.rejected.connect(frame_1)
    form.addRow(button_group)

    # Add layout to main layout
    main_layout.addLayout(form)
