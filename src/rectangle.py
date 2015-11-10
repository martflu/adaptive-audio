class rectangle:
    
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = color
        
    def top(self):
        return self.y

    def bottom(self):
        return self.y + self.h

    def left(self):
        return self.x

    def right(self):
        return self.x + self.w