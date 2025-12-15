from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QCheckBox, QPushButton, QLabel, QGroupBox, QScrollArea, QTextEdit, QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from logic.remover import RemovalThread

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remove Windows AI - GUI Edition")
        self.setMinimumSize(800, 600)
        
        # Main Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Header
        header_label = QLabel("Windows AI Remover")
        header_label.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header_label)
        
        desc_label = QLabel("Select the AI features you want to remove completely from your system.")
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        desc_label.setStyleSheet("color: #aaaaaa; font-size: 14px;")
        main_layout.addWidget(desc_label)
        
        # Options Area
        options_group = QGroupBox("Removal Options")
        options_layout = QVBoxLayout()
        
        self.checkboxes = {}
        options = [
            ("Disable-Registry-Keys", "Disable Registry Keys (Copilot, Recall, etc.)"),
            ("Prevent-AI-Package-Reinstall", "Prevent AI Package Reinstall"),
            ("Disable-Copilot-Policies", "Disable Copilot Policies"),
            ("Remove-AI-Appx-Packages", "Remove AI Appx Packages"),
            ("Remove-Recall-Optional-Feature", "Remove Recall Optional Feature"),
            ("Remove-AI-CBS-Packages", "Remove AI CBS Packages"),
            ("Remove-AI-Files", "Remove AI Files (Edge, System32, etc.)"),
            ("Hide-AI-Components", "Hide AI Components"),
            ("Disable-Notepad-Rewrite", "Disable Notepad AI Rewrite"),
            ("Remove-Recall-Tasks", "Remove Recall Scheduled Tasks")
        ]
        
        for key, text in options:
            cb = QCheckBox(text)
            cb.setChecked(True)  # Default all checked
            self.checkboxes[key] = cb
            options_layout.addWidget(cb)
            
        options_group.setLayout(options_layout)
        
        # Scroll Area for options (in case list grows)
        scroll = QScrollArea()
        scroll.setWidget(options_group)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.Shape.NoFrame)
        main_layout.addWidget(scroll)
        
        # Action Buttons
        btn_layout = QHBoxLayout()
        
        self.btn_select_all = QPushButton("Select All")
        self.btn_select_all.clicked.connect(self.select_all)
        btn_layout.addWidget(self.btn_select_all)
        
        self.btn_deselect_all = QPushButton("Deselect All")
        self.btn_deselect_all.clicked.connect(self.deselect_all)
        btn_layout.addWidget(self.btn_deselect_all)
        
        btn_layout.addStretch()
        
        self.btn_remove = QPushButton("REMOVE SELECTED")
        self.btn_remove.setObjectName("RemoveButton")
        self.btn_remove.setMinimumHeight(45)
        self.btn_remove.clicked.connect(self.start_removal)
        btn_layout.addWidget(self.btn_remove)
        
        main_layout.addLayout(btn_layout)
        
        # Console Output
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        self.console.setPlaceholderText("Log output will appear here...")
        self.console.setMaximumHeight(150)
        main_layout.addWidget(self.console)
        
        # Thread
        self.worker = None

    def select_all(self):
        for cb in self.checkboxes.values():
            cb.setChecked(True)

    def deselect_all(self):
        for cb in self.checkboxes.values():
            cb.setChecked(False)

    def start_removal(self):
        if self.worker and self.worker.isRunning():
            return

        selected = [key for key, cb in self.checkboxes.items() if cb.isChecked()]
        if not selected:
            self.log("No options selected.", color="yellow")
            return
            
        confirm = QMessageBox.question(self, "Confirm Removal", 
                                     "Are you sure you want to remove the selected AI features?\nThis action modifies system files and registry keys.",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.No:
            return

        self.console.clear()
        self.log(f"Starting removal for {len(selected)} items...", color="cyan")
        self.btn_remove.setEnabled(False)
        self.btn_remove.setText("Running...")
        
        self.worker = RemovalThread(selected)
        self.worker.progress_update.connect(self.handle_log)
        self.worker.finished.connect(self.removal_finished)
        self.worker.start()

    def handle_log(self, message):
        color = "white"
        if "[ ! ]" in message or "Error" in message:
            color = "#ff5555"
        elif "[ + ]" in message:
            color = "#00ff00"
        self.log(message, color=color)

    def removal_finished(self):
        self.btn_remove.setEnabled(True)
        self.btn_remove.setText("REMOVE SELECTED")
        self.log("Operation Complete. Please restart your computer.", color="#00aaff")
        QMessageBox.information(self, "Finished", "Operation Complete.\nPlease restart your computer to apply all changes.")

    def log(self, message, color="white"):
        self.console.append(f'<span style="color:{color}">{message}</span>')
        # Scroll to bottom
        scrollbar = self.console.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
