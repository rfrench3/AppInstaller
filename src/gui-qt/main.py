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
sys.path.insert(0, "/app/share/appbox") # flatpak path
from program_file_locator import DATA_DIR
from widget_manager import load_widget, load_message_box
import subprocess



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
        self.install_file.clicked.connect(self.method_install_file)

            
    def method_select_file(self) -> str:
        """Opens a QFileDialog window in the Downloads directory that lets the user pick from any supported file type.
        Returns the path to the file, or an empty string if no file was chosen."""

        downloads_dir:str = str(os.environ.get("XDG_DOWNLOAD_DIR"))
        if not downloads_dir:
            # Fallback: use ~/Downloads if XDG_DOWNLOAD_DIR is not set
            downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

        # Only let the user select a file type if they have the right program
        file_types:str = ''
        has_installer:list[str] = []

        if self.has_distrobox():
            file_types += "*.deb *.rpm "
            has_installer.append("distrobox")
        
        if self.has_flatpak():
            file_types += "*.flatpak "
            has_installer.append("flatpak")

        if self.has_appimage():
            file_types += "*.appimage "
            has_installer.append("appimage")

        if self.has_tar():
            file_types += "*.tar *.tar.gz *.tgz *.tar.bz2 *.tbz2 *.tar.xz *.txz "
            has_installer.append("tar")

        file_types = f"All Supported Files ({file_types.strip()})"

        for program in has_installer:
            match program:
                case "distrobox":
                    file_types += ";;Debian Packages (*.deb);;RPM Packages (*.rpm)"
                case "flatpak":
                    file_types += ";;Flatpak Packages (*.flatpak)"
                case "appimage":
                    file_types += ";;AppImages (*.appimage)"
                case "tar":
                    file_types += ";;Binaries (*.tar *.tar.gz *.tgz *.tar.bz2 *.tbz2 *.tar.xz *.txz)"
                case _:
                    raise TypeError


        original_path, _ = QFileDialog.getOpenFileName(
            self.window,
            "Select Application File",
            downloads_dir,
            file_types
        )

        if not original_path:
            return ""  # no file selected
        
        return original_path
    
    def method_install_file(self):
        """Uses available app management programs to install the chosen application."""

        file_path = self.method_select_file()
        if not file_path:
            return
        
        file_extension = (
            "deb" if file_path.endswith("deb") else 
            "rpm" if file_path.endswith("rpm") else 
            "flatpak" if file_path.endswith("flatpak") else 
            "appimage" if file_path.endswith("appimage") else 
            "tar"
            )
        
        def install_distrobox(file_path, extension) -> bool:
            """Create the necessary distrobox if one doesn't exist, install the file in it, 
            and then export the file to host."""
            
            if extension == "deb":
                try:
                    result = subprocess.run(
                        [os.path.join(os.path.dirname(__file__), "install_distrobox.sh"), extension, file_path],
                        check=True
                    )
                except subprocess.CalledProcessError as e:
                    load_message_box(
                        self.window,
                        "Error",
                        f"Failed to create install .deb file:\n{e}"
                        )
                    return False

                

            elif extension == "rpm":
                try:
                    result = subprocess.run(
                        [os.path.join(os.path.dirname(__file__), "install_distrobox.sh"), extension, file_path],
                        check=True
                    )
                except subprocess.CalledProcessError as e:
                    load_message_box(
                        self.window,
                        "Error",
                        f"Failed to create install .rpm file:\n{e}"
                        )
                    return False

            else:
                raise NotImplementedError





            return True

        def install_flatpak(file_path) -> bool:
            """Install the flatpak file to the user, return True if successful."""
            try:
                subprocess.run(
                    ["bash", "-c", f"flatpak install --user --assumeyes '{file_path}'"],
                    check=True
                )
                load_message_box(
                    self.window,
                    "Success",
                    "Flatpak package installed successfully."
                )
                return True
            except subprocess.CalledProcessError as e:
                load_message_box(
                    self.window,
                    "Error",
                    f"Failed to install Flatpak package:\n{e}"
                )
                return False
            




        match file_extension:
            case "deb":
                install_distrobox(file_path,"deb")
            case "rpm":
                install_distrobox(file_path,"rpm")
            case "flatpak":
                install_flatpak(file_path)
            case "appimage":
                load_message_box(
                    self.window,
                    "Not Yet Implemented",
                    "Installing tar binaries is not yet implemented!"
                )
            case "tar":
                load_message_box(
                    self.window,
                    "Not Yet Implemented",
                    "Installing tar binaries is not yet implemented!"
                )
            case _:
                raise TypeError













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