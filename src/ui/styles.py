from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QColor, QPalette

def apply_styles(app: QApplication):
    # Set Fusion style as a base
    app.setStyle("Fusion")
    
    # Define a modern dark palette
    palette = QPalette()
    
    # Colors
    dark_bg = QColor("#1e1e1e")
    darker_bg = QColor("#121212")
    text_color = QColor("#ffffff")
    accent_color = QColor("#0078d4")  # Windows Blue
    accent_hover = QColor("#2b88d8")
    danger_color = QColor("#d13438")
    
    palette.setColor(QPalette.ColorRole.Window, dark_bg)
    palette.setColor(QPalette.ColorRole.WindowText, text_color)
    palette.setColor(QPalette.ColorRole.Base, darker_bg)
    palette.setColor(QPalette.ColorRole.AlternateBase, dark_bg)
    palette.setColor(QPalette.ColorRole.ToolTipBase, text_color)
    palette.setColor(QPalette.ColorRole.ToolTipText, text_color)
    palette.setColor(QPalette.ColorRole.Text, text_color)
    palette.setColor(QPalette.ColorRole.Button, dark_bg)
    palette.setColor(QPalette.ColorRole.ButtonText, text_color)
    palette.setColor(QPalette.ColorRole.BrightText, QColor("#ff0000"))
    palette.setColor(QPalette.ColorRole.Link, accent_color)
    palette.setColor(QPalette.ColorRole.Highlight, accent_color)
    palette.setColor(QPalette.ColorRole.HighlightedText, text_color)
    
    app.setPalette(palette)
    
    # Stylesheet for specific widgets
    app.setStyleSheet("""
        QMainWindow {
            background-color: #1e1e1e;
        }
        QGroupBox {
            border: 1px solid #3a3a3a;
            border-radius: 6px;
            margin-top: 12px;
            font-weight: bold;
            color: #e0e0e0;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 0 5px;
            left: 10px;
        }
        QCheckBox {
            spacing: 8px;
            color: #d0d0d0;
            font-size: 14px;
            padding: 4px;
        }
        QCheckBox::indicator {
            width: 18px;
            height: 18px;
            border-radius: 3px;
            border: 1px solid #5a5a5a;
            background: #2d2d2d;
        }
        QCheckBox::indicator:checked {
            background-color: #0078d4;
            border-color: #0078d4;
            image: url(assets/check.svg); /* Fallback to color if no svg */
        }
        QCheckBox::indicator:hover {
            border-color: #0078d4;
        }
        QPushButton {
            background-color: #2d2d2d;
            border: 1px solid #3a3a3a;
            border-radius: 4px;
            padding: 8px 16px;
            color: #ffffff;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #3a3a3a;
            border-color: #5a5a5a;
        }
        QPushButton:pressed {
            background-color: #0078d4;
            border-color: #0078d4;
        }
        QPushButton#RemoveButton {
            background-color: #d13438;
            border-color: #d13438;
            font-size: 16px;
        }
        QPushButton#RemoveButton:hover {
            background-color: #e04347;
        }
        QTextEdit {
            background-color: #121212;
            border: 1px solid #3a3a3a;
            border-radius: 4px;
            color: #00ff00; /* Console green */
            font-family: Consolas, "Courier New", monospace;
        }
    """)
