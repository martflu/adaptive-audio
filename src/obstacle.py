import rectangle
class obstacle:
    
    def __init__(self, x, y, w, h, c):
        self.rectangle = rectangle.rectangle(x, y, w, h, c)
        self.n = 0
