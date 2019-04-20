# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.uix.popup import Popup
from kivy.uix.button import Button

import time

class CustomPopup(Popup):
    def on_open(self):
        Logger.info('on_open()')
        self.event = Clock.schedule_once(self.on_press_b, 10)

    def on_press_a(self, args):
        Logger.info('A')
        Logger.info(args)
        self.dismiss()

    def on_press_b(self, args):
        Logger.info('B')
        Logger.info(args)
        self.dismiss()

    def on_dismiss(self):
        Logger.info('on_dismiss()')
        self.event.cancel()


class MainApp(App):
    def build(self):
        b = Button(on_press=self.show_popup, text="Show Popup")
        return b

    def show_popup(self, b):
        p = CustomPopup()
        p.open()


if __name__ == '__main__':
    MainApp().run()
