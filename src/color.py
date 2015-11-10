class color:
    
    def __init__(self, (r, g, b)):
        self.r = r
        self.g = g
        self.b = b
    
    def ar(self, value):
        self.r = self.r + value
        if self.r > 255:
            self.r = 255
        
    def ag(self, value):
        self.g = self.g + value
        if self.g > 255:
            self.g = 255
        
    def ab(self, value):
        self.b = self.b + value
        if self.b > 255:
            self.b = 255
    
    def sr(self, value):
        self.r = self.r - value
        if self.r < 0:
            self.r = 0
        
    def sg(self, value):
        self.g = self.g - value
        if self.g < 0:
            self.g = 0
        
    def sb(self, value):
        self.b = self.b - value
        if self.b < 0:
            self.b = 0
    
    def negative(self):
        self.r = 255 - self.r
        self.g = 255 - self.g
        self.b = 255 - self.b
    
    def set(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        
    def get(self):
        return (self.r, self.g, self.b)