from PyQt5.QtGui import QLinearGradient


styles = """
    QWidget{
        background: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #036666, stop: 1 #99e2b4);
        font-family: 'Lucida Typewriter';
    }
    QLabel{
        background: transparent;
        font-size: 16px;
        color: 'white';
    }
    QPushButton{
        margin-left: 10px;
        margin-right: 10px;
        padding: 15px 0;
        color: white;
        font-size: 20px;
        border-radius: 20px;
        background: #1a936f;
    }
    QPushButton:hover{
        background: '#114b5f';
    }
    QLineEdit{
        margin-bottom: 10px;
        padding: 4px 8px;
        width: 150px;
        background-color: 'white';
        border-radius: 5px;
    }
"""