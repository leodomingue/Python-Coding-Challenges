class Cell:

    def __init__(self, x, y):
        self.position_x = x
        self.position_y = y


    def is_passable(self): 
        raise NotImplementedError("Should be Implemented")
    
    def is_wall(self):
        return False
    
    def is_path(self):
        return False
    
    def is_position(self, x, y):
        return (self.position_x == x and self.position_y == y)
    

class WallCell(Cell):
     
    def __init__(self,x,y):
        super().__init__(x, y)

    def is_passable(self): 
        return False
    
    def is_wall(self):
        return True


class PathCell(Cell):
    def __init__(self,x,y):
        super().__init__(x, y)
        self.visited = False

    def is_passable(self): 
        return True
    
    def is_path(self):
        return True
    
    def was_visited(self):
        return self.visited
    
    def is_visit(self):
        self.visited = True
    

class PlayerCell(Cell):
    def __init__(self,x,y):
        super().__init__(x, y)

    def is_passable(self): 
        return False
    
    def movement_up(self):
        self.position_y = self.position_y -1

    def movement_down(self):
        self.position_y = self.position_y +1

    def movement_right(self):
        self.position_x = self.position_x +1

    def movement_left(self):
        self.position_x = self.position_x - 1
    

    
