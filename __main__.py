# author: Christopher Thomas ~ github.com/CCThomas
# created: Oct 19th 2017

from gui.window import Window
import sys

if sys.version_info < (3, 0):
    print("Python version 3+ required")
    print("Download Python 3: https://www.python.org/downloads/")

# Main Code
test = True

if test:
    from test import console
    console.start()
else:
    my_window = Window()
    my_window.mainloop()
