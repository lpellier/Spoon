import pygame
import random

from pygame.locals import *
from math import *

from die import *
from circles import *

from OpenGL.GL import *
from OpenGL.GLU import *

def which_to_rotate(die, number, angle, d_coord):
    x = d_coord[0]
    y = d_coord[1]
    z = d_coord[2]
    if number == 1:
        glTranslatef(-2, 0, 0)
        glRotatef(angle, x, y, z)
        glTranslatef(2, 0, 0)
        die.draw(number)
    elif number == 2:
        glTranslatef(2, 0, 0)
        glRotatef(angle, -x, y, z)
        glTranslatef(-2, 0, 0)
        die.draw(number)

def rotate_die(die, number, angle, rand):
    glPushMatrix()
    if rand == 1: #avant
        which_to_rotate(die, number, angle, (-1, 0, 0))
    elif rand == 2: #gauche
        which_to_rotate(die, number, angle, (0, -1, 0))
    elif rand == 3: #droite
        which_to_rotate(die, number, angle, (0, 1, 0))
    elif rand == 4: #arriere
        which_to_rotate(die, number, angle, (1, 0, 0))
    glPopMatrix()

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                return

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    angle = 0
    plus = 1
    die_one, die_two = Die(1), Die(2)
    done_coord = (1, 0, 0)
    dtwo_coord = (1, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                wait()
            '''
            if event.key == K_w:
                wait()
                done_coord = (-1, 0, 0)
            elif event.key == K_a:
                wait()
                done_coord = (0, -1, 0)
            elif event.key == K_d:
                wait()
                done_coord = (0, 1, 0)
            elif event.key == K_s:
                wait()
                done_coord = (1, 0, 0)
                #dtwo_coord = (1, 0, 0)
                #plus = 100
            '''

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if angle == 0 or angle == 90:
            angle = 0
            rand = random.randint(1, 4)
        if angle > 90:
            angle = 0
        angle += plus
        rotate_die(die_one, 1, angle, rand)
        #rotate_die(die_two, 2, angle, dtwo_coord)
        pygame.display.flip()
        pygame.time.wait(1)

main()
