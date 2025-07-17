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
import shutil

# locating other application files
sys.path.insert(0, "/app/share/pyside6apptemplate") # flatpak path
from program_file_locator import DATA_DIR
from widget_manager import load_widget, load_message_box

#PySide6, Qt Designer UI files
from PySide6.QtWidgets import (
    QApplication, QPushButton, QFileDialog
    ) #Import widgets here as needed


# Edit the .ui file using Qt Designer
ui_main = os.path.join(DATA_DIR, "main_window.ui")



# path to application folder. TODO: let the user change this
apps_folder = os.path.expanduser("~/applications")

os.makedirs(apps_folder, exist_ok=True)

class MainWindow():
    def __init__(self, window): 
        self.window = window

        # connect ui elements to code
        self.select_file = self.window.findChild(QPushButton,"select_file")
        self.select_folder = self.window.findChild(QPushButton,"select_folder")

        # Connect actions to slots or functions
        self.select_file.clicked.connect(self.method_select_file)
        self.select_folder.clicked.connect(self.method_select_folder)
        
    def method_select_file(self):
        """TODO:IMPLEMENT! If a recognized zip/tar/etc file is chosen, 
        unzip it and proceed with logic of folder method. 
        Much later, implement native/distrobox support for distro packages."""

        file_path, _ = QFileDialog.getOpenFileName(self.window, "NOT YET IMPLEMENTED!")

        return file_path

    def method_select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self.window, "Select Application Folder")

        # move folder to user's chosen applications directory
        

        return folder_path


# Logic that loads the main window
app = QApplication([])

window_main = load_widget(
    ui_main,
    "App Installer"
    )
logic = MainWindow(window_main)

window_main.show()
app.exec()