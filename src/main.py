#!/usr/bin/env python3

"""
App Installer

Created in 2025 by rfrench3 (TealMango) - https://github.com/rfrench3

Licensed under the GNU GPLv3 only. See LICENSE file in the project root for full license information.
"""

import sys
import os
import shutil

# locating other application files
sys.path.insert(0, "/app/share/appinstaller") # flatpak path
from program_file_locator import DATA_DIR
from widget_manager import load_widget, load_message_box



#PySide6, Qt Designer UI files
from PySide6.QtWidgets import (
    QApplication, QFileDialog,
    QPushButton
    ) #Import widgets here as needed


# Edit the .ui file using Qt Designer
ui_main = os.path.join(DATA_DIR, "main_window.ui")

class MainWindow():
    def __init__(self, window): 
        self.window = window

        # connect ui elements to code
        self.install_file:QPushButton = self.window.findChild(QPushButton,"install_new_app")

        # Connect actions to slots or functions
        self.install_file.clicked.connect(self.method_select_file)


        # make sure various file managers are available for use
        self.flatpak = self.has_flatpak()
        self.appimage = self.has_appimage()
        self.distrobox = self.has_distrobox()

            
    def method_select_file(self) -> str:
        """Opens a QFileDialog window in the Downloads directory that lets the user pick from any supported file type.
        Returns the path to the file, or an empty string if no file was chosen."""

        downloads_dir:str = str(os.environ.get("XDG_DOWNLOAD_DIR"))
        if not downloads_dir:
            # Fallback: use ~/Downloads if XDG_DOWNLOAD_DIR is not set
            downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

        original_path, _ = QFileDialog.getOpenFileName(
            self.window,
            "Select Application File",
            downloads_dir,
            (
            "All Supported Files (*.deb *.rpm *.flatpak *.appimage *.tar *.tar.gz *.tgz *.tar.bz2 *.tbz2 *.tar.xz *.txz);;"
            "Debian Packages (*.deb);;"
            "RPM Packages (*.rpm);;"
            "Flatpak Packages (*.flatpak);;"
            "AppImages (*.appimage);;"
            "Binaries (*.tar *.tar.gz *.tgz *.tar.bz2 *.tbz2 *.tar.xz *.txz)"
            )
        )

        if not original_path:
            return ""  # no file selected
        
        return original_path
    


    def has_flatpak(self) -> bool:
        return shutil.which("flatpak") is not None
        
    
    def has_appimage(self) -> bool:
        """All systems should be able to run AppImages, 
        but if that ever changes this makes it easy to implement a proper check."""
        return True

    def has_distrobox(self) -> bool:
        return shutil.which("distrobox") is not None
    
    def has_tar(self) -> bool:
        return shutil.which("tar") is not None

    
# Logic that loads the main window
app = QApplication([])

window_main = load_widget(
    ui_main,
    "App Installer"
    )
logic = MainWindow(window_main)

window_main.show()
app.exec()