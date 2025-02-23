# api/index.py
from nicegui import ui

@ui.page('/')
def home():
    ui.label('Welcome to my NiceGUI app!')
    ui.button('Click me!', on_click=lambda: ui.notify('Button clicked!'))

ui.run(server='flask')
