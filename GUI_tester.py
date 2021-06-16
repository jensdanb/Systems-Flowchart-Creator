# For now, this is a test lab. Will move that to separate file and put actual main code here later.

from kivy.app import App
from kivy.uix.button import Button

from nodes import *


class NodeButton(Button):
    def __init__(self, **kwargs):
        super(NodeButton, self).__init__(**kwargs)
        self.text = "Hello there"
        self.pos = (100, 100)
        self.size_hint = (0.5, 0.4)


class FlowChartApp(App):
    def build(self):
        return NodeButton()


if __name__ == '__main__':

    # Make UI flowchart
    FlowChartApp().run()