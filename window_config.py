from kivy.config import Config

from constants import WIDTH, HEIGHT, MIN_H, MIN_W

Config.set('kivy', 'exit_on_escape', '0')
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', WIDTH)
Config.set('graphics', 'height', HEIGHT)
Config.set('graphics', 'minimum_width', MIN_W)
Config.set('graphics', 'minimum_height', MIN_H)

