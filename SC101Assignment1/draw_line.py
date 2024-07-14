"""
File: Draw_a_Line program
Name: DK
-------------------------
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()
SIZE = 10
second_click = False
p1_x = 0
p1_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(click)


def click(mouse):
    """
    For first click, a circle is made.
    For second click, a line is drawn from the point of first click and the point of second click.
    """
    global second_click, p1_x, p1_y
    if second_click is False:
        first_click = GOval(SIZE, SIZE, x=(mouse.x - SIZE/2), y=(mouse.y - SIZE/2))
        window.add(first_click)
        p1_x = mouse.x
        p1_y = mouse.y
        second_click = True
    else:
        start = window.get_object_at(p1_x, p1_y)
        p2_x = mouse.x
        p2_y = mouse.y
        line = GLine(p1_x, p1_y, p2_x, p2_y)
        window.remove(start)
        window.add(line)
        second_click = False


if __name__ == "__main__":
    main()
