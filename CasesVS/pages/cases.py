import reflex as rx

def datatableCase():
    return rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Full name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Group"),
                    class_name="text-black"
                ),
            ),
            rx.table.body(
                rx.table.row(
                    rx.table.row_header_cell("Danilo Sousa"),
                    rx.table.cell("danilo@example.com"),
                    rx.table.cell("Developer"),
                ),
                rx.table.row(
                    rx.table.row_header_cell("Zahra Ambessa"),
                    rx.table.cell("zahra@example.com"),
                    rx.table.cell("Admin"),
                ),
                rx.table.row(
                    rx.table.row_header_cell("Jasper Eriks"),
                    rx.table.cell("jasper@example.com"),
                    rx.table.cell("Developer"),
                ),
            ),
        width="100%"
    )
   
def cases() -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.button(
                rx.icon('plus'),
                "Nuevo Caso"
                ),
            rx.input(
                rx.input.slot(
                    rx.icon(tag="search"),
                ),
                placeholder="Buscar Caso",
                class_name=""
                ),
        ),
        rx.box(
            datatableCase(),
            class_name="mt-5"
            ),
        class_name=""
    )