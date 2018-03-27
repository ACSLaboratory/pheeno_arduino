"""
Pheeno Arduino/Teensy File Setup

Creates copies of `lib/` into each arduino file folder. Afterwards, a user may
run the necessary platformio commands to upload the code to the microcontroller
of each Pheeno robot.

You must use either --all or --file option. Not using an option will
result in nothing getting done. Example cases:

$ python file_setup.py --all

or

$ python file_setup.py --file ros
"""
import os
import subprocess
import argparse

def get_args():
    """ Get arguments for file setup. """
    help_description = """
    Microcontroller setup script for the Pheeno robot.
    You must use either --all or --file option. Not using an option will
    result in nothing getting done.
    """
    parser = argparse.ArgumentParser(
        description=help_description)

    # Required arguments
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--all",
                       default=False,
                       action="store_true",
                       help="Copy `lib` into every directory.")
    group.add_argument("-f", "--file",
                       action="store",
                       default=None,
                       type=str,
                       help="Copy `lib` into a specified directory. (STR)")

    return parser.parse_args()

def main():
    """ Copy necessary arduino files to their appropriate locations. """
    args = get_args()

    # Select option based on argparse results
    if args.all is not False:
        # Copy `lib` to all directories.
        directories = os.listdir(".")
        exclude_dirs = [".git", "lib"]
        for directory in directories:
            if directory not in exclude_dirs and os.path.isdir(directory):
                subprocess.Popen(["cp", "-r", "lib/", directory + "/"])

    elif args.file is not None:
        # Check to make sure filepath is valid, then copy to file directory.
        if os.path.isdir(args.file):
            subprocess.Popen(["cp", "-r", "lib/", args.file])

        else:
            raise ValueError("File path given is not a real directory or path!")

    else:
        raise Exception("Need to give an --all or --file option!")

if __name__ == "__main__":
    main()
