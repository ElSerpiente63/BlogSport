import flet
from flet import *
import requests
from requests import *
import json
import uuid
import regex



class MainFront(UserControl):
    def build(self):
        return View(
            "/articles",
            bgcolor=colors.WHITE,
            controls= [Row(expand=True, alignment=MainAxisAlignment.CENTER, controls=[Column(
                    expand=True,
                    wrap=False,
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Text('BlogSport', weight='bold', italic=True,size=35)
                    ])])])