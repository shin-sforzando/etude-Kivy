# -*- coding: utf-8 -*-

import kivy
kivy.require('1.10.1')
from kivy import Logger
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class MainApp(App):
    class MyPopupContent(BoxLayout):
        def __init__(self, **args):
            super(this, self).__init__(**args)

    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.popup = Popup(title='MyPopup', content=self.MyPopupContent())

    def on_open(self, args):
        self.popup.open()


if __name__ == '__main__':
    MainApp().run()
