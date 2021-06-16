from dataclasses import dataclass
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from nodes import *


class NodeWidget(Widget):
    def __init__(self, **kwargs):
        super(NodeWidget, self).__init__(**kwargs)
        self.text = "Hello there"
        self.pos = (100, 100)
        self.size_hint = (0.5, 0.4)


class FlowChartApp(App):
    def build(self):
        return NodeWidget()


if __name__ == '__main__':

    # Make UI flowchart
    FlowChartApp().run()
