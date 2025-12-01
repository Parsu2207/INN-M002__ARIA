import sys
from pyQt5.QtWidgets import QApplication
from .main_window import MainWindow

def run_desktop():
  app=QApplication(sys.argv)
  win=MainWindow()
  win.show()
  sys.exit(app.exec())
  
