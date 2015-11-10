import pygame

class graphic:    
    res_x = 800
    res_y = 600

    def __init__(self):
        self.screen = pygame.display.set_mode((self.res_x, self.res_y))
        pygame.display.set_caption('adaptive audio')
        pygame.mouse.set_visible(False)
        self.level = 1
        
    def clear(self):
        c = (0, 0, 0)
        x = 0
        y = 0
        w = self.res_x
        h = self.res_y
        pygame.draw.rect(self.screen, c, (x, y, w, h))
        
    def draw_scene(self, scene, logic):
        self.clear()
        self.draw_hud(scene, logic)
        if logic.pause:
            self.draw_level_indicator(scene.playing_field_rect, logic)
        else:
            self.draw_obstacles(scene.playing_field_rect, scene.obstacles, scene, logic)
            self.draw_particles(scene.playing_field_rect, scene.particles)
            self.draw_player(scene, logic)
        
    def draw_hud(self, scene, logic):
        self.draw_hud_background(scene, logic)
        self.draw_playing_field(scene, logic)
        self.draw_stats_background(scene, logic)
        self.draw_color_status(scene.color_bar_background_rect, scene.player.rectangle.c, scene, logic)
        
    def draw_hud_background(self, scene, logic):
        rectangle = scene.hud_background_rect
        c = rectangle.c.get()
        if logic.hit == 1:
            rectangle.c.negative()
            c = rectangle.c.get()
            rectangle.c.negative()
        x = rectangle.x
        y = rectangle.y
        w = rectangle.w
        h = rectangle.h
        pygame.draw.rect(self.screen, c, (x, y, w, h))
        
    def draw_playing_field(self, scene, logic):
        rectangle = scene.playing_field_rect
        c = rectangle.c.get()
        if logic.hit == 1:
            rectangle.c.negative()
            c = rectangle.c.get()
            rectangle.c.negative()
        x = rectangle.x
        y = rectangle.y
        w = rectangle.w
        h = rectangle.h
        pygame.draw.rect(self.screen, c, (x, y, w, h))
        
    def draw_stats_background(self, scene, logic):
        rectangle = scene.stats_background_rect
        c = rectangle.c.get()
        if logic.hit == 1:
            rectangle.c.negative()
            c = rectangle.c.get()
            rectangle.c.negative()
        x = rectangle.x
        y = rectangle.y
        w = rectangle.w
        h = rectangle.h
        pygame.draw.rect(self.screen, c, (x, y, w, h))
        
    def draw_player(self, scene, logic):
        player = scene.player
        px = player.rectangle.x
        py = player.rectangle.y
        pw = player.rectangle.w
        ph = player.rectangle.h
        c = (255, 255, 255)
        if logic.hit == 1:
            c = (0, 0, 0)
        pygame.draw.rect(self.screen, c, (px, py, pw, ph))
        px = px + 1
        py = py + 1
        pw = pw - 2
        ph = ph - 2
        c = player.rectangle.c.get()
        if logic.hit == 1:
            player.rectangle.c.negative()
            c = player.rectangle.c.get()
            player.rectangle.c.negative()
        pygame.draw.rect(self.screen, c, (px, py, pw, ph))

    def draw_particles(self, rectangle, particles):
        for particle in particles:
            x = particle.rectangle.x
            y = particle.rectangle.y
            w = particle.rectangle.w
            h = particle.rectangle.h
            c = particle.rectangle.c.get()
            pygame.draw.rect(self.screen, c, (x, y, w, h)) 
    
    def draw_obstacles(self, rectangle, obstacles, scene, logic):
        for obstacle in obstacles:
            ox = obstacle.rectangle.x
            oy = obstacle.rectangle.y
            ow = obstacle.rectangle.w
            oh = obstacle.rectangle.h
            if obstacle.n == 1:
                c = (255, 255, 255)
                if logic.hit == 1:
                    c = (0, 0, 0)
                pygame.draw.rect(self.screen, c, (ox, oy, ow, oh))
                ox = ox + 1
                oy = oy + 1 
                ow = ow - 2
                oh = oh - 2
                c = (0, 0, 0)
                if logic.hit == 1:
                    c = (255, 255, 255)
                pygame.draw.rect(self.screen, c, (ox, oy, ow, oh))
                ox = ox + 1
                oy = oy + 1 
                ow = ow - 2
                oh = oh - 2
            c = obstacle.rectangle.c.get()
            if logic.hit == 1:
                obstacle.rectangle.c.negative()
                c = obstacle.rectangle.c.get()
                obstacle.rectangle.c.negative()
            pygame.draw.rect(self.screen, c, (ox, oy, ow, oh))
        
    def draw_color_status(self, rectangle, c, scene, logic):
        backround_color = rectangle.c.get()
        if logic.hit == 1:
            rectangle.c.negative()
            backround_color = rectangle.c.get()
            rectangle.c.negative()
        x = rectangle.x
        y = rectangle.y
        w = rectangle.w  
        h = rectangle.h
        pygame.draw.rect(self.screen, backround_color, (x, y, w, h))
        h = h / 3
        l = w
        unit = float(l) / 255
        rl = c.r * unit
        gl = c.g * unit
        bl = c.b * unit
        color = (255, 0, 0)
        if logic.hit == 1:
            color = (0, 255, 255)
        w = rl
        pygame.draw.rect(self.screen, color, (x, y, w, h))
        color = (0, 255, 0)
        if logic.hit == 1:
            color = (255, 0, 255)
        y = y + h + 1
        w = gl
        pygame.draw.rect(self.screen, color, (x, y, w, h))
        color = (0, 0, 255)
        if logic.hit == 1:
            color = (255, 255, 0)
        y = y + h + 1
        w = bl
        pygame.draw.rect(self.screen, color, (x, y, w, h))        
        
    def draw_level_indicator(self, rect, logic):
        self.clear()
        t = logic.time / 3
        if t >= 255:
            logic.time = 0
            t = 0
        c = (t, t, t)
        if self.level == 1:
            c = (t, 10, 10)
        elif self.level == 2:
            c = (10, t, 10)
        elif self.level == 3:
            c = (10, 10, t)
        elif self.level == 4:
            c = (t, 255 - t, 255 - t)
        elif self.level == 5:
            c = (255 - t, t, 255 - t)
        elif self.level == 6:
            c = (255 - t, 255 - t, t)
        level = self.level + 1
        font = pygame.font.Font(None, 100)
        text = font.render("LEVEL " + str(level), 1, c)
        textpos = text.get_rect(centerx=self.screen.get_width()/2)
        textpos.y = rect.y + rect.h / 2
        self.screen.blit(text, textpos)