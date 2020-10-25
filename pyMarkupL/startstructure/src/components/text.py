from pyMarkupL.core.elements import Element

class Text(Element):

    def render(self, title=None):
        return f'''<p class="title">{title}</p>'''