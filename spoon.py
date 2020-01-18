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
        glRotatef(angle, x, y, z)
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
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                else:
                    return

def stats(output_list):
    count_1, count_2, count_3, count_4, count_5, count_6 = 0, 0, 0, 0, 0, 0
    for i in output_list:
        if i == 1:
            count_1 += 1
        elif i == 2:
            count_2 += 1
        elif i == 3:
            count_3 += 1
        elif i == 4:
            count_4 += 1
        elif i == 5:
            count_5 += 1
        elif i == 6:
            count_6 += 1
    longe = len(output_list)
    print(f"1 = {count_1}/{longe}\n2 = {count_2}/{longe}\n3 = {count_3}/{longe}\n4 = {count_4}/{longe}\n5 = {count_5}/{longe}\n6 = {count_6}/{longe}")

def main():
    pygame.init()
    display = (1920, 1080)
    pygame.display.set_mode(display, RESIZABLE | DOUBLEBUF | OPENGL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    output_list = []
    angle = 0
    plus = 22.5
    die_one, die_two = Die(1), Die(2)
    done_coord = (1, 0, 0)
    dtwo_coord = (1, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                stats(output_list)
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                while angle != 90:
                    if event.type == pygame.QUIT:
                        pygame.quit() 
                        quit()
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            quit()
                    angle+=plus
                    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                    rotate_die(die_one, 1, angle, rand_one)
                    rotate_die(die_two, 2, angle, rand_two)
                    pygame.display.flip()
                    pygame.time.wait(1)
                output_list.append(front_one)
                output_list.append(front_two)
                wait()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if angle == 0 or angle == 90:
            if angle == 90:
                front_one = rand_happen(rand_one, 1)
                front_two = rand_happen(rand_two, 2)
            angle = 0
            rand_one = random.randint(1, 4)
            rand_two = random.randint(1, 4)
        if angle > 90:
            angle = 0
        angle += plus
        rotate_die(die_one, 1, angle, rand_one)
        rotate_die(die_two, 2, angle, rand_two)
        pygame.display.flip()
        pygame.time.wait(1)

def rand_happen(rand, number):
    if rand == 1:
        return swap(1, number, 'y')
    elif rand == 2:
        return swap(2, number, 'x')
    elif rand == 3:
        return swap(0, number, 'x')
    elif rand == 4:
        return swap(0, number, 'y')

main()
