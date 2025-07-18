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
  - app name (autofill with directory name)
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
    QApplication, QFileDialog, QListWidget
    ) #Import widgets here as needed
from PySide6.QtGui import (QAction)


# Edit the .ui file using Qt Designer
ui_main = os.path.join(DATA_DIR, "main_window.ui")
ui_installer = os.path.join(DATA_DIR, "installer.ui")



# path to application folder. TODO: let the user change this
apps_dir = os.path.expanduser("~/applications")

os.makedirs(apps_dir, exist_ok=True)

class MainWindow():
    def __init__(self, window): 
        self.window = window

        # connect ui elements to code
        self.install_file = self.window.findChild(QAction,"install_file")
        self.install_folder = self.window.findChild(QAction,"install_folder")


        # Connect actions to slots or functions
        self.install_file.triggered.connect(self.method_select_file)
        self.install_folder.triggered.connect(self.method_select_folder)
        

        
    def method_select_file(self):
        """TODO:IMPLEMENT! If a recognized zip/tar/etc file is chosen, 
        unzip it and proceed with logic of folder method. 
        Much later, implement native/distrobox support for distro packages."""

        original_path, _ = QFileDialog.getOpenFileName(self.window, "NOT YET IMPLEMENTED!")
        if not original_path:
            return  # no file selected

        filename = os.path.basename(original_path).lower()
        print(f"Selected file name: {filename}")

        if filename.endswith(".zip"):
            print("Zip archive selected. Extraction logic to be implemented.")
            # TODO: implement zip extraction
        elif (
            filename.endswith(".tar") or
            filename.endswith(".tar.gz") or
            filename.endswith(".tgz") or
            filename.endswith(".tar.bz2") or
            filename.endswith(".tbz2") or
            filename.endswith(".tar.xz") or
            filename.endswith(".txz")
        ):
            print("Tar archive selected. Extraction logic to be implemented.")
            # TODO: implement tar extraction
        else:
            print("Unsupported file type or not an archive.")
            return

        file_name = os.path.basename(original_path)
        dest_path = os.path.join(apps_dir, file_name)

        # STEP: MOVE FILE

        # if file isn't already in place
        if os.path.abspath(original_path) != os.path.abspath(dest_path):
            

            if os.path.exists(dest_path):
                raise NotImplementedError #TODO: dialog asking if user wants to keep new one or old one
            else:
                shutil.move(original_path, dest_path)

        # STEP: EXTRACT ARCHIVE FILE


        # STEP: MANUALLY "INSTALL" EXTRACTED FILES


        return 

    def method_select_folder(self):
        """Opens folder picker, moves chosen folder to apps_dir, 
        then opens window to continue "installation" of binary."""
        original_path = QFileDialog.getExistingDirectory(self.window, "Select Application Folder")

        # move folder to user's chosen applications directory
        if not original_path:
            return # no folder selected
            
        folder_name = os.path.basename(os.path.normpath(original_path))
        
        dest_path = os.path.join(apps_dir, folder_name)

        #TODO: ensure user didn't do anything like move an entire xdg-home folder
        
        # ensures the user did not try moving a folder already in the correct location
        if os.path.abspath(original_path) != os.path.abspath(dest_path):
            if os.path.exists(dest_path):
                raise NotImplementedError #TODO: dialog asking if user wants to keep new one or old one
            else:
                shutil.move(original_path, dest_path)
        else:
            print("the folder is already in place.")

        self.initiate_installer_interface(dest_path)

        return

    def initiate_installer_interface(self,folder):
        """TODO: opens the interface that instructs the user on manually "Installing" the binary."""

# Logic that loads the main window
app = QApplication([])

window_main = load_widget(
    ui_main,
    "App Installer"
    )
logic = MainWindow(window_main)

window_main.show()
app.exec()