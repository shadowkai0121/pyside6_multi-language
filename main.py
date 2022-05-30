from PySide6 import QtWidgets
from PySide6.QtCore import QTranslator
from ui_main import Ui_MainWindow
from enum import Enum


class Language(Enum):
    '''
    使用 enum 型別方便管理語系
    '''
    us = 0
    tw = 1


class MainController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def select_language(self, lang: str):
        translator = QTranslator()
        QtWidgets.QApplication.instance().installTranslator(translator)

        # 讀取 qm 檔案
        translator.load(f'ui_main_{Language(lang).name}')

        self.ui.retranslateUi(self)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = MainController()
    window.show()
    sys.exit(app.exec())
