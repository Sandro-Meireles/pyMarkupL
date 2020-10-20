# pyMarkupL (Python Markup language)
Streamline the production of your HTML page using this python framework

## Installation
 - Download/Clone this repository `git clone https://github.com/Sandro-Meireles/pyMarkupL.git`
 
 This framework will be added future in PyPi
 
## Understanding the Structure

This is the structure of the files in the repository.


```
│   .gitignore
│   debug.py
│   manage.py
│   README pt-br.md
│   README.md
│   settings.py
│
├── core
│   │   elements.py
│   └── exceptions.py
│  
└── src
    │   main.py
    │
    └── components
        │   box.py
        │   toolbar.py
        │
        └──static
            └── style.py   
```

The way the entire project is structured is at the discretion of the developer, I used this pattern as an example only.

- `settings.py` Where we configure some aspects of our project.

```py
from src.main import Main

MAIN_ELEMENT = Main
```
`MAIN_ELEMENT` Is a constant, where we tell our project which is the main element,which in this example is `Main`.

These constants can be changed at any time, again, as stated before:
the way the entire project is structured is at the discretion of the developer.

- `src/` All components of that project are found here.

```
└── src
    │   main.py
    │
    └── components
        │   box.py
        │   toolbar.py
        │
        └──static
            └── style.py
```

- `src/main.py` Contains the main element, the one that was called in `settings.py`

```py
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
            </div>
        '''
```
See how simple it is to create an element.
```py
from core.elements import Element
```
- We import of `Element` which is in `core.elements`  
This is an abstract class, to create an element just inherit it and add/modify some parameters and methods.

```py

class Main(Element):
    ...
```
- We created a class that inherits from `Element`, thus indicating that `Main` is an element  
With just these steps we already have an element, however, it does not render anything, if you try to run an element like this you will receive an EmptyCode error.
That's why the `render` method exists.

```py
def render(self, **kwargs) -> str:
    return '''
        ...
    '''
```
- The "render" method is responsible for returning one or more elements, both HTML and pML Elememnts (Classes that inherit from `Element`).
This method must return a `str` and, within that string, can contain HTML elements:
```html
<div class="container">
    ...
</div>
```
and pML elements:
```html
<toolbar(title="pyMarkupL")>
```
There is no limit on the number of elements being returned, be careful only with the syntax, because depending on the error nothing will be raised.  
Don't worry if you can't understand what `<toolbar(title="pyMarkupL")>` does, or how it works, right after this topic we'll explain everything right.

## Run

To test this application use the command:
- `python manage.py run`

This will generate a file in `output/debug` named `debug.html` as configured in `settings.py`.  
To modify the path of this file change the constant `UTPUT_DEBUG` in `settings.py`

---

This documentation is still in production, so give this repository a star, as soon as possible we will finalize

## Goal

This framework aims to facilitate the creation of html pages using python code. it will be possible to: create reusable elements that can change its parameters, run a local server to view specific pages and components, thus facilitating testing, among other features.
