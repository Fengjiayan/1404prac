from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # basic data (model) example - list of names
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.names:
            # create a label for each name
            name_label = Label(text=name)
            # add the label to the "main" layout widget
            self.root.ids.main.add_widget(name_label)


DynamicWidgetsApp().run()
