# First practical example from the book: Pomodoro time manager
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTabWidget
from PyQt5.QtGui import QIcon


class MainWindow(QWidget):
	
	def __init__(self): # Create default constructor
		super().__init__()
		self.initializeUI()
	
	def initializeUI(self):
		"""Initialize the window and display its contents to the screen."""
		self.setGeometry(int((SCREEN_WIDTH-WINDOW_WIDTH)/2),int((SCREEN_HEIGHT-WINDOW_HEIGHT)/2),WINDOW_WIDTH,WINDOW_HEIGHT) # x,y,w,h
		self.setWindowTitle('Dickcheese')
		self.setWindowIcon(QIcon("Borticon.png"))
		self.setupTabsAndWidgets()

		self.show()

	def setupTabsAndWidgets(self):
		"""UI stuff. Tabs, windows, buttons etc."""

		self.tab_bar = QTabWidget(self)
		self.pomodoro_tab = QWidget()
		self.pomodoro_tab = QWidget()
		self.pomodoro_tab.setObjectName("Pomodoro")
		self.short_break_tab = QWidget()
		self.short_break_tab.setObjectName("ShortBreak")
		self.long_break_tab = QWidget()
		self.long_break_tab.setObjectName("LongBreak")
		self.tab_bar.addTab(self.pomodoro_tab, "Pomodoro")
		self.tab_bar.addTab(self.short_break_tab, "Short Break")
		self.tab_bar.addTab(self.long_break_tab, "Long Break")


	
		



if __name__ == '__main__':
	app = QApplication(sys.argv)
	WINDOW_WIDTH, WINDOW_HEIGHT = 1000,600
	SCREEN_X, SCREEN_Y, SCREEN_WIDTH, SCREEN_HEIGHT = app.desktop().screenGeometry().getRect()
	window = MainWindow()
	sys.exit(app.exec_())
