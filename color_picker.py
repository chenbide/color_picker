import sys
import pyautogui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt
import clipboard  # 需要安装这个库，用于实现复制功能，使用命令pip install clipboard安装


class ColorPicker(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("Color Picker")
        # 设置窗口大小
        self.setFixedSize(800, 600)  # 适当调整下窗口大小方便展示图片和操作

        # 加载名为pic的图片文件
        self.pixmap = QPixmap("pic")
        if self.pixmap.isNull():
            print("无法加载图片文件")
            sys.exit(1)

        # 创建用于显示颜色信息的标签
        self.color_label = QLabel(self)
        self.color_label.setStyleSheet("QLabel { background-color: white; }")  # 设置背景色方便查看文字

        # 创建复制按钮
        self.copy_button = QPushButton("复制", self)
        self.copy_button.clicked.connect(self.copy_color_code)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("点击图片获取颜色代码", self))
        layout.addWidget(self.color_label)
        layout.addWidget(self.copy_button)
        self.setLayout(layout)

        # 绑定鼠标按下事件
        self.setMouseTracking(True)
        self.mousePressEvent = self.on_mouse_press

    def on_mouse_press(self, event):
        if event.button() == Qt.LeftButton:
            # 获取鼠标在图片中的相对坐标（需要转换，因为坐标是相对于窗口的，要映射到图片上）
            x = event.x()
            y = event.y()
            if 0 <= x < self.pixmap.width() and 0 <= y < self.pixmap.height():
                # 获取该坐标处像素的颜色
                color = self.pixmap.toImage().pixelColor(x, y).getRgb()[:3]
                # 将RGB颜色值转换为十六进制颜色代码
                hex_color = "#{:02x}{:02x}{:02x}".format(*color)
                # 更新标签显示的颜色代码信息
                self.color_label.setText(f"Color Code: {hex_color}")
                self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pixmap)

    def copy_color_code(self):
        color_text = self.color_label.text().split(": ")[-1]
        clipboard.copy(color_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorPicker()
    window.show()
    sys.exit(app.exec_())