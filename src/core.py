#!/usr/bin/env python3
"""
AppBox

Created in 2025 by rfrench3 (TealMango) - https://github.com/rfrench3
Source code - https://github.com/rfrench3/appbox

Licensed under the GNU GPLv3 only. See LICENSE file in the project root for full license information.
"""

import shutil

def has_distrobox() -> bool:
    return shutil.which("distrobox") is not None

def has_flatpak() -> bool:
    return shutil.which("flatpak") is not None

def has_appimage() -> bool:
    return True # implement proper check later

def has_tar() -> bool:
    return shutil.which("tar") is not None

def print_help():
    print("help information")

def install(file_path):
    print("[Placeholder] Running install...")

def uninstall(program_name):
    print("[Placeholder] Running uninstall...")

def list_apps():
    print("[Placeholder] List of apps...")

