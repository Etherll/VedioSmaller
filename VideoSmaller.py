# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(579, 256)
        MainWindow.setStyleSheet("background-color: rgb(7, 7, 22);\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 90, 101, 30))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(179, 179, 179);\n"
"border:none;")
        self.pushButton.setText("Open File")
        self.pushButton.setCheckable(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.OpenFile)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(450, 90, 10, 31))
        self.widget.setStyleSheet("background-color: rgb(7, 13, 86);")
        self.widget.setObjectName("widget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(50, 130, 91, 17))
        self.checkBox.setStyleSheet("background-color: rgb(7, 7, 22);\n"
"color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 271, 51))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 8pt \"Yu Gothic UI\";")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 90, 401, 30))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 10, 111, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./src/discord.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.OpenDiscord)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 130, 101, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(179, 179, 179);\n"
                                        "font: 10pt \"MS Shell Dlg 2\";\n"
                                        "border:none;\n"
                                        "")

        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.Run_FFmeg)
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def OpenFile(self):
        path = os.path.dirname(os.path.realpath(__file__))
        file_name,_=QtWidgets.QFileDialog.getOpenFileName(MainWindow,'Open Video File',path,'*')
        self.textEdit.setText(file_name)

    def Run_FFmeg(self):
        self.worker = FFMEG_Worker()
        self.worker.filename = self.textEdit.toPlainText()
        self.worker.noAudio = self.checkBox.isChecked()
        self.worker.start()
        self.worker.finished.connect(self.worker_finished)
    def worker_finished(self):
        old_size = os.path.getsize(self.textEdit.toPlainText()) *1000
        filepath = self.textEdit.toPlainText()
        filename = filepath.split(r"/")[-1]
        new_size =  os.path.getsize(f'{filepath[:-len(filename)]}{filename.split(".")[0]}_smaller.mp4') *1000
        message = QtWidgets.QMessageBox()
        message.setStyleSheet('color: rgb(255, 255, 255);\n'
                              "background-color: rgb(7, 7, 22);\n")
        message.setWindowTitle('Done!')
        message.setText(f"{str(old_size)[:1]+'.'+str(old_size)[1:3]} --> {str(new_size)[:1]+'.'+str(new_size)[1:3]}")
        message.exec_()
    def OpenDiscord(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://discord.gg/3pP7pDAccn'))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Smaller"))
        self.checkBox.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">remove audio</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Remove Audio"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Video smaller</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "Start"))
class FFMEG_Worker(QtCore.QThread):
    filename = None
    noAudio=False

    def run(self):
        if self.noAudio:
            os.system(
                f'ffmpeg -i "{self.filename}" -an -c:v libx264 -b:v 1m -y "{self.filename.split(r"/")[-1].split(".")[0]}_smaller.mp4"')
            return
        os.system(f'ffmpeg -i "{self.filename}" -c:v libx264 -b:v 1m -y "{self.filename.split(r"/")[-1].split(".")[0]}_smaller.mp4"')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
