from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from login import Ui_Form


class MyWindow(QWidget, Ui_Form):  # 多继承
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])  # Qt应用程序
    window = MyWindow()  # 打开窗口
    window.show()  # 显示窗口
    app.exec()  # 停止应用程序
