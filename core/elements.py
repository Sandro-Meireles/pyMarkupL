from core.exceptions import EmptyCode

class Element:

    def __init__(self, code: str = '', *args, **kwargs):
        self._code = code
        self.assign_code()

    def assign_code(self):
        render = self.render()
        if not render:
            raise EmptyCode(f'{self.__class__.__name__} has no code!')

        if not self._code:
            self._code = render

        self.search_tag(render)

    def search_tag(self, render: str):
        mairq_index = None

        for index, letter in enumerate(render):

            if letter == '<':
                mairq_index = index

            if mairq_index != None and letter == '>':
                str_element = render[mairq_index: index + 1]

                self.replace_element(str_element)

                mairq_index = None

    def element_found(self, element: str) -> bool:
        if not hasattr(self, element):
            return False

        attr = getattr(self, element)

        if not isinstance(attr, Element):
            return False

        return True

    def clean_element(self, element: str) -> str:
        if not element.startswith('<') and not element.endswith('>'):
            raise Exception('Elemento errado')

        return element[1:-1].strip()

    def replace_element(self, element: str):
        clean_element = self.clean_element(element)

        if clean_element.startswith('/'):
            return

        if self.element_found(clean_element):
            attr = getattr(self, clean_element)
            self._code = self._code.replace(element, attr.content())


    def content(self) -> str:
        return self._code

    def render(self) -> str:
        return self._code