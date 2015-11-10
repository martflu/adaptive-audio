import player
import rectangle
import color
import random
import obstacle as obs
import particle
    
class scene:

    def __init__(self, graphic):
        self.player = player.player(graphic.res_x, graphic.res_y)
        self.obstacles = []
        self.particles = []
        self.res_x = graphic.res_x
        self.res_y = graphic.res_y
        self.playing_field_rect = rectangle.rectangle(0, 100, self.res_x, self.res_y - 100, color.color((0, 0, 0)))
        self.hud_background_rect = rectangle.rectangle(0, 0, graphic.res_x, graphic.res_y, color.color((100, 100, 100)))
        self.stats_background_rect = rectangle.rectangle(5, 5, graphic.res_x - 10, self.playing_field_rect.top() - 10, color.color((50, 50, 50)))
        self.color_bar_background_rect = rectangle.rectangle(self.stats_background_rect.left() + 5, self.stats_background_rect.top() + 5, self.stats_background_rect.right() - 15, self.stats_background_rect.bottom() - 15, color.color((0, 0, 0)))
        
    def new_trail_particle(self, x, y, color):
        w = self.player.rectangle.w
        h = self.player.rectangle.h
        self.particles.append(particle.particle(x, y, w, h, color))
        
    def new_obstacle(self):
        top = self.playing_field_rect.top()
        bottom = self.playing_field_rect.bottom()
        o_list = []
        g_list = []  
        diff = bottom - top
        for obstacle in self.obstacles:
            if obstacle.rectangle.left() <= self.res_x and obstacle.rectangle.right() >= self.res_x:
                o_list.append((obstacle.rectangle.top(), obstacle.rectangle.bottom()))
        o_list.sort()
        if len(o_list) != 0:
            g_list.append((o_list[0][0] - top, 0))
            g_list.append((bottom - o_list[len(o_list) - 1][1], len(g_list)))
            g_list.sort()
            if g_list[len(g_list) - 1][1] == 0:
                top = self.playing_field_rect.top()
                bottom = o_list[0][0]
            if g_list[len(g_list) - 1][1] == len(g_list) - 1:
                top = o_list[len(o_list) - 1][1]
                bottom = self.playing_field_rect.bottom()
        diff = bottom - top
        w = random.randint(40, 200)
        h = random.randint(diff / 10, diff)
        if h < 40:
            if diff >= 40:
                h = 40    
        if h > 200:
            h = 200
        x = self.res_x
        y_min = top
        y_max = bottom - h
        y = random.randint(y_min,  y_max)
        r = 0
        g = 0
        b = 0
        r = random.randint(10, 255)
        g = random.randint(10, 255)
        b = random.randint(10, 255)
        c = color.color((r, g, b))
        o = obs.obstacle(x, y, w, h, c)
        if h >= 40:
            self.obstacles.append(o)
        
    def negative(self):
        for obstacle in self.obstacles:
            obstacle.rectangle.c.negative()
            obstacle.n = (obstacle.n + 1)%2
            
    def collision_test(self, x1, y1, x2, y2, x3, y3, x4, y4):
        if x1 >= x4:
            return 0
        if x2 <= x3:
            return 0
        if y1 >= y4:
            return 0
        if y2 <= y3:
            return 0       
        return 1