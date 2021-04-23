"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui
import os

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    space = (width-GRAPH_MARGIN_SIZE*2)/len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * space
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE)
    # top line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # color = None
    color_index = 0
    count = -1         # for loop round count to decide when to reset the loop
    xy_lst = []        # list to store x_coordinate and y_coordinate of each point
    for name in lookup_names:

        # define the color of the line
        color = COLORS[color_index % len(YEARS)-1]
        color_index += 1

        # check whether input name is in name_data dict
        if name in name_data:
            # check whether the rank of each year is within 1000
            for year in YEARS:
                count += 1
                x1 = get_x_coordinate(CANVAS_WIDTH, count)
                year = str(year)

                # rank below 1000
                if year in name_data[name]:
                    y1 = GRAPH_MARGIN_SIZE+((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK * int(name_data[name][year]))
                    canvas.create_text(x1 + TEXT_DX, y1,
                                       text=(name, name_data[name][year]), anchor=tkinter.SW, fill=color)
                # rank over 1000
                else:
                    y1 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                    canvas.create_text(x1 + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       text=(name, '*'), anchor=tkinter.SW, fill=color)

                # store all coordinate of all the points in the list
                xy_lst.append((x1, y1))

                # reset the loop to store data for next name in lookup_names
                if count == len(YEARS)-1:
                    count = -1

        # connect all the dots with lines
        for i in range(len(xy_lst)-1):
            canvas.create_line(xy_lst[i][0], xy_lst[i][1], xy_lst[i + 1][0], xy_lst[i + 1][1], width=LINE_WIDTH, fill=color)
        xy_lst = []


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()

# def main():
#     # Load data
#     # dir = r'C:\Users\tyw46\Desktop\SC101\Assignment\SC101_Assignment4_翁庭玉\SC101_Assignment4\data\full'
#     # filenames = []
#     # for filename in os.listdir(dir):
#     #     filenames.append(os.path.join(dir, filename))
#
#     name_data = babynames.read_files(filenames)
#
#     # Create the window and the canvas
#     top = tkinter.Tk()
#     top.wm_title('Baby Names')
#     canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)
#
#     # Call draw_fixed_lines() once at startup so we have the lines
#     # even before the user types anything.
#     draw_fixed_lines(canvas)
#
#     # This line starts the graphical loop that is responsible for
#     # processing user interactions and plotting data
#     top.mainloop()

if __name__ == '__main__':
    main()
