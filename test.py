import kivy

kivy.require('1.0.6')  # replace with your current kivy version !

from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

start_time = datetime.now()

class MyApp(App):
    def build(self):
        self.modes = (
            '%I:%m:%S',
            '%H:%m:%S %P',
            '%S:',
        )
        self.mode = 0
        self.main_box = BoxLayout(orientation='vertical')

        self.button = Button(text='00:00', font_size=100)
        self.main_box.add_widget(self.button)

        self.button.bind(on_press=self.tap)
        Clock.schedule_interval(self.timer, 1)

        return self.main_box

    def tap(self, button):
        if self.mode + 1 == len(self.modes):
            self.mode = 0
        else:
            self.mode += 1

    def timer(self, dt):
        difference = datetime.now() - start_time
        minutes = (difference.total_seconds() % 3600) // 60
        seconds = difference.total_seconds() % 60
        self.button.text = '%02d:%02d' % (int(minutes), int(seconds))


if __name__ == '__main__':
    MyApp().run()