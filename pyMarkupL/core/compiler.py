
import os

class SettingsManager:

    @classmethod
    def dont_exist_create(cls, path: str):
        if not os.path.exists(path):
            print(f'Generating: {path}')
            os.makedirs(path)


class Compiler:
    def __init__(self, element, settings, debug=False):
        self.settings = settings
        self.element = element
        self.debug = debug

    def generate(self):
        if self.debug:
            self.generate_file(self.settings.OUTPUT_DEBUG, 'debug.html')

            return
        
        self.generate_file(self.settings.OUTPUT_RELEASE, 'release.html')

    def generate_file(self, path: str, file_name: str):

        SettingsManager.dont_exist_create(path)

        with open(path + file_name, 'w') as generated_file:
            print(f'Generating: {file_name} in {path}')
            generated_file.write(self.element().content())
