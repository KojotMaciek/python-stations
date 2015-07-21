#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter

class app(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        pass
        

if __name__ == "__main__":
    app = app(None)
    app.title('my application')
    app.mainloop()
