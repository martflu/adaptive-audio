import sys
import color

class logic:
    
    def __init__(self):
        self.time = 0
        self.score = 0
        self.level = 1
        self.pause = 0
        self.hit = 0
    
    def exit_game(self, msg):
        print msg
        print "end of game"
        sys.exit()
    
    def update(self, input, delta, scene, sound):
        if (not self.pause):
            self.update_obstacles(scene, delta)
            self.update_player(scene, delta, input, sound)
            self.collision(scene, sound, delta)
            self.update_level(scene, delta, sound)
        self.update_particles(scene, delta)

    def update_obstacles(self, scene, delta):
        for obstacle in scene.obstacles:
            obstacle.rectangle.x = obstacle.rectangle.x - delta / 20
            if obstacle.rectangle.right() <=  0:
                scene.obstacles.remove(obstacle)
            if obstacle.rectangle.c.r < 10 and obstacle.rectangle.c.g < 10 and obstacle.rectangle.c.b < 10:
                scene.obstacles.remove(obstacle)       
                
    def update_player(self, scene, delta, input, sound):
        player = scene.player
        if input.up == 1:
            player.vector.y = -10
        elif input.down == 1:
            player.vector.y = 10
        else:
            player.vector.y = 0
        if input.left == 1:
            player.vector.x = -10
        elif input.right == 1:
            player.vector.x = 10
        else:
            player.vector.x = 0
        if player.vector.x != 0:
            player.rectangle.x = player.rectangle.x + player.vector.x * (delta / 47)
            if player.rectangle.left() < scene.playing_field_rect.left():
                player.rectangle.x = scene.playing_field_rect.left()
                player.vector.x = 0
            elif player.rectangle.right() > scene.playing_field_rect.right():
                player.rectangle.x = scene.playing_field_rect.right() - player.rectangle.w
                player.vector.x = 0
        if player.vector.y != 0:
            player.rectangle.y = player.rectangle.y + player.vector.y * (delta / 47)
            if player.rectangle.top() < scene.playing_field_rect.top():
                player.rectangle.y = scene.playing_field_rect.top()
                player.vector.y = 0
            elif player.rectangle.bottom() > scene.playing_field_rect.bottom():
                player.rectangle.y = scene.playing_field_rect.bottom() - player.rectangle.h
                player.vector.y = 0
        elif player.rectangle.c.get() == (255, 255, 255):
            self.score = 1
            self.pause = 1
            player.rectangle.c.set(20, 20, 20)
            scene.particles = []
                
    def update_particles(self, scene, delta):
        if self.time > 10:
            self.time = self.time - 10
            x = scene.player.rectangle.x
            y = scene.player.rectangle.y
            c = color.color(scene.player.rectangle.c.get())
            scene.new_trail_particle(x, y, c)
        for particle in scene.particles:
            particle.rectangle.x = particle.rectangle.x - delta / 20
            r = scene.player.rectangle.c.r
            g = scene.player.rectangle.c.g
            b = scene.player.rectangle.c.b
            amount = 4 * (delta / 20)
            if r >= g and r >= b:
                particle.rectangle.c.sg(amount)
                particle.rectangle.c.sb(amount)
                if particle.rectangle.c.g == 0 and particle.rectangle.c.b == 0:
                    particle.rectangle.c.sr(amount)
            if g >= r and g >= b:
                particle.rectangle.c.sr(amount)
                particle.rectangle.c.sb(amount)
                if particle.rectangle.c.r == 0 and particle.rectangle.c.b == 0:
                    particle.rectangle.c.sg(amount)
            if b >= r and b >= g:
                particle.rectangle.c.sr(amount)
                particle.rectangle.c.sg(amount)
                if particle.rectangle.c.r == 0 and particle.rectangle.c.g == 0:
                    particle.rectangle.c.sb(amount)
            if particle.rectangle.c.r == 0 and particle.rectangle.c.g == 0 and particle.rectangle.c.b == 0:
                scene.particles.remove(particle)
            elif particle.rectangle.x + particle.rectangle.w <= 0:
                scene.particles.remove(particle)
        if self.hit == 1:
            scene.particles = []   
            
    def collision(self, scene, sound, delta):
        self.hit = 0
        for obstacle in scene.obstacles:
            x1 = scene.player.rectangle.x
            x2 = scene.player.rectangle.x + scene.player.rectangle.w
            y1 = scene.player.rectangle.y 
            y2 = scene.player.rectangle.y + scene.player.rectangle.h
            x3 = obstacle.rectangle.x
            x4 = obstacle.rectangle.x + obstacle.rectangle.w
            y3 = obstacle.rectangle.y 
            y4 = obstacle.rectangle.y + obstacle.rectangle.h
            if scene.collision_test(x1, y1, x2, y2, x3, y3, x4, y4) == 1:
                r = obstacle.rectangle.c.r
                g = obstacle.rectangle.c.g
                b = obstacle.rectangle.c.b
                if obstacle.n == 0:
                    veryhigh = 0.1 * delta
                    high = 0.03 * delta
                    neutral = 0.01 * delta
                    low = 0.005 * delta
                    if r >= g and r >= b:
                        obstacle.rectangle.c.sr(veryhigh)
                        scene.player.rectangle.c.ar(high)
                        if g >= b:
                            obstacle.rectangle.c.sg(veryhigh)
                            scene.player.rectangle.c.ag(neutral)
                            obstacle.rectangle.c.sb(veryhigh)
                            scene.player.rectangle.c.ab(low)
                        else:
                            obstacle.rectangle.c.sb(veryhigh)
                            scene.player.rectangle.c.ab(neutral)
                            obstacle.rectangle.c.sg(veryhigh)
                            scene.player.rectangle.c.ag(low)
                    elif g >= r and g >= b:
                        obstacle.rectangle.c.sg(veryhigh)
                        scene.player.rectangle.c.ag(high)
                        if r >= b:
                            obstacle.rectangle.c.sr(veryhigh)
                            scene.player.rectangle.c.ar(neutral)
                            obstacle.rectangle.c.sb(veryhigh)
                            scene.player.rectangle.c.ab(low)
                        else:
                            obstacle.rectangle.c.sb(veryhigh)
                            scene.player.rectangle.c.ab(neutral)
                            obstacle.rectangle.c.sr(veryhigh)
                            scene.player.rectangle.c.ar(low)
                    elif b >= r and b >= g:
                        obstacle.rectangle.c.sb(veryhigh)
                        scene.player.rectangle.c.ab(high)
                        if r >= g:
                            obstacle.rectangle.c.sr(veryhigh)
                            scene.player.rectangle.c.ar(neutral)
                            obstacle.rectangle.c.sg(veryhigh)
                            scene.player.rectangle.c.ag(low)
                        else:
                            obstacle.rectangle.c.sg(veryhigh)
                            scene.player.rectangle.c.ag(neutral)
                            obstacle.rectangle.c.sr(veryhigh)
                            scene.player.rectangle.c.ar(low)
                elif obstacle.n == 1:
                    veryhigh = 0.1 * self.level * delta
                    high = 0.03 * self.level * delta
                    neutral = 0.01 * self.level * delta
                    low = 0.005 * self.level * delta
                    obstacle.rectangle.c.negative()
                    if r >= g and r >= b:
                        obstacle.rectangle.c.ar(veryhigh)
                        scene.player.rectangle.c.sr(high)
                        self.hit = 1
                        sound.state = 2
                        if g >= b:
                            obstacle.rectangle.c.ag(veryhigh)
                            scene.player.rectangle.c.sg(neutral)
                            obstacle.rectangle.c.ab(veryhigh)
                            scene.player.rectangle.c.sb(low)
                        else:
                            obstacle.rectangle.c.ab(veryhigh)
                            scene.player.rectangle.c.sb(neutral)
                            obstacle.rectangle.c.ag(veryhigh)
                            scene.player.rectangle.c.sg(low)
                    elif g >= r and g >= b:
                        obstacle.rectangle.c.ag(veryhigh)
                        scene.player.rectangle.c.sg(high)
                        self.hit = 1
                        sound.state = 3
                        if r >= b:
                            obstacle.rectangle.c.ar(veryhigh)
                            scene.player.rectangle.c.sr(neutral)
                            obstacle.rectangle.c.ab(veryhigh)
                            scene.player.rectangle.c.sb(low)
                        else:
                            obstacle.rectangle.c.ab(veryhigh)
                            scene.player.rectangle.c.sb(neutral)
                            obstacle.rectangle.c.ar(veryhigh)
                            scene.player.rectangle.c.sr(low)
                    elif b >= r and b >= g:
                        obstacle.rectangle.c.ab(veryhigh)
                        scene.player.rectangle.c.sb(high)
                        self.hit = 1
                        sound.state = 4
                        if r >= g:
                            obstacle.rectangle.c.ar(veryhigh)
                            scene.player.rectangle.c.sr(neutral)
                            obstacle.rectangle.c.ag(veryhigh)
                            scene.player.rectangle.c.sg(low)
                        else:
                            obstacle.rectangle.c.ag(veryhigh)
                            scene.player.rectangle.c.sg(neutral)
                            obstacle.rectangle.c.ar(veryhigh)
                            scene.player.rectangle.c.sr(low)
                    obstacle.rectangle.c.negative()

    def update_level(self, scene, delta, sound):
        if self.score == 1:
            sound.state = 5
            self.score = 0    