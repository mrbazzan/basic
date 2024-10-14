
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QPushButton
)


class MyButton(QPushButton):
    def command(self, func):
        # the callable passed to connect accepts
        # no argument this is why we use a partial
        # callable defined with lambda
        self.clicked.connect(lambda: func(self))
        return func


if __name__ == "__main__":
    app = QApplication([])

    frame = QWidget()
    frame.setWindowTitle("Event binding with decorators")

    layout = QHBoxLayout()

    btn1 = MyButton("Left")
    btn2 = MyButton("Right")

    layout.addWidget(btn1)
    layout.addWidget(btn2)

    frame.setLayout(layout)

    @btn1.command
    @btn2.command
    def onclick(target):
        print(f"You clicked on button <{target.text()}>")

    frame.show()
    sys.exit(app.exec())

