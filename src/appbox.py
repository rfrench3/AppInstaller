#!/usr/bin/env python3

import argparse

def run_gui_qt():
    print("[Placeholder] Running Qt GUI...")

def print_help():
    print("help information")

def install(file_path):
    print("[Placeholder] Running install...")

def uninstall(program_name):
    print("[Placeholder] Running uninstall...")

def list_apps():
    print("[Placeholder] List of apps...")


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
        print_help()

    elif args.command == "gui":
        if args.type == "qt":
            run_gui_qt()
        else:
            print("The only available GUIs are:\n qt")

    elif args.command == "install":
        install(args.file_path)

    elif args.command == "uninstall":
        uninstall(args.program_name)

    elif args.command == "list":
        list_apps()

    else:
        print("Unrecognized command.")





if __name__ == "__main__":
    main()
