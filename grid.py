
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

        # size will be the side length of the square
        square_length = 1

        # grid_list will be the list of lists that make up the grid
        grid_list = []

        for x in range(0, size_columns):
            temp_list = []
            for y in range(0, size_rows):
                # x & y is the position in the grid to keep track of each square object's position
                temp_list.append(Square(square_length, x, y))
            grid_list.append(temp_list)


