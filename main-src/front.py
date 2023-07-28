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
textfield_username_ref = ft.Ref[ft.TextField]()
textfield_password_ref = ft.Ref[ft.TextField]()
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

class LoginAdmin(UserControl):
    def build(self):
        return ft.View(
            "/login",
            bgcolor=ft.colors.WHITE,
            controls=[
                ft.Column(expand=True, wrap=False, alignment=ft.MainAxisAlignment.CENTER, controls=[ft.TextField(ref=textfield_username_ref, label="username"), ft.TextField(ref=textfield_password_ref, label="password", password=True), ft.TextButton("Login")])
            ]
        )




class MainFront(UserControl):
    def build(self):
        self.column_append = ft.Column(scroll="always",expand=True, alignment=ft.MainAxisAlignment.SPACE_EVENLY,controls=[])
        #self.__row__ = ft.Row(expand=True,alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START, wrap=False, controls=[self.column_append])
        self.card = ft.Card(elevation=10, surface_tint_color=ft.colors.LIGHT_GREEN, content=ft.Container(width=400, height=700, bgcolor=ft.colors.BLACK))
        self._column = ft.Column(expand=True,scroll="always",alignment=ft.MainAxisAlignment.START, wrap=False, controls=[], horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=50)
        self.view =  ft.View(
            "/home",
            bgcolor=ft.colors.WHITE,
            controls=[
                ft.Column(expand=True, wrap=False, alignment=ft.MainAxisAlignment.START, controls=[
                    ft.Row(alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER, controls=[ft.Container(padding=padding.only(bottom=40, top=40 ),content=ft.Text('Blogsport', size=18, weight="bold")), ft.Row(expand=True, wrap=False, alignment=ft.MainAxisAlignment.END, vertical_alignment=ft.CrossAxisAlignment.CENTER, controls=[ft.TextButton('Login')])]),
                    ft.Row(expand=True,wrap=False,controls=[self._column], alignment=ft.MainAxisAlignment.CENTER),
                    ]),
            ])
        #on travaille d'abord avec une liste de titres
        self.response = requests.get('http://127.0.0.1:4001/articles')
        self.__list__ = []
        def on_container_click(index):
            def click_handler(e):
                print(self.response.json()[index]["title"])
                News(self.response.json()[index]["id"],self.response.json()[index]["title"])
            return click_handler

        if self.response.status_code == 200:
            for i in range(len(self.response.json())):
                self._ref_ = Ref[Container]()
                self.__container__ = ft.Container(
                    width=900,
                    height=150,
                    content=ft.Text(str(self.response.json()[i]["title"]), weight="bold"),
                    alignment=ft.alignment.top_center,
                    border_radius=5,
                    bgcolor=ft.colors.WHITE,
                    on_click=on_container_click(i)  # Utilise la fonction intermédiaire ici
                )
                self._column.controls.append(ft.Card(elevation=5, content=self.__container__))
        else:
            print("Status not done")
        return self.view

#mettre le texte sur une ligne chaque 60 caractères, police 18
class News(UserControl):
    def __init__(self, ide: str,title: str):
        self.title = title 
        self.ide = ide
        self.json = {"ide":self.ide}
        self.response = requests.post('http://127.0.0.1:4001/content', json=self.json)
        print(self.response.json())
        self.create_view()

    def create_view(self):
        return ft.View(
            f"/{self.title}",
            controls = [
                ft.Text("Something", weight="bold")
            ]
        )   
flet.app(target=main, port=4000, view=ft.WEB_BROWSER)

