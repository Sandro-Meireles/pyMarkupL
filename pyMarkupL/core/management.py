import os
import pyMarkupL
import shutil
import distutils.dir_util

class Init:

    startstructure = 'startstructure'

    def __init__(self):
        self.pymarkup_path =self.pml_root_path()
        self.cwd = os.getcwd()
        self.startstructure_path = self.get_startstructure_path()
        self.content_files = self.get_content_files()
    
    def start_generating(self):
        self.interator()

    def interator(self):
        for file in self.content_files:
            self.generate(file)

    def generate(self, file_name):
        file_path = os.path.join(self.startstructure_path, file_name)

        if os.path.isdir(file_path):
            self.generate_dir(file_path, file_name)
            return
        
        try:
            shutil.copy(file_path, self.cwd)
        except Exception as error:
            raise ProjectInitError('Your project could not be initialized! ' + str(error))

    def generate_dir(self, file_path, file_name):
        try:
            src_dir = os.path.join(self.cwd, file_name)
            os.mkdir(src_dir)
            distutils.dir_util.copy_tree(file_path, src_dir)

        except Exception as error:
            raise ProjectInitError('Your project could not be initialized! ' + str(error))

    def get_content_files(self):
        files = []
        for file in os.listdir(self.startstructure_path):
            if not self.cwd_file_exist(os.path.join(self.cwd, file)):
                files.append(file)
            else:
                print(f'{file} already exists in your project')

        return files

    def cwd_file_exist(self, path) -> bool:
        return os.path.exists(path)

    def pml_root_path(self) -> str:
        return os.path.dirname(os.path.abspath(pyMarkupL.__file__))
    
    def get_startstructure_path(self):
        return os.path.join(self.pymarkup_path, self.startstructure)