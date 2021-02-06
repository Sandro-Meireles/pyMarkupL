import os

from pyMarkupL.core.compiler import Compiler
from pyMarkupL.core.exceptions import ProjectInitError

from pyMarkupL.core.decorators.command_decoratos import ManageRequire
from pyMarkupL.core.management import Init

def get_core_path() -> str:
    core_path = os.path.dirname(os.path.abspath(__file__))
    return core_path

class Command:

    def __init__(self, argv: list, settings=None):
        self.argv = argv
        self.settings = settings
        self.analyze_command()

    def is_equals(self, arg1, *args):

        for arg in args:
            if arg1.lower() == arg.lower():
                return True

        return False

    def cwd_file_exist(self, path) -> bool:
        return os.path.exists(path)

    def is_manage_command(self) -> bool:
        if self.argv[0] == 'pml':
            return False
        if not self.settings:
            return False

        return True

    def analyze_command(self):

        if len(self.argv) == 1:
            self.help_()

            return

        if self.is_equals(self.argv[1], 'start', 'init', 'startproject', 'iniciar'):
            self.init()

        elif self.is_equals(self.argv[1], 'ok', 'ok?'):
            self.ok()

        elif self.is_equals(self.argv[1], 'help', '-h', 'ajuda', '--help'):
            self.help_()

        elif self.is_equals(self.argv[1], 'compile', 'compilar', 'cpl'):
            self.compile_()

        elif self.is_equals(self.argv[1], 'run', 'rodar', 'runserver'):
            self.run()

        else:
            self.help_()

    def init(self):
        init = Init()
        init.start_generating()

    def ok(self):
        print('\npyMarkupL has been successfully installed!')

    def help_(self):
        root = os.path.dirname(get_core_path())
        with open(os.path.join(root, 'help.txt'), 'r') as help_file:
            print(help_file.read())
        
    @ManageRequire
    def compile_(self):
        compiler = Compiler(self.settings.MAIN_ELEMENT, self.settings)
        compiler.generate()

    @ManageRequire
    def run(self):
        if '-e' in self.argv:
            # TODO: Run the server for a specific element
            return

        compiler = Compiler(self.settings.MAIN_ELEMENT, self.settings, debug=True)
        compiler.generate()

        # TODO: Run the server
