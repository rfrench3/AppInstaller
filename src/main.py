#!/usr/bin/env python3

"""
App Installer

Created in 2025 by rfrench3 (TealMango) - https://github.com/rfrench3

Licensed under the GNU GPLv3 only. See LICENSE file in the project root for full license information.
"""



"""
binaries logic:
- ask user to open binary folder or binary zip/tar
- unzip if necessary
- open that folder in the app
- tell the user to select:
  - the executable
  - the icon
  - more

from there, make/install:
- the icon
- the .desktop file
- more
"""



import sys
import os

# locating other application files
sys.path.insert(0, "/app/share/pyside6apptemplate") # flatpak path
from program_file_locator import DATA_DIR
from widget_manager import load_widget, load_message_box

#PySide6, Qt Designer UI files
from PySide6.QtWidgets import QApplication, QPushButton #Import widgets here as needed

# Edit the .ui file using Qt Designer
ui_main = os.path.join(DATA_DIR, "main_window.ui")

# logic for the main windowscopebuddy-guiscopebuddy-gui

class MainWindow():
    def __init__(self, window): 
        self.window = window

        # connect ui elements to code
        self.button = self.window.findChild(QPushButton,"pushButton")

        # Connect actions to slots or functions
        self.button.clicked.connect(self.button_clicked)
        
    def button_clicked(self):
        load_message_box(
            self.window,
            "message box title!",
            "message box text!"
        )

# Logic that loads the main window
app = QApplication([])

window_main = load_widget(
    ui_main,
    "App Installer",
    )
logic = MainWindow(window_main)

window_main.show()
app.exec()