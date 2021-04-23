"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

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
