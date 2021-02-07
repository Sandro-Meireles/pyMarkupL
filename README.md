<img src="https://image.prntscr.com/image/xrHhAMB7T-CWvSU1u9_myw.png" width="550" align="right">

# pyMarkupL
(Python Markup Language) Streamline the production of your HTML page using this python framework.

Creating an HTML page can be very repetitive,
often having to copy and paste multiple lines
code to modify minimal things, like a
description.

pyMarkupL greatly speeds up this process, giving
possibility to create elements with parameters
and / or fully customizable sub-elements.

## Installation
 - To install pyMarkupL, simply run this command in your terminal of choice:  
 `> pip install pyMarkupL`

Right after installation, the command `pml` will be available, to check if everything was installed correctly open a terminal and do the following command:
-  `> pml ok`

If you do not receive a response it means there was a problem during installation.

## Starting a project
To start developing your page, you must first organize your work environment.  
Enter a directory where you want to store your code, run the following command:
- `> pml init`

This command will generate a set of files needed to run your application, to do a brief test, run `manage.py` passing as `run` argument:
- `> python manage.py run`

This will generate a file in `output/debug` named `debug.html` as configured in `settings.py`.  
For more information on how to generate your page go to the "Run" topic.
## Understanding the Structure


This is the structure of the files in the repository.


```
│   settings.py
│    manage.py
│  
└── src
    │   main.py
    │
    └── components
        │   box.py
        │   toolbar.py
        │   text.py
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
        │   text.py
        │
        └──static
            └── style.py 
```

- `src/main.py` Contains the main element, the one that was called in `settings.py`

```py
from core.elements import Element
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
<Toolbar(title="pyMarkupL")>
```
There is no limit on the number of elements being returned, be careful only with the syntax, because depending on the error nothing will be raised.  
Don't worry if you can't understand what `<Toolbar(title="pyMarkupL")>` does, or how it works, right after this topic we'll explain everything right.  
...

## Run

To test this application use the command:
- `> python manage.py run`

This will generate a file in `output/debug` named `debug.html` as configured in `settings.py`.  
To modify the path of this file change the constant `UTPUT_DEBUG` in `settings.py`

---

This documentation is still in production, so give this repository a star, as soon as possible we will finalize

## Goal

This framework aims to facilitate the creation of html pages using python code. it will be possible to: create reusable elements that can change its parameters, run a local server to view specific pages and components, thus facilitating testing, among other features.
