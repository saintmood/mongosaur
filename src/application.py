import urwid

from src.handlers import StartHandler
from src.views import StartView

class Application:

    def __init__(self):
        handler = StartHandler() 
        self.loop = None
        self.view = StartView(handler)
    
    def main(self):
        self.loop = urwid.MainLoop(self.view, self.view.palette)
        self.loop.run()


def main():
    Application().main()


if __name__ == '__main__':
    main()