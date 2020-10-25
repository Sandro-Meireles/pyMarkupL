from pyMarkupL.core.elements import Element

class Box(Element):
    def render(self, **kwargs):
        title = kwargs.get('title')

        return f'''
    <div class="box">
        <div class="box-title">
            <p>{title}</p>
        </div>
        <div class="box-content">
            <p>
                Lorem ipsum dolor sit amet, conse ctetur adipi scing elit. Donec eu ele mentum urna. Morbi mauris lorem, lacinia et
                dignissim vitae, solli citudin nec sem. Aliquam mollis lorem in ligula semper suscipit. Duis nibh ipsum, lobortis id
                vulputate sed, tempor eu neque. Suspendisse id risus interdum, condimentum purus a, aliquet erat. tempor eu neque. Suspendisse id
            </p>
        </div>
    </div>'''