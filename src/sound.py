import pygame
import os
import random

class sound:
    
    def __init__(self):
        self.level = 1
        self.sound_level = 1
        self.state = 0
        self.laststate = 0
        self.available_sounds = {}
        self.sounds = {}
        self.music_channel = pygame.mixer.Channel(0)
        
    def update(self, scene, logic, input, graphic):
        self.level = self.get_sound_level(logic.level)
        if self.music_channel.get_queue() == None:
            self.laststate = self.state
            self.queue()
            if self.state == 0:
                self.state = 1
                scene.__init__(graphic)
            elif self.state == 2:
                self.state = 1
            elif self.state == 3:
                self.state = 1
            elif self.state == 4:
                self.state = 1
            elif self.state == 5:
                self.state = 0
                logic.level = logic.level + 1
            else:
                if logic.level != graphic.level:
                    graphic.level = logic.level
            if self.laststate == 0:
                scene.negative()
                scene.new_obstacle()
            elif self.laststate == 1:
                scene.negative()
                scene.new_obstacle()
                logic.pause = 0
            elif self.laststate == 2:
                scene.negative()
                scene.new_obstacle()
                scene.negative()
                scene.new_obstacle()
                scene.negative()
            elif self.laststate == 3:
                scene.new_obstacle()
                scene.negative()
                scene.new_obstacle()
                scene.negative()
                scene.new_obstacle()
                scene.negative()
            elif self.laststate == 4:
                scene.negative()
                scene.new_obstacle()
                scene.negative()
                scene.new_obstacle()
                scene.negative()
                scene.new_obstacle()
                scene.negative()
                scene.new_obstacle()
                scene.negative()
                    
    def queue(self):
        self.new_sample()
        self.music_channel.queue(self.sounds[self.sample])
        
    def init_available_sounds(self):
        self.available_sounds["00"] = 9
        self.available_sounds["01"] = 5
        self.available_sounds["02"] = 7
        self.available_sounds["03"] = 0
        self.available_sounds["04"] = 10
        self.available_sounds["05"] = 8
        self.available_sounds["10"] = 4
        self.available_sounds["11"] = 5
        self.available_sounds["12"] = 5
        self.available_sounds["13"] = 7
        self.available_sounds["14"] = 1
        self.available_sounds["15"] = 2
        self.available_sounds["30"] = 2
        self.available_sounds["31"] = 7
        self.available_sounds["32"] = 6
        self.available_sounds["33"] = 0
        self.available_sounds["34"] = 4
        self.available_sounds["35"] = 3
        self.available_sounds["40"] = 1
        self.available_sounds["41"] = 4
        self.available_sounds["42"] = 3
        self.available_sounds["43"] = 3
        self.available_sounds["44"] = 2
        self.available_sounds["45"] = 2
        self.available_sounds["50"] = 5
        self.available_sounds["51"] = 7
        self.available_sounds["52"] = 7
        self.available_sounds["53"] = 5
        self.available_sounds["54"] = 10
        self.available_sounds["55"] = 2
        self.available_sounds["60"] = 1
        self.available_sounds["61"] = 4
        self.available_sounds["62"] = 4
        self.available_sounds["63"] = 0
        self.available_sounds["64"] = 3
        self.available_sounds["65"] = 1
        for dir, subdir, files in os.walk("media"):
            for file in files:
                path = os.path.join(dir, file)
                self.sounds[file] = pygame.mixer.Sound(os.path.join(dir, file))
                
    def get_sound_level(self, logic_level):
        if logic_level == 1:
            return 1
        elif logic_level == 2:
            return 0
        elif logic_level == 3:
            return 4
        elif logic_level == 4:
            return 6
        elif logic_level == 5:
            return 5
        elif logic_level == 6:
            return 3
        else:
            return 3
        
    def new_sample(self):
        level = 100 * self.level
        state = 10 * self.state
        range = self.available_sounds[str(self.level)+str(self.state)]
        if range == 0:
            self.state = 1
            state = 10 * self.state
            range = self.available_sounds[str(self.level)+str(self.state)]
        number = random.randint(0, range - 1)
        self.sample = str(level + state + number) + ".wav"        