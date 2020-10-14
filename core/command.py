from .compiler import Compiler
import settings

class Command:

    def __init__(self, argv: list):
        self.argv = argv
        self.analyze_command()

    def is_equals(self, arg1, *args):

        for arg in args:
            if arg1.lower() == arg.lower():
                return True

        return False

    def analyze_command(self):

        if len(self.argv) == 1:
            self.help_()

            return

        if self.is_equals(self.argv[1], 'help', '-h', 'ajuda', '--help'):
            self.help_()

        elif self.is_equals(self.argv[1], 'compile', 'compilar', 'cpl'):
            self.compile()

        elif self.is_equals(self.argv[1], 'run', 'rodar', 'runserver'):
            self.run()

        else:
            self.help_()

    def help_(self):
        # TODO: implement the help interface
        ...

    def compile(self):
        compiler = Compiler(settings.MAIN_ELEMENT)
        compiler.generate()

    def run(self):
        if '-e' in self.argv:
            # TODO: Run the server for a specific element
            return

        compiler = Compiler(settings.MAIN_ELEMENT, debug=True)
        compiler.generate()

        # TODO: Run the server
