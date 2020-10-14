from core.elements import Element

class Toolbar(Element):

    def render(self, **kwargs):
        title = kwargs.get("title")

        return f'''
<div class="toolbar">
    <p class="title">{title}</p>
</div>
        '''
