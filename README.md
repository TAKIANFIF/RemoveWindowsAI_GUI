# RemoveWindowsAI - GUI Edition

A modern Windows GUI application to remove AI features (Copilot, Recall, etc.) from Windows 10/11.

## features
- **User-Friendly Interface**: Select exactly what you want to remove.
- **Safety**: Uses the proven logic from the original [RemoveWindowsAI](https://github.com/TAKIANFIF/RemoveWindowsAI) script.
- **Standalone**: Runs as a single EXE file without needing Python installed.

## Usage
1. Download the latest release (EXE).
2. Run as Administrator.
3. Select the features to remove.
4. Click **REMOVE SELECTED**.
5. Restart your computer.

## Credits
- **GUI & Python Wrapper**: Developed by [Your Name/Antigravity]
- **PowerShell Logic**: Based on the excellent work by [@zoicware](https://github.com/zoicware) / [TAKIANFIF](https://github.com/TAKIANFIF).

## Build from Source
```bash
pip install -r requirements.txt
pyinstaller --noconsole --onefile --uac-admin --name "RemoveWindowsAI_GUI" --add-data "src/assets/scripts/RemoveWindowsAi.ps1;assets/scripts" src/main.py
```

## Disclaimer
This tool modifies system files and registry keys. Use at your own risk. Always create a restore point before using.
