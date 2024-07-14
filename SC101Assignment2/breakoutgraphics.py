"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(window_width-paddle_width)/2,
                            y=window_height-(paddle_offset + paddle_height))
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(width=ball_radius*2, height=ball_radius*2, x=window_width/2 - ball_radius,
                          y=window_height/2 - ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_start)

        # Draw bricks
        self.brick_number = 0
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(width=brick_width, height=brick_height, x=j * (brick_width + brick_spacing),
                                   y=brick_offset + i * (brick_height + brick_spacing))
                self.brick_number += 1
                self.brick.filled = True
                if i < brick_rows/5:
                    self.brick.fill_color = "red"
                elif i < brick_rows/5 * 2:
                    self.brick.fill_color = "orange"
                elif i < brick_rows/5 * 3:
                    self.brick.fill_color = "yellow"
                elif i < brick_rows/5 * 4:
                    self.brick.fill_color = "green"
                elif i < brick_rows/5 * 5:
                    self.brick.fill_color = "blue"
                self.window.add(self.brick)

        # 球的初始座標
        self.ball_initial_x = window_width/2 - ball_radius
        self.ball_initial_y = window_height/2 - ball_radius

        self.brick_width = brick_width
        self.ball_center_x = self.ball.x + self.ball.width/2
        self.ball_center_y = self.ball.y + self.ball.height/2

        self.obj_list = []
        self.hit = []

    # 讓板子跟著滑鼠水平移動
    def paddle_move(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width / 2
        if self.paddle.x < 0:
            self.paddle.x = 0
        elif self.paddle.x + self.paddle.width > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

    # 如果球處於停止狀態就取得速度
    def ball_start(self, mouse):
        if self.__dy == 0:
            self.get_velocity()

    def get_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # 讓球以得到的速度進行移動
    def ball_move(self):
        self.ball.move(self.__dx, self.__dy)

    # 偵測球是否撞到牆壁(上、左、右)，有則反彈
    def is_hit_the_wall(self):
        if self.ball.x <= 0 or (self.ball.x + self.ball.width) > self.window.width:
            self.__dx = -self.__dx
        elif self.ball.y <= 0:
            self.__dy = -self.__dy

    # 偵測球的四個角落座標是否有撞到物體
    def is_hit_object(self):
        self.ball_center_x = self.ball.x + self.ball.width / 2
        self.ball_center_y = self.ball.y + self.ball.height / 2
        obj_1 = self.window.get_object_at(self.ball.x, self.ball.y)  # 左上
        obj_2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)  # 右上
        obj_3 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)  # 右下
        obj_4 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)  # 左下
        self.obj_list = [obj_1, obj_2, obj_3, obj_4]
        self.hit = []
        for obj in self.obj_list:  # 將四個角落的狀態變成list
            if obj is not None and obj is not self.paddle:
                self.hit.append("brick")
            else:
                self.hit.append("false")

        if self.paddle in self.obj_list:
            self.after_hit_paddle()
        elif "brick" in self.hit:
            if self.hit[0] is "brick":
                self.is_hit_sidewall(obj_1)
                self.window.remove(obj_1)
                self.brick_number -= 1
            elif self.hit[1] is "brick":
                self.is_hit_sidewall(obj_2)
                self.window.remove(obj_2)
                self.brick_number -= 1
            elif self.hit[2] is "brick":
                self.is_hit_sidewall(obj_3)
                self.window.remove(obj_3)
                self.brick_number -= 1
            elif self.hit[3] is "brick":
                self.is_hit_sidewall(obj_4)
                self.window.remove(obj_4)
                self.brick_number -= 1


    def after_hit_paddle(self):
        self.ball_center_x = self.ball.x + self.ball.width/2
        self.ball_center_y = self.ball.y + self.ball.height/2
        # 如果球心不在 "低於板子上緣且超過板子左右邊界" 的位置
        if not (self.ball_center_y > self.paddle.y and (self.ball_center_x < self.paddle.x or self.ball_center_x > self.paddle.x + self.paddle.width)):
            self.__dy = -self.__dy
            self.ball.y = self.paddle.y - self.ball.height
        # 如果"球心在板子左側且x速度為正" 或 "球心在板子右側且x速度為負" 則反彈
        elif (self.ball_center_x < self.paddle.x and self.__dx > 0) or (self.ball_center_x > self.paddle.x + self.paddle.width and self.__dx < 0):
            self.__dx = -self.__dx
            self.ball_move()

    def is_hit_sidewall(self, obj):
        if abs(self.__dx) <= abs(self.__dy):
            if obj.x <= self.ball.x + self.ball.width/2 <= obj.x + self.brick_width:
                self.__dy = -self.__dy
            else:
                self.__dx = -self.__dx
        else:
            if obj.x <= self.ball.x + self.ball.width / 2 <= obj.x + self.brick_width:
                self.__dy = -self.__dy
            else:
                self.__dx = -self.__dx

    # 球是否掉出視窗的下邊界
    def is_over(self):
        if self.ball.y + self.ball.height > self.window.height:
            self.ball.x = self.ball_initial_x
            self.ball.y = self.ball_initial_y
            self.__dx = 0
            self.__dy = 0
            return True

    # 視窗中的磚塊是否都清光
    def is_win(self):
        if self.brick_number == 0:
            return True
