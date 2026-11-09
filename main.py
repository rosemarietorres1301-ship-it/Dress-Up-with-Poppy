import flet as ft


def main(page: ft.Page):
    # Page settings
    page.title = "What Is Poppy Wearing Today?"
    page.bgcolor = ft.Colors.PINK_50
    page.padding = 20

    # Header
    title = ft.Text(
        "What Is Poppy Wearing Today?",
        size=28,
        weight=ft.FontWeight.BOLD,
    )

    # Area where Poppy will appear (empty for now)
    poppy_area = ft.Container(
        width=300,
        height=400,
        bgcolor=ft.Colors.WHITE,
        border_radius=ft.BorderRadius.all(10),
    )

    # Area where the controls will go (empty for now)
    controls_area = ft.Container(
        width=300,
        height=400,
        bgcolor=ft.Colors.GREY_100,
        border_radius=ft.BorderRadius.all(10),
        padding=10,
    )

    # Add everything to the page: title on top, the two areas side by side
    page.add(
        title,
        ft.Row([poppy_area, controls_area]),
    )


ft.run(main)