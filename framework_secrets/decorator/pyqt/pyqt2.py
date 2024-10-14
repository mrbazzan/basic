
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QListWidget
)


def bind(widget):
    def decorator(func):
        widget.clicked.connect(lambda: func(widget))
        return func
    return decorator


if __name__ == "__main__":
    app = QApplication([])

    frame = QWidget()
    frame.setWindowTitle("Event binding with decorators")

    layout = QHBoxLayout()

    lb = QListWidget()
    for i, s in enumerate(['one', 'two', 'three', 'four']):
        lb.insertItem(i, s)

    layout.addWidget(lb)
    frame.setLayout(layout)

    @bind(lb)
    def onselect(evt):
        index = evt.currentItem().listWidget().currentRow()
        value = evt.currentItem().text()
        print(f"You selected item {index}: {value}")

    frame.show()
    sys.exit(app.exec())


