import sys
import os
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.styles import apply_styles

def main():
    app = QApplication(sys.argv)
    
    # Apply global styles
    apply_styles(app)
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
