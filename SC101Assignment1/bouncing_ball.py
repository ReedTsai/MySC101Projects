"""
File: Bouncing-Ball program
Name: DK
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.8
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')

gate = False  # when gate is True, the ball will bounce.
time = 0
vy0 = 0
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
i = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    ball.filled = True
    window.add(ball)

    onmouseclicked(click)


def click(mouse):
    global gate, vy0, time, i, ball
    if gate is False and i + 1 <= 3:
        gate = True
        while True:
            vy = vy0 + time * GRAVITY
            ball.move(VX, vy)
            pause(DELAY)
            time += 1
            if ball.x < window.width:
                if ball.y + SIZE > window.height:  # 如果ball低於畫面，強制讓ball回到地平線上
                    ball.y = window.height - SIZE
                    time = 0
                    vy0 = -vy * REDUCE
            else:
                ball.x = START_X
                ball.y = START_Y
                break
        gate = False
        i += 1


if __name__ == "__main__":
    main()
