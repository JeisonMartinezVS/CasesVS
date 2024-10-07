import reflex as rx

def navbar() -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.image(
                src="/LogoVS.png",
                class_name="w-[30px] h-[30px]"
                ),
            rx.text(
                "Casos VirtualSoft",
                class_name="size-6 font-bold uppercase"
                ),
            class_name="items-center"
            ),
        class_name="bg-black text-white border-b-4 mb-2 w-full"
    )