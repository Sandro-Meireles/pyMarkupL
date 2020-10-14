from core.exceptions import EmptyCode, InconsistentElement

class Element:

    def __init__(self, code: str = '', *args, **kwargs):
        self._code = code
        self.assign_code(self.render(*args, **kwargs))

    def assign_code(self, render: str):
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

        if not issubclass(attr, Element):
            raise InconsistentElement(f'{attr} it is not an Element')

        return True

    def is_arg_valid(self, arg) -> bool:
        # TODO: Add more validations

        splited_arg = arg.split('=')
        if len(splited_arg) == 1:
            return False

        if not splited_arg[1] :
            return False
        
        return True

    def treat_kwargs(self, args: str):
        args = args.replace('(', '').replace(')', '')
        kwargs = {}
        for arg in args.split(','):
            arg = arg.strip()

            if not self.is_arg_valid(arg):
                raise SyntaxError(f'Invalid arg <{arg}> by {self.__class__}')

            key = arg.split('=')[0]
            value = arg.split('=')[1].replace('"', '')

            kwargs[key] = value
        
        return kwargs

    def clean_element(self, element: str) -> (str, dict):
        if not element.startswith('<') and not element.endswith('>'):
            raise Exception('Elemento errado')

        element = element[1:-1].strip()

        if '(' in element and ')' in element:
            open_args, close_args = element.index('('), element.index(')') + 1

            kwargs = self.treat_kwargs(element[open_args:close_args])

            return element[:open_args], kwargs

        return element, None


    def replace_element(self, element: str):
        clean_element, args = self.clean_element(element)
  
        if clean_element.startswith('/'):
            return

        if self.element_found(clean_element):
            attr = getattr(self, clean_element)
            
            child_element = attr(**args) if args else attr()
            self._code = self._code.replace(element, child_element.content())

    def content(self) -> str:
        return self._code

    def render(self) -> str:
        return self._code