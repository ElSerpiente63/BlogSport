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
                ft.Column(expand=True, wrap=False, alignment=ft.MainAxisAlignment.CENTER, controls=[ft.TextField(ref=textfield_username_ref, label="username"), ft.TextField(ref=textfield_password_ref, label="password", passwrd=True), ft.TextButton("Login")])
            ]
        )

class MainFront(UserControl):
    def build(self):
        self.column_append = ft.Column(scroll="always",expand=True, alignment=ft.MainAxisAlignment.SPACE_EVENLY,controls=[])
        self.view =  ft.View(
            "/home",
            bgcolor=ft.colors.WHITE,
            controls=[
                ft.Column(expand=True, wrap=False, alignment=ft.MainAxisAlignment.START, controls=[ft.Row(alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER, controls=[ft.Container(padding=40, content=ft.Text('Blogsport'))]), ft.Row(alignment=ft.MainAxisAlignment.END, vertical_alignment=ft.CrossAxisAlignment.START, controls=[ft.Container(height=200,alignment=ft.alignment.top_left,padding=padding.only(right=20, bottom=50),content=ft.TextButton('Login', on_click=lambda e: e.page.go('/login')))]), ft.Row(expand=True, wrap=False, alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.STRETCH, controls=[self.column_append])])
            ])
        #on travaille d'abord avec une liste de titres
        self.response = requests.get('http://127.0.0.1:4001/articles')
        if self.response.status_code == 200:
            for i in range(len(self.response.json())):
                self.column_append.controls.append(ft.Container(
                    width=200,
                    height=200,
                    content=ft.Text(str(self.response.json()[i]), weight="bold"),
                    alignment=ft.alignment.top_center,
                ))
        else:
            print("Status not done")
        return self.view   
flet.app(target=main, port=4000, view=ft.WEB_BROWSER)

