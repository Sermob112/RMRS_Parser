
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog

from PyQt5 import QtWidgets, uic,QtCore,QtGui

class mywindow(QtWidgets.QMainWindow):


    def __init__(self):
        super(mywindow, self).__init__()
        uic.loadUi('untitled.ui',self)
        self.folderEx = None


    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        folder = QFileDialog.getExistingDirectory(self,'Выбрерите папку для сохранения файла ', options=options)
        return folder
    def update_label(self, i,t ):
        self.label.setText(f" Парсинг дпнных: {i} из {t}")



