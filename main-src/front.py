import flet
from flet import *
import requests
from requests import *
import json
import uuid
import regex
import flet as ft
import requests
column_ref = ft.Ref[ft.Column]()
def main(page: ft.Page):
    page.title = "BlogSport"
    page.bgcolor = ft.colors.WHITE
    def route_change(route):
        page.views.clear()
        if page.route == "/home":
            MainFront().build()
    def view_pop(view):
        page.views.pop()
        page.go(page.views[-1].route)
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.views.append(MainFront().build())
    page.update()
class MainFront(UserControl):
    def build(self):
        return ft.View(
            "/home",
            bgcolor=ft.colors.WHITE,
            controls= [ft.Column(expand=True, alignment=ft.MainAxisAlignment.CENTER, controls=[ft.Row(
                    expand=True,
                    wrap=False,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Container(padding=20,content=ft.Text('BlogSport', weight='bold', italic=True,size=35))])]),
                        ]),
flet.app(target=main, port=4000, view=ft.WEB_BROWSER)

