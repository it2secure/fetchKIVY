from kivy.uix.boxlayout import BoxLayout
from kivy.clock import mainthread

class MyBoxLayout(BoxLayout):

    def init(self, **kwargs):
        super().__init__(**kwargs)

        @mainthread  # execute within next frame
        def delayed():
            self.load_random_car()
        delayed()

    def load_random_car(self):
        self.ids.label.text = "fetch random car data from db and put here"

    