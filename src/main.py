from core.elements import Element
from .components.static.style import MyStyle
from .components.toolbar import Toolbar
from .components.box import Box

class Main(Element):
    
    myStyle = MyStyle
    toolbar = Toolbar
    box = Box

    def render(self, **kwargs):
        return '''
<myStyle>
<toolbar(title="pyMarkupL")>
<div class="container">
    <box(title="Title 1")>
    <box(title="Title 2")>
    <box(title="Title 3")>
</div>'''
