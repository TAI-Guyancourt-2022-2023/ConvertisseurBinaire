# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designedUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Binary(object):
    def setupUi(self, Binary):
        Binary.setObjectName("Binary")
        Binary.resize(529, 281)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Background/icons8-100-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Binary.setWindowIcon(icon)
        Binary.setStyleSheet("background-color: rgb(121, 121, 121);")
        Binary.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(Binary)
        self.centralwidget.setObjectName("centralwidget")
        self.Convert = QtWidgets.QPushButton(self.centralwidget)
        self.Convert.setGeometry(QtCore.QRect(10, 202, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Convert.setFont(font)
        self.Convert.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.Convert.setObjectName("Convert")
        self.octet1 = QtWidgets.QTextEdit(self.centralwidget)
        self.octet1.setGeometry(QtCore.QRect(30, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.octet1.setFont(font)
        self.octet1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.octet1.setObjectName("octet1")
        self.octet2 = QtWidgets.QTextEdit(self.centralwidget)
        self.octet2.setGeometry(QtCore.QRect(150, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.octet2.setFont(font)
        self.octet2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.octet2.setObjectName("octet2")
        self.octet3 = QtWidgets.QTextEdit(self.centralwidget)
        self.octet3.setGeometry(QtCore.QRect(270, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.octet3.setFont(font)
        self.octet3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.octet3.setObjectName("octet3")
        self.octet4 = QtWidgets.QTextEdit(self.centralwidget)
        self.octet4.setGeometry(QtCore.QRect(390, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.octet4.setFont(font)
        self.octet4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.octet4.setObjectName("octet4")
        self.rsultat1 = QtWidgets.QLineEdit(self.centralwidget)
        self.rsultat1.setGeometry(QtCore.QRect(30, 80, 101, 31))
        self.rsultat1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rsultat1.setObjectName("rsultat1")
        self.rsultat2 = QtWidgets.QLineEdit(self.centralwidget)
        self.rsultat2.setGeometry(QtCore.QRect(150, 80, 101, 31))
        self.rsultat2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rsultat2.setObjectName("rsultat2")
        self.rsultat3 = QtWidgets.QLineEdit(self.centralwidget)
        self.rsultat3.setGeometry(QtCore.QRect(270, 80, 101, 31))
        self.rsultat3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rsultat3.setObjectName("rsultat3")
        self.rsultat4 = QtWidgets.QLineEdit(self.centralwidget)
        self.rsultat4.setGeometry(QtCore.QRect(390, 80, 101, 31))
        self.rsultat4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rsultat4.setObjectName("rsultat4")
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(10, 162, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.refresh.setFont(font)
        self.refresh.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.refresh.setObjectName("refresh")
        Binary.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Binary)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 21))
        self.menubar.setObjectName("menubar")
        self.menuConvertisseur = QtWidgets.QMenu(self.menubar)
        self.menuConvertisseur.setObjectName("menuConvertisseur")
        Binary.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Binary)
        self.statusbar.setObjectName("statusbar")
        Binary.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuConvertisseur.menuAction())

        self.retranslateUi(Binary)
        QtCore.QMetaObject.connectSlotsByName(Binary)

    def retranslateUi(self, Binary):
        _translate = QtCore.QCoreApplication.translate
        Binary.setWindowTitle(_translate("Binary", "Convertisseur Tommy©"))
        self.Convert.setText(_translate("Binary", "Convert"))
        self.octet1.setHtml(_translate("Binary", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:30pt;\"><br /></p></body></html>"))
        self.octet2.setHtml(_translate("Binary", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:30pt;\"><br /></p></body></html>"))
        self.octet3.setHtml(_translate("Binary", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:30pt;\"><br /></p></body></html>"))
        self.octet4.setHtml(_translate("Binary", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:30pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:30pt;\"><br /></p></body></html>"))
        self.refresh.setText(_translate("Binary", "Refresh"))
        self.menuConvertisseur.setTitle(_translate("Binary", "Convertisseur"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Binary = QtWidgets.QMainWindow()
    ui = Ui_Binary()
    ui.setupUi(Binary)
    Binary.show()
    sys.exit(app.exec_())