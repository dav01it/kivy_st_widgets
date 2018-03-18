import kivy
from kivy.uix.textinput import TextInput
import re
from kivy.core.window import Window
from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'dock')

class FloatInput(TextInput):
    def __init__(self, **kwargs):
       super(FloatInput, self).__init__(**kwargs)
       self._keyboard  = Window.request_keyboard(
           self._keyboard_close, self, input_type='number')
       if self._keyboard.widget:
           vkeyboard = self._keyboard .widget
           vkeyboard.layout = 'numeric.json'

    def _keyboard_close(self):
        pass
    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)
