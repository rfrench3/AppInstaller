#!/usr/bin/env python3
"""
AppBox

Created in 2025 by rfrench3 (TealMango) - https://github.com/rfrench3
Source code - https://github.com/rfrench3/appbox

Licensed under the GNU GPLv3 only. See LICENSE file in the project root for full license information.
"""
import sys
import argparse
import core
import gui_qt

sys.path.insert(0, "/app/share/appbox")

def run_gui_qt():
    gui_qt.main()

def main():
    parser = argparse.ArgumentParser(description="AppBox CLI and GUI")
    subparsers = parser.add_subparsers(dest="command")

    # GUI command
    gui_parser = subparsers.add_parser("gui", help="Launch GUI interfaces")
    gui_parser.add_argument("type", choices=["qt"], help="Type of GUI to launch")

    # Install command
    install_parser = subparsers.add_parser("install", help="Install an app from a file")
    install_parser.add_argument("file_path", help="Path to the app file to install")

    # Uninstall command
    uninstall_parser = subparsers.add_parser("uninstall", help="Uninstall an app by name")
    uninstall_parser.add_argument("program_name", help="Name of the program to uninstall")

    # List command
    subparsers.add_parser("list", help="List installed apps")

    args = parser.parse_args()

    if args.command is None:
        core.print_help()

    elif args.command == "gui":
        if args.type == "qt":
            run_gui_qt()
        else:
            print("The only available GUIs are:\n qt")

    elif args.command == "install":
        core.install(args.file_path)

    elif args.command == "uninstall":
        core.uninstall(args.program_name)

    elif args.command == "list":
        core.list_apps()

    else:
        print("Unrecognized command.")

if __name__ == "__main__":
    main()
