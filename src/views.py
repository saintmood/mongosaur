import urwid 


class StartView(urwid.WidgetWrap):
    palette = []

    def __init__(self, handler):
        self.handler = handler

