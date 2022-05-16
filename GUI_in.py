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
#path
import os
cwd = os.getcwd().replace("\\","/")


class Plot_interpolate(QWidget):
    def __init__(self): 
        #QApplication
        super().__init__()
        self.Creater()

    def interpolate(self):

        self.x = np.linspace(0, 10, num=11, endpoint=True)
        self.y = np.cos(-self.x**2/9.0)

        start_li = datetime.datetime.now() # set start time 
        f = interp1d(self.x, self.y)
        end_li = datetime.datetime.now()   # set end time
        print("linear time", end_li - start_li)
        self.bro2.clear()
        self.bro2.append(str(end_li - start_li))

        start_cu = datetime.datetime.now() # set start time
        f2 = interp1d(self.x, self.y, kind='cubic')
        end_cu = datetime.datetime.now()   # set end time
        print("cubic time",end_cu - start_cu)
        self.bro3.clear()
        self.bro3.append(str(end_cu - start_cu)) 

        start_qu = datetime.datetime.now() # set start time 
        f3 = interp1d(self.x, self.y, kind='quadratic')
        end_qu = datetime.datetime.now()   # set end time 
        print("quadratic time",end_qu - start_qu)
        self.bro4.clear()
        self.bro4.append(str(end_qu - start_qu))
        
        xnew = np.linspace(0, 10, num=4001, endpoint=True)

        import matplotlib.pyplot as plt
        plt.plot(self.x, self.y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--', xnew, f3(xnew))
        plt.legend(['data', 'linear', 'cubic', 'quadratic'], loc='best')
        plt.savefig('my_plot.png')
        self.bro1.setStyleSheet(f'border-image:url({cwd}/my_plot.png);')

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
