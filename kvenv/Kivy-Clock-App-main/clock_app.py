from time import strftime
from datetime import date
from kivy import Config
from kivy.lang import Builder

# Initial commit

# Disable fullscreen when not in raspberry pi
Config.set('graphics', 'fullscreen', '0')
Config.write()

# a fixed size is set for the app's display when executed
Config.set("graphics", "height", "480")
Config.set("graphics", "width", "320")

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock


class ClockApp(MDApp):
    # Clock object for the clock(in the app) event
    event_clock = None
    event_date = None

    def build(self):
        """
        The build function is the main entry point for the build system. It
        creates a new Builder object.
        :return: A MainScreen Object containing the main screen to the app
        """
        return MainScreen()
        # return Builder.load_file('hot_reload.kv')

    def on_start(self):
        """
        The on_start function is called when the app is first opened. It creates a
        Clock event that calls the root widget's clock_update and chrono_update functions to
        update the clock and chrono in real time.
        """

        self.event_clock = Clock.schedule_interval(self.root.clock_update, 1)
        self.event_date = Clock.schedule_interval(self.root.display_date, 2)


class MainScreen(MDScreen):
    # Clock object for the Chrono event
    event_chrono = None

    def __init__(self, **kw):
        super().__init__(**kw)
        self.tiktok = True

    def display_date(self, dt):
        today = date.today()
        self.date_label.text = today.strftime("%d/%m/%Y [b] %a [/b]")

    def clock_update(self, dt):
        if(self.tiktok == True):
            self.tiktok = False
            self.time_label.text = strftime("%I[color=#453345]:[/color]%M %p")
        else:
            self.tiktok = True
            self.time_label.text = strftime("%I:%M %p")

        # self.time_label.text = strftime("%I:%M:%S %p")

if __name__ == "__main__":
    from kivy.core.text import LabelBase

    # Register the different font files(.ttf) to the LabelBase with a specific font_name
    # for easy referencing in both the .kv and .py files

    LabelBase.register(
        name="Roboto",
        fn_regular="assets/fonts/Roboto-Regular.ttf",
        fn_bold="assets/fonts/Roboto-Medium.ttf"
    )
    LabelBase.register(
        name="LLPIXEL3",
        fn_regular="assets/fonts/LLPIXEL3.ttf",
    )
    LabelBase.register(
        name="DisplayOTF",
        fn_regular="assets/fonts/DisplayOTF.otf",
    )
    # Run the App
    ClockApp().run()
