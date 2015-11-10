class vector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def ax(self, value):
        self.x = self.x + value
        if self.x > 10:
            self.x = 10
            
    def ay(self, value):
        self.y = self.y + value
        if self.x > 20:
            self.x = 20
            
    def sx(self, value):
        self.x = self.x - value
        if self.x < -10:
            self.x = -10
            
    def sy(self, value):
        self.y = self.y - value
        if self.x < -20:
            self.x = -20