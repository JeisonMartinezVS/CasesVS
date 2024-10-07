import reflex as rx

from CasesVS.pages.cases import cases
from CasesVS.pages.navbar import navbar
from rxconfig import config

class State(rx.State):
    """The app state."""

    ...

def index() -> rx.Component:
    return rx.vstack(
            navbar(),
        rx.container(
                cases(),
                class_name=""
            ),
        class_name="bg-white w-full h-full p-0 m-0"
        ),


app = rx.App()
app.add_page(index)
