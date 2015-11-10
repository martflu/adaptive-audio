import pygame
import input
import logic
import graphic
import sound
import scene

print "starting up adaptive audio"
pygame.init()
clock = pygame.time.Clock()
input = input.input()
logic = logic.logic()
graphic = graphic.graphic()
sound = sound.sound()
sound.init_available_sounds()
scene = scene.scene(graphic)
clock.tick()

while True:    
    delta = float(clock.tick())
    logic.time = logic.time + delta
    input.update(logic, scene)
    logic.update(input, delta, scene, sound)
    graphic.draw_scene(scene, logic)
    sound.update(scene, logic, input, graphic)
    pygame.display.flip()