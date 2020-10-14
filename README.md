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

## Run

To test this application use the command:
- `python manage.py compile`

---

This documentation is still in production, so give this repository a star, as soon as possible we will finalize

## Goal

This framework aims to facilitate the creation of html pages using python code. it will be possible to: create reusable elements that can change its parameters, run a local server to view specific pages and components, thus facilitating testing, among other features.
