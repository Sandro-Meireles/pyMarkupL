import os
import sys
import settings

from pyMarkupL.core.command import Command

# TODO: implement command interface used to manage the framework

# This interface will be improved in the future!

def main():
    Command(sys.argv, settings)

if __name__ == '__main__':
    main()