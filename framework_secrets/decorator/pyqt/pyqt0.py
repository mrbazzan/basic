
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QPushButton
)


def onclick():
    print("You clicked a button")


if __name__ == "__main__":
    app = QApplication([])

    frame = QWidget()
    frame.setWindowTitle("Event binding with decorators")

    layout = QHBoxLayout()

    btn1 = QPushButton("Left")
    btn2 = QPushButton("Right")

    btn1.clicked.connect(onclick)
    btn2.clicked.connect(onclick)

    layout.addWidget(btn1)
    layout.addWidget(btn2)

    frame.setLayout(layout)

    frame.show()
    sys.exit(app.exec())

