from pyMarkupL.core.elements import Element
from src.components.static.style import MyStyle
from src.components.toolbar import Toolbar
from src.components.box import Box

class Main(Element):

    def render(self, **kwargs):
        return '''
            <MyStyle>
            <Toolbar(title="pyMarkupL")>
            <div class="container">
                <Box(title="Title 1")>
                <Box(title="Title 2")>
                <Box(title="Title 3")>
            </div>
        '''
