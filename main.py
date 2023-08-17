from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon, QFontDatabase
import keyboard
import pyautogui
from PyQt5.QtCore import Qt

QFontDatabase.addApplicationFont(":/fonts/Inter-Regular.ttf")

app = QtWidgets.QApplication([])
ui = uic.loadUi("design.ui")

# header color #257b71
ui.setStyleSheet("background-color: #257b71;")

ui.setWindowIcon(QIcon("../color_picker/img.jpg"))
ui.setWindowTitle("color_picker")

style = "background-color: #132623; font-family: Inter; font-size: 12px; color:#afb1b3; font-weight: bold;"
ui.setStyleSheet(style)
labels = "background-color: #20403f; border-radius:3px; text-align:center;"
ui.label.setStyleSheet(labels)
ui.label.setAlignment(Qt.AlignCenter)
ui.label_2.setStyleSheet(labels)
ui.label_2.setAlignment(Qt.AlignCenter)
button = "background-color:#20403f;border-radius:5px;"
ui.change.setStyleSheet(button)
ui.keys.setStyleSheet("border: 2px solid #2fb86b;")

label_c = "color: #2fb86b;"
ui.color.setStyleSheet(label_c)
ui.color.setText("#none")
ui.color.setTextInteractionFlags(Qt.TextSelectableByMouse)


def key_upd():
    keyboard.remove_hotkey("alt")
    keyboard.add_hotkey(ui.keys.text(), color_change)


def color_change():
    x, y = pyautogui.position()
    color = pyautogui.pixel(x, y)
    hex_color = '#{:02x}{:02x}{:02x}'.format(*color)
    ui.color.setText(hex_color)


keyboard.add_hotkey("alt", color_change)
ui.change.clicked.connect(key_upd)
ui.show()
app.exec()
#20403f
#132623
#2a5440
#2fb86b
