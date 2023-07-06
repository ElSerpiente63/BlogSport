import flet as ft



class AdminPanel(ft.View):
    def build(self, token:str, username: str):
        return ft.View(
            "/admin",
            controls=[
                ft.Row(expand=True,controls=[ft.Container(
                width=400,
                height=400,
                content=ft.Text("Dashboard",size=40, text_color=ft.colors.BLACK),
                alignment=ft.MainAxisAlignment.CENTER,
                bgcolor=ft.colors.WHITE)])
        ]
    )