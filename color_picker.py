import sys
import pyautogui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt


class ColorPicker(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("Color Picker")
        # 设置窗口大小
        self.setFixedSize(220, 150)

        # 创建用于显示颜色信息的标签
        self.color_label = QLabel(self)
        layout = QVBoxLayout()
        layout.addWidget(self.color_label)
        self.setLayout(layout)

        # 绑定鼠标按下事件
        self.setMouseTracking(True)
        self.mousePressEvent = self.on_mouse_press

    def on_mouse_press(self, event):
        if event.button() == Qt.LeftButton:
            # 获取鼠标当前位置的坐标
            x, y = pyautogui.position()
            # 获取该坐标处像素的颜色
            color = pyautogui.screenshot().getpixel((x, y))
            # 将RGB颜色值转换为十六进制颜色代码
            hex_color = "#{:02x}{:02x}{:02x}".format(*color)
            # 更新标签显示的颜色代码信息
            self.color_label.setText(f"Color Code: {hex_color}")
            self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorPicker()
    window.show()
    sys.exit(app.exec_())