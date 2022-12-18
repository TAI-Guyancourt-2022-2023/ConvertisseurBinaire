"""nbr = int(input("Entrez votre nombre en decimal compris entre 0 et 255:  "))
print("Résultat en binaire: ", bin(nbr).replace("0b",""))"""
 
from PyQt5 import QtCore , QtGui , QtWidgets
from designedUI import Ui_Binary
#ôfrom PyQt5 import Qtimer, QTime, Qt 


"""
def action1():
    def action(self):
        nbr=int(self.octet1.text())
        self.rsultat1=input.setText(str(bin(nbr).replace("0b","")))
"""



#Slots 
def action1():
    try:
        nbr=int(ui.octet1.toPlainText())
        ui.rsultat1.setText(str(bin(nbr).replace("0b","")))
    except Exception:
        ui.octet1.setText("0"), ui.rsultat1.setText("0")
        
def action2():
    try:
        nbr=int(ui.octet2.toPlainText())
        ui.rsultat2.setText(str(bin(nbr).replace("0b","")))
    except Exception:
        ui.octet2.setText("0"), ui.rsultat2.setText("0")
def action3():
    try:
        nbr=int(ui.octet3.toPlainText())
        ui.rsultat3.setText(str(bin(nbr).replace("0b","")))
    except Exception:
        ui.octet3.setText("0"), ui.rsultat3.setText("0")
def action4():
    try:
        nbr=int(ui.octet4.toPlainText())
        ui.rsultat4.setText(str(bin(nbr).replace("0b","")))
    except Exception:
        ui.octet4.setText("0"), ui.rsultat4.setText("0")

def refresh():   
    ui.octet1.setText(""), ui.rsultat1.setText("")
    ui.octet2.setText(""), ui.rsultat2.setText("")
    ui.octet3.setText(""), ui.rsultat3.setText("")
    ui.octet4.setText(""), ui.rsultat4.setText("")




import sys
app = QtWidgets.QApplication(sys.argv)
Binary = QtWidgets.QMainWindow()
ui = Ui_Binary()
ui.setupUi(Binary)
Binary.show()

#connection
#ui.octet1.print(ui.rsultat1(bin(nbr).replace("0b","")))
ui.Convert.clicked.connect(action1)
ui.Convert.clicked.connect(action2)
ui.Convert.clicked.connect(action3)
ui.Convert.clicked.connect(action4)
ui.refresh.clicked.connect(refresh)
sys.exit(app.exec_())


