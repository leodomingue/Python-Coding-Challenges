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
    
    def get_color(self):
        raise NotImplementedError("Should be Implemented")
    

class WallCell(Cell):
     
    def __init__(self,x,y):
        super().__init__(x, y)
        self.color = (0, 0, 0)

    def is_passable(self): 
        return False
    
    def is_wall(self):
        return True
    
    def get_color(self):
        return self.color


class PathCell(Cell):
    def __init__(self,x,y):
        super().__init__(x, y)
        self.visited = False
        self.color_normal = (255, 255, 255)
        self.color_visited = (136,231,136)

    def is_passable(self): 
        return True
    
    def is_path(self):
        return True
    
    def was_visited(self):
        return self.visited
    
    def is_visit(self):
        self.visited = True

    def is_unvisit(self):
        self.visited = False

    def get_color(self):
        if self.was_visited():
            return self.color_visited
        return self.color_normal
    

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
    

    
