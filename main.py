import urwid

txt = urwid.Text(u"Hello World")
fill = urwid.Filler(txt, 'top')

if __name__ == '__main__':
    loop = urwid.MainLoop(fill)
    loop.run()