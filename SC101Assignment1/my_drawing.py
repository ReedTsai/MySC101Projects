"""
File: House
Name: DK
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: House

    This is how I imagined my retirement life would be.
     Live in the slow-paced countryside and enjoy the phytoncides of the woods
    """
    window = GWindow(width=800, height=600)
    background = GRect(800, 600)
    background.filled = True
    background.fill_color = "lightblue"
    window.add(background)

    horizon = GLine(50, 550, 750, 550)
    window.add(horizon)

    house = GRect(200, 150, x=120, y=400)
    house.filled = True
    house.fill_color = "darkgray"
    window.add(house)

    roof = GPolygon()
    roof.add_vertex((220, 320))
    roof.add_vertex((90, 400))
    roof.add_vertex((350, 400))
    roof.add_vertex((220, 320))
    roof.filled = True
    roof.fill_color = "firebrick"
    window.add(roof)

    door = GRect(70, 100, x=220, y=450)
    handle = GOval(10, 10, x=270, y=495)
    door.filled = True
    door.fill_color = "mediumblue"
    window.add(door)
    handle.filled = True
    handle.fill_color = "gold"
    window.add(handle)

    sun = GOval(120, 120, x=550, y=100)
    l1 = GRect(15, 50, x=605, y=35)
    l2 = GOval(25, 25, x=670, y=80)
    l3 = GRect(50, 15, x=680, y=150)
    l4 = GOval(25, 25, x=670, y=210)
    l5 = GRect(15, 50, x=605, y=230)
    l6 = GOval(25, 25, x=535, y=210)
    l7 = GRect(50, 15, x=480, y=150)
    l8 = GOval(25, 25, x=535, y=80)
    sun.filled = True
    sun.fill_color = "gold"
    l1.filled = True
    l1.fill_color = "gold"
    l2.filled = True
    l2.fill_color = "gold"
    l3.filled = True
    l3.fill_color = "gold"
    l4.filled = True
    l4.fill_color = "gold"
    l5.filled = True
    l5.fill_color = "gold"
    l6.filled = True
    l6.fill_color = "gold"
    l7.filled = True
    l7.fill_color = "gold"
    l8.filled = True
    l8.fill_color = "gold"
    window.add(sun)
    window.add(l1)
    window.add(l2)
    window.add(l3)
    window.add(l4)
    window.add(l5)
    window.add(l6)
    window.add(l7)
    window.add(l8)

    tree = GPolygon()
    tree.add_vertex((600, 320))
    tree.add_vertex((500, 420))
    tree.add_vertex((700, 420))
    tree.add_vertex((600, 320))
    tree.filled = True
    tree.fill_color = "darkgreen"
    window.add(tree)
    tree1 = GPolygon()
    tree1.add_vertex((600, 380))
    tree1.add_vertex((500, 480))
    tree1.add_vertex((700, 480))
    tree1.add_vertex((600, 380))
    tree1.filled = True
    tree1.fill_color = "darkgreen"
    window.add(tree1)
    tree2 = GRect(50, 70, x=575, y=480)
    tree2.filled = True
    tree2.fill_color = "brown"
    window.add(tree2)


if __name__ == '__main__':
    main()
