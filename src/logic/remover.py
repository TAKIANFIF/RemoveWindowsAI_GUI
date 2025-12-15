import sys
import os
import subprocess
from PyQt6.QtCore import QObject, pyqtSignal, QThread

class RemovalThread(QThread):
    progress_update = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, selected_options):
        super().__init__()
        self.selected_options = selected_options

    def run(self):
        script_path = self.get_script_path()
        if not os.path.exists(script_path):
            self.progress_update.emit(f"Error: Script not found at {script_path}")
            self.finished.emit()
            return

        # Construct PowerShell command
        # Mapping GUI keys to Script params
        key_map = {
            "Disable-Registry-Keys": "DisableRegKeys",
            "Prevent-AI-Package-Reinstall": "PreventAIPackageReinstall",
            "Disable-Copilot-Policies": "DisableCopilotPolicies",
            "Remove-AI-Appx-Packages": "RemoveAppxPackages",
            "Remove-Recall-Optional-Feature": "RemoveRecallFeature",
            "Remove-AI-CBS-Packages": "RemoveCBSPackages",
            "Remove-AI-Files": "RemoveAIFiles",
            "Hide-AI-Components": "HideAIComponents",
            "Disable-Notepad-Rewrite": "DisableRewrite",
            "Remove-Recall-Tasks": "RemoveRecallTasks"
        }

        params = []
        for key in self.selected_options:
            if key in key_map:
                params.append(key_map[key])
        
        if not params:
            self.progress_update.emit("No valid options selected.")
            self.finished.emit()
            return

        param_string = ",".join(params)
        
        # Command: powershell.exe -NoProfile -ExecutionPolicy Bypass -File script.ps1 -Options ...
        cmd = [
            "powershell.exe",
            "-NoProfile",
            "-ExecutionPolicy", "Bypass",
            "-File", script_path,
            "-Options", param_string,
            "-nonInteractive"
        ]

        self.progress_update.emit(f"Executing: {' '.join(cmd)}")
        
        try:
            # Hide console window
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                startupinfo=startupinfo,
                bufsize=1,
                universal_newlines=True
            )

            for line in process.stdout:
                self.progress_update.emit(line.strip())
            
            process.wait()
            self.progress_update.emit("Done.")
            
        except Exception as e:
            self.progress_update.emit(f"Execution failed: {str(e)}")
        
        self.finished.emit()

    def get_script_path(self):
        # Handle PyInstaller path
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, "assets", "scripts", "RemoveWindowsAi.ps1")
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "scripts", "RemoveWindowsAi.ps1")
