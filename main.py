import pygame
import os
import time

from do import do
from gui import GUI

from renderers import *

gui = GUI(500,500,'CivClone')
done = False
images = {}

for f in os.listdir('assets/images'):
  if f[-4:] == '.png':
    print('Loading asset ' + f)
    images[f[0:-4]] = pygame.image.load('assets/images/' + f)

keys = []
mouse_presses = (0, 0, 0)

title = TitleScreen(gui, images)

render_sequence = [title]

while not done:
  for e in gui.event():
    if e.type == pygame.QUIT:
      done = True
      break
    if e.type == pygame.KEYUP:
      for i in render_sequence:
        i.key_hit(keys)

    if e.type == pygame.VIDEORESIZE:
      gui.resize(e.dict['size'][0],e.dict['size'][1])

  keys = gui.keysDown()

  do(gui)

  if gui.mouseAction() != mouse_presses:
    for button in range(3):
      if gui.mouseAction()[button]:
        if mouse_presses[button]:
          continue
        action = 'mouse{}'.format(button), 'down'

      elif mouse_presses[button]:
        action = 'mouse{}'.format(button), 'up'

    mouse_presses = gui.mouseAction()
    for i in render_sequence:
      i.click(action)

  for i in render_sequence:
    i.setCursorPos(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

  if gui.keysDown(pygame.K_ESCAPE):
    done = True

  for i in render_sequence:
    i.render()

  gui.flip(120)
