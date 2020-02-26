from kivy.app import App

from kivy.clock import Clock

from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.graphics import Rectangle, Color

import kivy.utils

from datetime import datetime

from constants import FIELD_SIZE, WIDTH, HEIGHT

import window_config

from kivy.core.window import Window

import game_processing

game_processing.fill_map()
game_processing.fill_map_solution()

click_counter = 0
start_time = datetime.now()

if __debug__:
    class MainMenu(BoxLayout):
        def __init__(self, **kwargs):
            super(MainMenu, self).__init__(**kwargs)
            Window.bind(on_key_down=self._on_keyboard_down)

        def _on_keyboard_down(self, instance, keyboard, keycode, text,
                              modifiers):
            if text == 'a':
                game_processing.end_game = True
else:
    pass


class NpazzleApp(App):
    def build(self):
        Clock.schedule_interval(self.timer, 1)
        if __debug__:
            main_layout = MainMenu()
        else:
            main_layout = BoxLayout()

        information_layout = BoxLayout(orientation='vertical',
                                       size_hint=(.3, 1))
        with information_layout.canvas:
            Color(kivy.utils.get_color_from_hex('#CCCCCC'))
            Rectangle(pos=(WIDTH * 1.54, 4), size=(WIDTH * .46, HEIGHT * 1.99))

        self.timer_lable = Label(text='[color=000]00:00[/color]',
                                 font_size='25sp', markup=True,
                                 size_hint=(1, .05))
        self.click_info = Label(text='[color=000]0[/color]',
                                font_size='25sp', markup=True,
                                size_hint=(1, .05))

        information_layout.add_widget(Label(text='[color=000]Game time:[/color]',
                                            font_size='20sp', markup=True,
                                            size_hint=(1, .15)))
        information_layout.add_widget(self.timer_lable)
        information_layout.add_widget(Widget(size_hint=(1, .1)))
        information_layout.add_widget(
            Label(text='[color=000]Total number of movements:[/color]',
                  font_size='20sp', text_size=(280, None), halign='center',
                  markup=True, size_hint=(1, .15)))
        information_layout.add_widget(self.click_info)
        information_layout.add_widget(Widget())


        self.widgets = list()
        self.field_layout = GridLayout(cols=FIELD_SIZE,
                                       rows=FIELD_SIZE)
        self.create_gui_field()
        main_layout.add_widget(self.field_layout)
        main_layout.add_widget(information_layout)
        return main_layout

    def timer(self, dt):
        if game_processing.end_game:
            return
        difference = datetime.now() - start_time
        minutes = (difference.total_seconds() % 3600) // 60
        seconds = difference.total_seconds() % 60
        self.timer_lable.text = '[color=000]%02d:%02d[/color]' % (
            int(minutes), int(seconds))

    def get_index_free_cell(self):
        i = 0
        for widget in self.widgets:
            if type(widget) == Widget:
                return i
            i += 1
        return -1

    def create_gui_field(self):
        self.field_layout.clear_widgets()
        if game_processing.end_game:
            self.field_layout.add_widget(
                Button(text="Game over!\nClick here to exit.",
                       text_size=(500, None), halign='center', font_size='25sp',
                       on_press=self.close))
        else:
            for row in game_processing.field_map:
                for elem in row:
                    if elem == '0':
                        self.widgets.append(Widget())
                        self.field_layout.add_widget(self.widgets[-1])
                    else:
                        self.widgets.append(
                            Button(text=elem, on_press=self.try_move))
                        self.field_layout.add_widget(self.widgets[-1])

    def try_move(self, instance):
        global click_counter
        if game_processing.is_moved(instance.text):
            click_counter += 1
            self.click_info.text = '[color=000]' + str(
                click_counter) + '[/color]'
            self.create_gui_field()

    def close(self, instance):
        exit(0)


if __name__ == '__main__':
    NpazzleApp().run()
