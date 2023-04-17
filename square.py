
import constants as c

class Square:
    """
    An object that will make up the grid, and be able to contain a defender.
    The basic unit of measurement for our game.
        __init__: (constructor) defines size of square (using constant),
                  and passes in coordinates x,y to a list that will be referenced when square position is needed.
        get_position: returns list of x,y coordinates
        has_plant: returns whether hasPlant is true/false.
                  Indicates whether the square is already holding a defender.
        add_plant: changes bool "has_plant" to true
        remove_plant: changes bool "has_plant" to false
    """
    def __init__(self, x, y):
        self.size = c.SQUARE_SIZE
        self.position_list = [x, y]
        self.has_plant = False

        self.abs_coords = [0,0]

    def get_position(self):
        return self.position_list

    def has_plant(self, x, y):
        # if square at x, y has a plant:
        return True
        # else
        # return False

    def add_plant(self):
        self.has_plant = True

    def remove_plant(self):
        self.has_plant = False


    def set_coords(self,x,y):
        if self.abs_coords == [0,0]:
            self.abs_coords = [x,y]
        else:
            pass

    def get_abs_coords(self):
        return self.abs_coords
    
    #checks whether click is in the square
    def in_square(self,x,y):
        square_x = self.abs_coords[0] 
        square_y = self.abs_coords[1]
        if (square_x-50 <= x <= square_x+50) and (square_y - 50 <= y <= square_y + 50):
            
            return True
            
        return False