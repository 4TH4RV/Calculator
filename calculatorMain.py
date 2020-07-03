from calculator import *
import sys


class Initialise(Ui_zero):
	def __init__(self, window):
		self.setupUi(window)
		
		# KeyPad Setup	
		self.one.clicked.connect(lambda: self.addSymbol(1))
		self.two.clicked.connect(lambda: self.addSymbol(2))
		self.three.clicked.connect(lambda: self.addSymbol(3))
		self.four.clicked.connect(lambda: self.addSymbol(4))
		self.five.clicked.connect(lambda: self.addSymbol(5))
		self.six.clicked.connect(lambda: self.addSymbol(6))
		self.seven.clicked.connect(lambda: self.addSymbol(7))
		self.eight.clicked.connect(lambda: self.addSymbol(8))
		self.nine.clicked.connect(lambda: self.addSymbol(9))
		self.zero.clicked.connect(lambda: self.addSymbol(0))
		self.multiply.clicked.connect(lambda: self.addSymbol("*"))
		self.divide.clicked.connect(lambda: self.addSymbol("/"))
		self.sum.clicked.connect(lambda: self.addSymbol("+"))
		self.subtract.clicked.connect(lambda: self.addSymbol("-"))
		
		# Main KeyPad Button Setup
		self.clear.clicked.connect(lambda: self.clearLabel()) 
		self.enter.clicked.connect(lambda: self.evaluate())  
		
	def evaluate(self):
		getText = self.inputLabel.text()
		
		if not getText.find("*") == -1:
			
			evalString = getText.split("*")
			self.inputLabel.setText(str(int(evalString[0]) * int(evalString[1])))
			
		elif not getText.find("/") == -1:
			
			evalString = getText.split("/")
			self.inputLabel.setText(str(int(evalString[0]) / int(evalString[1])))
			
		elif not getText.find("+") == -1:
			
			evalString = getText.split("+")
			self.inputLabel.setText(str(int(evalString[0]) + int(evalString[1])))
			
		elif not getText.find("-") == -1:
			
			evalString = getText.split("-")
			self.inputLabel.setText(str(int(evalString[0]) - int(evalString[1])))
		
	def addSymbol(self, symbol):
		self.inputLabel.setText(self.inputLabel.text() + str(symbol)) 

	def clearLabel(self):
		self.inputLabel.setText("")

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = Initialise(MainWindow)

MainWindow.show()
app.exec_()
