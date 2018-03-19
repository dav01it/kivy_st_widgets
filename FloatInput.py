import kivy
from kivy.uix.textinput import TextInput
import re
from kivy.core.window import Window
from kivy.config import Config

#Config.set('kivy', 'keyboard_mode', 'dock')

class FloatInput(TextInput):
    def __init__(self, **kwargs):
        super(FloatInput, self).__init__(**kwargs)

        Window.allow_vkeyboard = True
        Window.single_vkeyboard = True
        Window.docked_vkeyboard = True
        print "activated dock"
        self.bind(focus=self.on_focus)
        self.keyboard = ""

    def on_focus(self,instance, value):
        if value:
            print('User focused', instance)
            if self.keyboard == "":
                self.keyboard = Window.request_keyboard(self.keyboard_close, self)

            if self.keyboard.widget:
                vkeyboard = self._keyboard.widget
                vkeyboard.layout = 'numeric.json'
                #vkeyboard.show()

        else:
            if self.keyboard.widget:
                vkeyboard = self._keyboard.widget
                vkeyboard.layout = 'qwerty'
            print('User defocused', instance)

    def keyboard_close(self):
        pass


    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)
