#PyQt5
import sys
from tracemalloc import stop
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Backend import interpolate
from Gui_Julia import Julia

class Plot_interpolate(QWidget):
    def __init__(self): 
        #QApplication
        super().__init__()
        self.Creater()
        

    def Getvalue(self):
        strat = int(self.inputbox.text())
        stop = int(self.inputbox1.text())
        step = int(self.inputbox2.text())
        print(strat,stop,step)

        self.gettime = interpolate(strat,stop,step)
        self.gettime1 = Julia(strat,stop,step)

        self.bro2.clear()                   #bro2 is Linear interpolat
        self.bro2.append(self.gettime[0])
        self.bro2_J.clear()                   #bro2 is Linear interpolat
        self.bro2_J.append(self.gettime1[0])

        self.bro3.clear()                   #bro3 is Cubic interpolat
        self.bro3.append(self.gettime[1]) 
        self.bro3_J.clear()                   #bro2 is Linear interpolat
        self.bro3_J.append(self.gettime1[1])

        self.bro4.clear()                   #bro3 is Quadratic interpolat
        self.bro4.append(self.gettime[2])
        self.bro4_J.clear()                   #bro2 is Linear interpolat
        self.bro4_J.append(self.gettime1[2])
        
        
        self.bro1.setStyleSheet('border-image:url(my_plot.png);')
        self.bro1_J.setStyleSheet('border-image:url(plot_julia.png);')

    def Creater(self):
        self.setWindowTitle("Interpolation")
        self.resize(1500,500)
        self.move(300,30)

        #creating button QPushButton
        self.button = QPushButton("Interpolate",self)
        self.button.resize(200,30)
        self.button.move(700,250)
        self.button.clicked.connect(self.Getvalue)
        self.button.setFont(QtGui.QFont("Helvetica",14))

        # Input Start 
        self.label_0 = QLabel('Start point: ',self)
        self.label_0.move(680, 70)
        self.label_0.setFont(QtGui.QFont("Helvetica",14))
        # Input Stop 
        self.label_0 = QLabel('Stop point: ',self)
        self.label_0.move(680, 120)
        self.label_0.setFont(QtGui.QFont("Helvetica",14))
        # Input Step 
        self.label_0 = QLabel('Step point: ',self)
        self.label_0.move(680, 170)
        self.label_0.setFont(QtGui.QFont("Helvetica",14))

        #Inputbox Start
        self.inputbox = QLineEdit(self)
        self.inputbox.resize(100,30)
        self.inputbox.move(800,70)
        self.inputbox.setFont(QtGui.QFont("Helvetica",16))
        #Inputbox Stop
        self.inputbox1 = QLineEdit(self)
        self.inputbox1.resize(100,30)
        self.inputbox1.move(800,120)
        self.inputbox1.setFont(QtGui.QFont("Helvetica",16))
        #Inputbox Step
        self.inputbox2 = QLineEdit(self)
        self.inputbox2.resize(100,30)
        self.inputbox2.move(800,170)
        self.inputbox2.setFont(QtGui.QFont("Helvetica",16))

        #Python time 
        self.label_0 = QLabel('Python: ',self)
        self.label_0.move(80, 350)
        self.label_0.setFont(QtGui.QFont("Helvetica",14))
        #Julia time 
        self.label_0 = QLabel('Julia: ',self)
        self.label_0.move(950, 350)
        self.label_0.setFont(QtGui.QFont("Helvetica",14))

        #Python linear time 
        self.label_1 = QLabel('Linear time: ',self)
        self.label_1.move(180, 350)
        self.label_1.setFont(QtGui.QFont("Helvetica",14))
        #Julia linear time 
        self.label_1 = QLabel('Linear time: ',self)
        self.label_1.move(1050, 350)
        self.label_1.setFont(QtGui.QFont("Helvetica",14))

        #Python Cubic time 
        self.label_1 = QLabel('Cubic time : ',self)
        self.label_1.move(180, 400)
        self.label_1.setFont(QtGui.QFont("Helvetica",14))
        #Julia Cubic time 
        self.label_1 = QLabel('Cubic time: ',self)
        self.label_1.move(1050, 400)
        self.label_1.setFont(QtGui.QFont("Helvetica",14))

        #Julia Quadratic time 
        self.label_1 = QLabel('Quadratic time : ',self)
        self.label_1.move(180, 450)
        self.label_1.setFont(QtGui.QFont("Helvetica",14))
        #Julia Quadratic time 
        self.label_1 = QLabel('Quadratic time: ',self)
        self.label_1.move(1050, 450)
        self.label_1.setFont(QtGui.QFont("Helvetica",14))
        
        #TextBrower Python Graph
        self.bro1 = QTextBrowser(self)
        self.bro1.resize(500,320)
        self.bro1.move(70,10)
        self.bro1.setFont(QtGui.QFont("Helvetica",12))
        
        #TextBrower JuliaGraph
        self.bro1_J = QTextBrowser(self)
        self.bro1_J.resize(500,320)
        self.bro1_J.move(950,10)
        self.bro1_J.setFont(QtGui.QFont("Helvetica",12))

        #TextBrower time
        self.bro2 = QTextBrowser(self)
        self.bro2.resize(200,30)
        self.bro2.move(350,350)
        self.bro2.setFont(QtGui.QFont("Helvetica",12))
        #TextBrower time
        self.bro2_J = QTextBrowser(self)
        self.bro2_J.resize(250,30)
        self.bro2_J.move(1220,350)
        self.bro2_J.setFont(QtGui.QFont("Helvetica",12))

        #TextBrower time
        self.bro3 = QTextBrowser(self)
        self.bro3.resize(200,30)
        self.bro3.move(350,400)
        self.bro3.setFont(QtGui.QFont("Helvetica",12))
        #TextBrower time
        self.bro3_J = QTextBrowser(self)
        self.bro3_J.resize(250,30)
        self.bro3_J.move(1220,400)
        self.bro3_J.setFont(QtGui.QFont("Helvetica",12))

        #TextBrower time
        self.bro4 = QTextBrowser(self)
        self.bro4.resize(200,30)
        self.bro4.move(350,450)
        self.bro4.setFont(QtGui.QFont("Helvetica",12))
        #TextBrower time
        self.bro4_J = QTextBrowser(self)
        self.bro4_J.resize(250,30)
        self.bro4_J.move(1220,450)
        self.bro4_J.setFont(QtGui.QFont("Helvetica",12))
        

    def show_exit(self):
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    A = Plot_interpolate()
    A.show_exit()
    sys.exit(app.exec_())