
import kivy
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import FloatInput

kv = """
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
ScreenManager:
    transition: FadeTransition()
    FirstScreen:
#    SecondScreen:
<FirstScreen>:
    #menu principale
    first_screen: first_screen
    name: '_first_screen_'
    BoxLayout:
        orientation: 'vertical'
        spacing: 1 
        Label:
            size_hint_y: 0.15
            id: first_screen
            text: "Main Menu"
            
        Button:
            size_hint_y: 0.25
            text: "exit"
            on_release: app.ap_exit()
        FloatInput:
            size_hint_y: 0.15
            font_size : dp(26)
            id: testFloat
            text: "0"
        Label:
            #size_hint_y: 0.15
            id: first_screen
            text: ""

"""

class TestApp(App):


    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)

    def build(self):

            self.root_widget=Builder.load_string(kv)
            #self.leggi_config()
            return self.root_widget
    def ap_exit(self):
        exit (0)
class FirstScreen(Screen):
    pass

if __name__ == '__main__':

    TestApp().run()

