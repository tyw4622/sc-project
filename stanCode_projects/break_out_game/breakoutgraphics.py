"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

Breakout Game contains start by users' click.
It will costs one live if ball drops below the paddle.
If all the bricks are removed, user wins.
Games ends either all three lives are used up or user win the game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

# Constant
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 90     # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15    # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).


INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        self.breakout_game = GLabel('The Breakout Game')
        self.breakout_game.font = 'Times New Roman-30-bold'
        self.breakout_game.color = 'navy'
        self.window.add(self.breakout_game, x=(self.window_width - self.breakout_game.width) / 2,
                        y=self.window_height / 3)

        self.label_tap_to_start = GLabel('Tap to start the game')
        self.label_tap_to_start.font = 'Times New Roman-20-bold'
        self.window.add(self.label_tap_to_start, x=(self.window.width-self.label_tap_to_start.width) / 2,
                        y=self.window.height / 2)

        self.paddle_offset = paddle_offset
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_width = brick_width
        self.brick_height = brick_height
        self._num_lives = 3
        self.if_game_start = False

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.color = 'slategrey'
        self.paddle.fill_color = 'slategrey'
        self.paddle_x = .5*self.window_width-.5*paddle_width
        self.paddle_y = self.window.height-self.paddle_offset
        self.paddle_width = paddle_width

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.color = 'darkcyan'
        self.ball.fill_color = 'darkcyan'
        self.ball_start_x = .5 * self.window.width - .5 * self.ball.width
        self.ball_start_y = .5 * self.window.height + .5 * self.ball.height

        # Default initial velocity for the ball
        self._dx = 0
        self._dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.tap_to_start)

        # check if all bricks are removed
        self.total_brick = self.brick_rows * self.brick_cols
        self.ball_start_position()
        self.if_fail()

        # win label
        self.label_win = GLabel('Congrats! You Win!')
        self.label_win.font = 'Times New Roman-35-bold'
        self.label_win.color = 'orangered'

        # Game over label
        self.label_gg = GLabel('Oops! Game Over!')
        self.label_gg.font = 'Times New Roman-35-bold'

        self.score = 0
        self.label_score = GLabel('score: ')
        self.label_score.color = 'teal'
        self.label_score.font = 'Times New Roman-24-bold'

        self.label_load = GLabel('Loading . . . ')
        self.label_load.font = 'Times New Roman-20-bold'

        self.loading_on = True         # determine if the switch of loading is on (True = can start loading animation)
        self.ready = True              # the loading animation is still running

    def paddle_move(self, event):
        """
         paddle can move within the width of the window at a fixed height
        Input :
            event(GMouseEvent): mouse moved event
        """
        self.paddle.x = event.x
        if event.x >= self.window.width-self.paddle_width:
            self.paddle.x = self.window.width-self.paddle_width

    def get_num_lives(self):
        """
        get numbers of lives
        """
        return self._num_lives

    def set_num_lives(self, new_num_lives):
        """
        users can assign a new number of lives
        """
        self._num_lives = new_num_lives

    def starter(self, event):
        """
        set ball velocity after mouse click
        """
        if self.ready:
            if not self._num_lives == 0:
                if self._dx == 0:
                    self._dx = random.randint(1, MAX_X_SPEED)
                    if random.random() > .5:
                        self._dx = -self._dx
                    self._dy = INITIAL_Y_SPEED
        else:
            pass

    def ball_start_position(self):
        """
        put ball in center of the window( initial position before each round start)
        """
        self.ball.x = self.ball_start_x
        self.ball.y = self.ball_start_y

    def if_fail(self):
        """
        return if the ball drops out of the bound of the window
        """
        if self.ball.y > self.window.height-self.paddle_offset:
            self._num_lives -= 1
            self.ball_start_position()
            self._dx = 0
            self._dy = 0
            onmouseclicked(self.starter)

            live_img_removed = GOval(20, 20, x=self.window.width/3*2 + self._num_lives*30, y=self.paddle.y+20)
            live_img_removed.filled = True
            live_img_removed.fill_color = 'white'
            live_img_removed.color = 'gray'
            self.window.add(live_img_removed)

    def ball_move(self):
        """
        ball move within the bound of the window
        check whether the ball hit the wall
        """
        self.ball.move(dx=self._dx, dy= self._dy )
        self.if_hit_walls()
        self.if_hit_object()
        self.if_fail()

    def if_hit_walls(self):
        """
        determine whether the ball hit the left, right hand sides or top of the window.
        """
        # hit the top
        if self.ball.y <= 0:
            self._dy *= -1

        # hit left or right side of the window
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self._dx *= -1

    def if_hit_object(self):
        """
        Detecting whether the corner of the ball hit the object (bricks or paddle) or not.
        if the ball hits the bricks, remove it before bouncing.
        if the ball hit the paddle, the ball bounces.
        """
        d = BALL_RADIUS * 2    # diameter of ball
        up_left_obj = self.window.get_object_at(self.ball.x, self.ball.y)           # up left corner of the ball
        up_right_obj = self.window.get_object_at(self.ball.x + d, self.ball.y)      # up right corner of the ball
        down_left_obj = self.window.get_object_at(self.ball.x, self.ball.y + d)     # down left corner of the ball
        down_right_obj = self.window.get_object_at(self.ball.x+d, self.ball.y + d)  # down right corner of the ball

        corner_check = (up_left_obj, up_right_obj, down_right_obj, down_left_obj)
        bottom_check = (down_left_obj, down_right_obj)

        # use initial ball position to determine whether ball hit brick or paddle

        # if the ball is above the central of the window => bricks
        if self.ball.y <= self.ball_start_y:
            for i in corner_check:
                if i is not None:
                    self.window.remove(i)
                    self.score += 1
                    self.label_score.text = 'score: ' + str(self.score)
                    self._dy *= -1
                    break                 # make sure each time(bounce) can only remove a brick

        # if the ball is below the central of the window => paddle
        elif self.ball.y > self.ball_start_y:
            for i in bottom_check:
                if i is not None:
                    self._dy *= -1
                    break                  # avoid count one hit twice

    def if_game_end(self):
        """
        determine if the game end (users win the game or use up all the lives).
        if not, keep ball moving.
        """
        # user wins
        if self.score == self.total_brick:
            self.window.add(self.label_win, x= (self.window_width-self.label_win.width)/2, y=self.window_height / 2)
            self._dx = 0
            self._dy = 0

        # users uses up all lives
        elif self._num_lives == 0:
            self.game_over()
            self._dx = 0
            self._dy = 0
        else:
            self.ball_move()

    def game_over(self):
        """
        Show 'Oops ! Game Over!' on the window when all the lives are used.
        """
        pause(200)
        for i in range(self.brick_cols):
            for j in range(self.brick_rows):
                obj_remove = self.window.get_object_at(x=i*self.brick_spacing+i*self.brick_width,
                                                       y=self.brick_offset+j * (self.brick_height+self.brick_spacing))
                self.window.remove(obj_remove)
                pause(30)
        self.window.remove(self.ball)
        self.window.add(self.label_gg, x=self.window_width/2-self.label_gg.width/2, y=self.window_height/2)

    def tap_to_start(self, event):
        """
        After user's first click, show loading animation than put all the objects(ball, paddle, bricks on the window.
        input: mouse click event
        """
        self.window.remove(self.breakout_game)
        self.window.remove(self.label_tap_to_start)

        if self.loading_on:          # if loading animation can be can run
            self.loading_on = False
            self.loading()

        # draw bricks
            color_index = self.brick_cols / 5
            for i in range(self.brick_cols):
                for j in range(self.brick_rows):
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'white'
                    if j < color_index:
                        brick.fill_color = 'navy'
                    elif j < 2*color_index:
                        brick.fill_color = 'blue'
                    elif j < 3*color_index:
                        brick.fill_color = 'royalblue'
                    elif j < 4*color_index:
                        brick.fill_color = 'cornflowerblue'
                    else:
                        brick.fill_color = 'lightsteelblue'
                    self.window.add(brick, x=i*self.brick_spacing+i*self.brick_width,
                                    y=self.brick_offset+j * (self.brick_height+self.brick_spacing))

                    self.window.add(self.paddle, x=self.paddle_x, y= self.paddle_y)
                    self.window.add(self.ball,x=self.ball_start_x,y=self.ball_start_y)
                    self.window.add(self.label_score, x=self.window.width / 15, y=self.paddle.y + 48)

                    # put lives images on the window
                    for k in range(self._num_lives):
                        live_img = GOval(20, 20, x=self.window.width / 3 * 2 + k * 30, y=self.paddle.y + 20)
                        live_img.filled = True
                        live_img.fill_color = 'paleturquoise'
                        live_img.color = 'paleturquoise'
                        self.window.add(live_img)
                self.ready = True
                onmouseclicked(self.starter)

    def get_dy(self):
        """
        get y velocity
        """
        return self._dy

    def loading(self):
        """
        put and remove the green rect on the window to simulate the loading animation.
        """
        self.window.add(self.label_load, x=100, y=200)
        for k in range(2):
            for j in range(7):
                pause(50)
                obj_b = self.window.get_object_at(x=272.5 - j * 20, y=230)
                if obj_b is not None:
                    self.window.remove(obj_b)
            for i in range(7):
                pause(60)
                self.battery = GRect(20, 25)
                self.battery.filled = True
                self.battery.fill_color = 'green'
                self.battery.color = 'white'
                self.window.add(self.battery, x=(self.window.width - self.battery.width * 7) / 2 + i * 20, y=230)

        pause(300)
        for j in range(7):
            pause(50)
            obj_b = self.window.get_object_at(x=272.5 - j * 20, y=230)
            self.window.remove(obj_b)
        self.window.remove(self.label_load)

from campy.gui.events.timer import pause

FRAME_RATE = 1000 / 200 # 120 frames per second
NUM_LIVES = 3			# Number of attempts

        
def main():
    graphics = BreakoutGraphics()
    graphics.set_num_lives(NUM_LIVES)

    # Add animation loop here!
    while True:
        graphics.ball_move()
        pause(FRAME_RATE)
        if graphics.if_game_end():
            break


if __name__ == '__main__':
    main()
