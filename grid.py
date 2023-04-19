import arcade
from square import Square


class Grid:
    '''
    Facilitates organizational structure of playing field. A list of lists of square objects.
        __init__: defines size of grid with x & y (dimensions are not square).
                  Also creates the grid (grid_list) and populates it with squares using the given dimensions.
    '''
    def __init__(self, size_columns, size_rows):
        self.size_columns = size_columns
        self.size_rows = size_rows





        # grid_list will be the list of lists that make up the grid
        self.grid_list = []


        for x in range(0, size_rows):
            temp_list = []
            for y in range(0, size_columns):
                # x & y is the position in the grid to keep track of each square object's position
                temp_list.append(Square(x, y))
            self.grid_list.append(temp_list)

    def grid_draw(self):

        for row in range(self.size_rows):
            for column in range(self.size_columns):
                # Messing with lawn-like color patterns for the grid
                if row % 2 == 0:
                    color = (155, 245, 66, 100)
                    if column % 2 != 0:
                        color = (197, 245, 66, 100)

                elif column % 2 == 0:
                    color = (218, 245, 66, 100)
                else:
                    color = (56, 161, 3, 100)


                # The math to make evenly sized/spaced squares
                x = (5 + 100) * column + 5 + 100 // 2
                y = (5+ 100) * row + 5 + 100 // 2

                # Draw the box
                arcade.draw_rectangle_outline(x, y, 100, 100, color)




