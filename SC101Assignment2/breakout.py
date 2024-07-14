"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

這個程式讓使用者可以進行打磚塊遊戲的編寫，所有會用到的method都在coder端寫好
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()  # 叫出遊戲的基本畫面
    life = NUM_LIVES
    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        graphics.ball_move()  # 讓球移動
        graphics.is_hit_the_wall()  # 偵測球是否撞到牆壁(上、左、右)，有則反彈
        graphics.is_hit_object()  # 偵測球的四個角落座標是否有撞到物體
        if graphics.is_over():  # 如果球掉出視窗下邊界
            life -= 1
            if life == 0:
                print("GAME OVER!")
                break
        elif graphics.is_win():  # 如果磚塊都清空
            print("YOU WIN!!")
            break


if __name__ == '__main__':
    main()
