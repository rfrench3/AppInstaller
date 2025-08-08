#!/usr/bin/env python3
"""
AppBox

Created in 2025 by rfrench3 (TealMango) - https://github.com/rfrench3
Source code - https://github.com/rfrench3/appbox

Licensed under the GNU GPLv3 only. See LICENSE file in the project root for full license information.
"""





def main():
    from PySide6.QtWidgets import QMessageBox, QApplication, QFileDialog, QPushButton
    from PySide6.QtGui import QIcon
    from PySide6.QtCore import QFile
    from PySide6.QtUiTools import QUiLoader

    import sys
    import os
    import core

    # This will only load the app icon from the theme, which happens automatically when installed as a flatpak
    app_icon = QIcon.fromTheme("io.github.rfrench3.pyside6apptemplate")


    def load_widget(ui_file: str, window_title:str='Scopebuddy GUI', icon:QIcon=app_icon):
        """Load a widget from a UI file and return it.
        Handles widgets as windows and widgets loaded into windows."""
        loader = QUiLoader()
        ui = QFile(ui_file)
        ui.open(QFile.OpenModeFlag.ReadOnly)
        widget = loader.load(ui)
        ui.close()
        if widget.isWindow():
            # set window attributes
            widget.setWindowTitle(window_title)
            widget.setWindowIcon(icon) #type:ignore
        return widget

    def load_message_box(parent_window,title:str,  text:str,  icon:QMessageBox.Icon=QMessageBox.Icon.Information,  standard_buttons:QMessageBox.StandardButton=QMessageBox.StandardButton.Ok) -> QMessageBox.StandardButton:
        """Loads a QMessageBox, returns the result of exec()."""
        msg = QMessageBox(parent_window)
        msg.setIcon(icon)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setStandardButtons(standard_buttons)
        return msg.exec() #type:ignore

    # locating other application files
    sys.path.insert(0, "/app/share/appbox") # flatpak path
    DATA_DIR = os.path.dirname(os.path.abspath(__file__)) 

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

            if core.has_distrobox():
                file_types += "*.deb *.rpm "
                has_installer.append("distrobox")
            
            if core.has_flatpak():
                file_types += "*.flatpak "
                has_installer.append("flatpak")

            if core.has_appimage():
                file_types += "*.appimage "
                has_installer.append("appimage")

            if core.has_tar():
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
        

        
    # Logic that loads the main window
    app = QApplication([])

    window_main = load_widget(
        ui_main,
        "AppBox"
        )
    logic = MainWindow(window_main)

    window_main.show()
    app.exec()
