import os
import sys
import settings

# TODO: implement command interface used to manage the framework

# This interface will be improved in the future!

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'compile':
            print(settings.MAIN_ELEMENT().content())

if __name__ == '__main__':
    main()