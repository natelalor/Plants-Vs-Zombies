


class Square:
    '''
    Facilitates organizational structure of playing field. A list of lists of square objects.
        __init__: (constructor) defines size of squares (one parameter, because always will be square.),
                  and passes in coordinates x,y to a new list that will be referenced when square position is needed.
        getPosition: returns list of x,y coordinates
    '''
    def __init__(self, size, x, y):
        self.size_x = size
        self.size_y = size
        self.position_list = [x, y]

    def getPosition(self):
        return self.position_list

