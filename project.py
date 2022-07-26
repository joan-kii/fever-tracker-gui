import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

from gui import frame_1, main_layout, create_logo
from styles import styles


def main() -> None:

    """
    Create the Tkinter GUI
    :return: None
    """

    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Fever Tracker")
    window.setWindowIcon(QIcon("./assets/thermometer.png"))
    window.setFixedWidth(1000)
    window.setFixedHeight(500)
    window.move(350, 200)
    window.setStyleSheet(styles)
    
    create_logo()
    frame_1()
    window.setLayout(main_layout)
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
