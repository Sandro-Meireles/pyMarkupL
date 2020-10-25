from pyMarkupL.core.elements import Element
from src.components.text import Text

class Toolbar(Element):

    def render(self, title=None):

        return f'''
            <div class="toolbar">
                <Text(title={title})>
            </div>
        '''
