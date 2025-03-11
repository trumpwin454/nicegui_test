from fastapi import FastAPI
from nicegui import ui

app = FastAPI()

# FastAPI route
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI with NiceGUI!"}

# Initialize NiceGUI app
def nicegui_app():
    with ui.row():
        ui.label('Hello, this is a NiceGUI interface with FastAPI!')
        ui.button('Click Me', on_click=lambda: ui.label('You clicked the button!'))

# Mount NiceGUI to FastAPI
ui.init()
app.mount("/ui", ui.app)

# Run the NiceGUI app in the background
ui.run(nicegui_app)
