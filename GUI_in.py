#PyQt5
import sys
from tracemalloc import stop
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Backend import interpolate
from Gui_Julia import Julia
from Interpolate_DIY import main
from DIY_Julia import DIY

class Plot_interpolate(QWidget):
    def __init__(self): 
        #QApplication
        super().__init__()
        self.Creater()
        

    def Getvalue(self):
        start = int(self.inputbox.text())
        stop = int(self.inputbox1.text())
        step = int(self.inputbox2.text())
        print(start,stop,step)

        self.gettimeP = interpolate(start,stop,step) # Send parameter to python library
        self.gettimeJ = Julia(start,stop,step)  #send parameter to Julia library
        
        self.gettimePM = main(start,stop,step)
        self.gettimeJM = DIY(start,stop,step)

        self.bro2.clear()                   #bro2 is Linear interpolat
        self.bro2.append(self.gettimeP[0])
        self.bro2_J.clear()                   #bro2 is Linear interpolat
        self.bro2_J.append(self.gettimeJ[0])

        self.bro3.clear()                   #bro3 is Cubic interpolat
        self.bro3.append(self.gettimeP[1]) 
        self.bro3_J.clear()                   #bro3 is Cubic interpolat
        self.bro3_J.append(self.gettimeJ[1])

        self.bro4.clear()                   #bro4 is Quadratic interpolat
        self.bro4.append(self.gettimeP[2])
        self.bro4_J.clear()                   #bro4 is Quadratic interpolat
        self.bro4_J.append(self.gettimeJ[2])

        self.bro1_P.setStyleSheet('border-image:url(my_plot.png);')
        self.bro1_J.setStyleSheet('border-image:url(plot_julia.png);')

        #############################################################
        
        self.bro6.clear()                   #bro5 is Linear interpolat
        self.bro6.append(self.gettimePM[0])
        self.bro6_J.clear()                   #bro5 is Linear interpolat
        self.bro6_J.append(self.gettimeJM[0])

        self.bro7.clear()                   #bro5 is Cubic interpolat
        self.bro7.append(self.gettimePM[1])
        self.bro7_J.clear()                   #bro5 is Cubic interpolat
        self.bro7_J.append(self.gettimeJM[1])
        
        self.bro8.clear()                   #bro5 is Quadratic interpolat
        self.bro8.append(self.gettimePM[2])
        self.bro8_J.clear()                   #bro5 is Quadratic interpolat
        self.bro8_J.append(self.gettimeJM[2])

        self.bro5_P.setStyleSheet('border-image:url(DIY_plot.png);')
        self.bro5_J.setStyleSheet('border-image:url(DIY_Julia.png);')



    def Creater(self):
        self.setWindowTitle("Interpolation")
        self.resize(1500,1000)
        self.move(300,30)

        #creating button QPushButton
        self.button = QPushButton("Interpolate",self)
        self.button.resize(200,30)
        self.button.move(650,500)
        self.button.clicked.connect(self.Getvalue)
        self.button.setFont(QtGui.QFont("Helvetica",14))

        # Input Start 
        self.label_0 = QLabel('Start point: ',self)
        self.label_0.move(620, 320)
        self.label_0.setFont(QtGui.QFont("Helvetica",14))
        # Input Stop 
        self.label_0 = QLabel('Stop point: ',self)
        self.label_0.move(620, 370)
        self.label_0.setFont(QtGui.QFont("Helvetica",14))
        # Input Step 
        self.label_0 = QLabel('Step point: ',self)
        self.label_0.move(620, 420)
        self.label_0.setFont(QtGui.QFont("Helvetica",14))

        #Inputbox Start
        self.inputbox = QLineEdit(self)
        self.inputbox.resize(100,30)
        self.inputbox.move(760,320)
        self.inputbox.setFont(QtGui.QFont("Helvetica",16))
        #Inputbox Stop
        self.inputbox1 = QLineEdit(self)
        self.inputbox1.resize(100,30)
        self.inputbox1.move(760,370)
        self.inputbox1.setFont(QtGui.QFont("Helvetica",16))
        #Inputbox Step
        self.inputbox2 = QLineEdit(self)
        self.inputbox2.resize(100,30)
        self.inputbox2.move(760,420)
        self.inputbox2.setFont(QtGui.QFont("Helvetica",16))

        #Python time 
        self.label_0 = QLabel('Python Library: ',self)
        self.label_0.move(15, 350)
        self.label_0.setFont(QtGui.QFont("Helvetica",14))
        #Julia time 
        self.label_0 = QLabel('Julia Library: ',self)
        self.label_0.move(910, 350)
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
        self.bro1_P = QTextBrowser(self)
        self.bro1_P.resize(500,320)
        self.bro1_P.move(70,10)
        self.bro1_P.setFont(QtGui.QFont("Helvetica",12))
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

        ##########################################################################################################

        #TextBrower Python Graph
        self.bro5_P = QTextBrowser(self)
        self.bro5_P.resize(500,320)
        self.bro5_P.move(70,500)
        self.bro5_P.setFont(QtGui.QFont("Helvetica",12))
        #TextBrower JuliaGraph
        self.bro5_J = QTextBrowser(self)
        self.bro5_J.resize(500,320)
        self.bro5_J.move(950,500)
        self.bro5_J.setFont(QtGui.QFont("Helvetica",12))

        #Python time 
        self.label_0 = QLabel('Python Manual: ',self)
        self.label_0.move(10, 850)
        self.label_0.setFont(QtGui.QFont("Helvetica",14))
        #Julia time 
        self.label_0 = QLabel('Julia Manual: ',self)
        self.label_0.move(910, 850)
        self.label_0.setFont(QtGui.QFont("Helvetica",14))

        #Python linear time 
        self.label_1 = QLabel('Linear time: ',self)
        self.label_1.move(180, 850)
        self.label_1.setFont(QtGui.QFont("Helvetica",14))
        #Julia linear time 
        self.label_1 = QLabel('Linear time: ',self)
        self.label_1.move(1050, 850)
        self.label_1.setFont(QtGui.QFont("Helvetica",14))

        #Python Cubic time 
        self.label_1 = QLabel('Cubic time : ',self)
        self.label_1.move(180, 900)
        self.label_1.setFont(QtGui.QFont("Helvetica",14))
        #Julia Cubic time 
        self.label_1 = QLabel('Cubic time: ',self)
        self.label_1.move(1050, 900)
        self.label_1.setFont(QtGui.QFont("Helvetica",14))

        #Julia Quadratic time 
        self.label_1 = QLabel('Quadratic time : ',self)
        self.label_1.move(180, 950)
        self.label_1.setFont(QtGui.QFont("Helvetica",14))
        #Julia Quadratic time 
        self.label_1 = QLabel('Quadratic time: ',self)
        self.label_1.move(1050, 950)
        self.label_1.setFont(QtGui.QFont("Helvetica",14))

         #TextBrower time
        self.bro6 = QTextBrowser(self)
        self.bro6.resize(200,30)
        self.bro6.move(350,850)
        self.bro6.setFont(QtGui.QFont("Helvetica",12))
        #TextBrower time
        self.bro6_J = QTextBrowser(self)
        self.bro6_J.resize(250,30)
        self.bro6_J.move(1220,850)
        self.bro6_J.setFont(QtGui.QFont("Helvetica",12))

        #TextBrower time
        self.bro7 = QTextBrowser(self)
        self.bro7.resize(200,30)
        self.bro7.move(350,900)
        self.bro7.setFont(QtGui.QFont("Helvetica",12))
        #TextBrower time
        self.bro7_J = QTextBrowser(self)
        self.bro7_J.resize(250,30)
        self.bro7_J.move(1220,900)
        self.bro7_J.setFont(QtGui.QFont("Helvetica",12))

        #TextBrower time
        self.bro8 = QTextBrowser(self)
        self.bro8.resize(200,30)
        self.bro8.move(350,950)
        self.bro8.setFont(QtGui.QFont("Helvetica",12))
        #TextBrower time
        self.bro8_J = QTextBrowser(self)
        self.bro8_J.resize(250,30)
        self.bro8_J.move(1220,950)
        self.bro8_J.setFont(QtGui.QFont("Helvetica",12))
        

    def show_exit(self):
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    A = Plot_interpolate()
    A.show_exit()
    sys.exit(app.exec_())