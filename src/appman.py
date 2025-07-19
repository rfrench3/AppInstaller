#!/usr/bin/env python3

"""
At some point, this may be moved into its own dedicated program. 
It handles all of the operations that don't require a GUI.
"""

import argparse, os


# Parse command line arguments
parser = argparse.ArgumentParser(description="AppInstaller command line tool")
subparsers = parser.add_subparsers(dest="command")

# Subcommands
list_parser = subparsers.add_parser("list", help="List installed apps", add_help=False)

install_parser = subparsers.add_parser("install", help="Install an app", add_help=False)
install_parser.add_argument("--executable", required=True, help="Required, path to the executable file.")
install_parser.add_argument("--name", required=False, help="Not required, name of the file. Defaults to the executable.")
install_parser.add_argument("--icon", required=False, help="Not required, path to the icon file.")
install_parser.add_argument("--description", required=False, help="Not required, description of the app.")
install_parser.add_argument("--use-terminal", action="store_true", help="If set, the app will run in a terminal.")

uninstall_parser = subparsers.add_parser("uninstall", help="Uninstall an app", add_help=False)
uninstall_parser.add_argument("--id", required=True, help="Required, ID of the app as shown by appman list.")


args = parser.parse_args()



def install_app(executable:str,name:str,icon:str="",description:str="",terminal:bool=False):
    """
    Outline for installing an app. Only the executable is strictly required.
    Args:
        executable (str): Path to the executable file.
        name (str): Name of the file.
        icon (str): Path to the icon file.
        description (str): Description of the app.
        terminal (bool): Makes the app open and run in a terminal.
    """

    if not executable:
        raise ValueError("The 'executable' argument is required. It is the path to the executable file.")
    
    if not name:
        name = os.path.basename(executable)


    # TODO: Implement installation logic
    
    


def create_desktop_file(executable:str,name:str,icon:str="",description:str="",terminal:bool=False):
    """create a .desktop file that will appear in the app menu"""
    
    filename = name + ".desktop"
    lines = [
        "[Desktop Entry]\n",
        f"Name={name}\n",
        f"Comment={description}\n",
        f"Exec={executable}\n",
        f"Icon={icon}\n",
        f"Terminal={terminal}\n",
    ]


    pass


def list_apps():
    """List all installed apps"""
    # TODO: Implement list logic
    print("Listing installed apps...")
    pass


if args.command == "install":
    install_app(
        executable=args.executable, 
        name=args.name or "",
        icon=args.icon or "",
        description=args.description or "",
        terminal=args.use_terminal
    )
elif args.command == "list":
    list_apps()