#PyQt5
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Numpy
import datetime
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate
from scipy.interpolate import interp1d
from scipy.interpolate import lagrange

from Backend import interpolate

class Plot_interpolate(QWidget):
    def __init__(self): 
        #QApplication
        super().__init__()
        self.Creater()
        

    def interpolate(self):

        self.gettime = interpolate()
        self.bro2.clear()                   #bro2 is Linear interpolat
        self.bro2.append(self.gettime[0])

        self.bro3.clear()                   #bro3 is Cubic interpolat
        self.bro3.append(self.gettime[1]) 

        self.bro4.clear()                   #bro3 is Quadratic interpolat
        self.bro4.append(self.gettime[2])
        
        
        self.bro1.setStyleSheet('border-image:url(C:/Users/Computer/Desktop/python/Intepolation/my_plot.png);')

    def Creater(self):
        self.setWindowTitle("Interpolation")
        self.resize(900,500)
        self.move(300,30)

        #creating button QPushButton
        self.button = QPushButton("Interpolate",self)
        self.button.resize(200,30)
        self.button.move(50,100)
        self.button.clicked.connect(self.interpolate)
        self.button.setFont(QtGui.QFont("Helvetica",14))

        
        #linear time 
        self.label_0 = QLabel('Linear time: ',self)
        self.label_0.move(50, 350)
        self.label_0.setFont(QtGui.QFont("Helvetica",14))

        #Cubic time 
        self.label_0 = QLabel('Cubic time : ',self)
        self.label_0.move(50, 400)
        self.label_0.setFont(QtGui.QFont("Helvetica",14))

        #Quadratic time 
        self.label_0 = QLabel('Quadratic time : ',self)
        self.label_0.move(50, 450)
        self.label_0.setFont(QtGui.QFont("Helvetica",14))
        
        #TextBrower Graph
        self.bro1 = QTextBrowser(self)
        self.bro1.resize(500,320)
        self.bro1.move(300,10)
        self.bro1.setFont(QtGui.QFont("Helvetica",12))

        #TextBrower time
        self.bro2 = QTextBrowser(self)
        self.bro2.resize(200,30)
        self.bro2.move(200,350)
        self.bro2.setFont(QtGui.QFont("Helvetica",12))

        #TextBrower time
        self.bro3 = QTextBrowser(self)
        self.bro3.resize(200,30)
        self.bro3.move(200,400)
        self.bro3.setFont(QtGui.QFont("Helvetica",12))

        #TextBrower time
        self.bro4 = QTextBrowser(self)
        self.bro4.resize(200,30)
        self.bro4.move(250,450)
        self.bro4.setFont(QtGui.QFont("Helvetica",12))

    def show_exit(self):
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    A = Plot_interpolate()
    A.show_exit()
    sys.exit(app.exec_())