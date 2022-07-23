import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout # type: ignore
from PyQt5.QtGui import QPixmap # type: ignore
from PyQt5 import QtGui, QtCore # type: ignore
from PyQt5.QtGui import QCursor # type: ignore

from gui import frame_1, grid


def main() -> None:

    """
    Create the Tkinter GUI
    :return: None
    """

    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Fever Tracker")
    window.setFixedWidth(1000)
    window.setFixedHeight(500)
    window.move(350, 200)
    window.setStyleSheet("background: #2a9d8f;")
    
    frame_1()
    window.setLayout(grid)
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
