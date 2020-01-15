import pygame
from pygame.locals import *

from math import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Circles():
    def __init__(self, posx, posy, number):
        self.posx = posx
        self.posy = posy
        self.number = number

    def draw(self):
        sides = 100
        radius = 0.20
        glPushMatrix()
        rotate(self.number)
        glBegin(GL_TRIANGLE_FAN)
        for i in range(sides):
            cosine = radius * cos(i*2*pi/sides)
            sine = radius * sin(i*2*pi/sides)
            glVertex3f(cosine + self.posx, sine + self.posy, 1.01)
            glColor3fv(colors_black[0])
        glEnd()
        glPopMatrix()

def rotate(number):
    if number == 1:
        pass
    elif number == 2:
        glRotate(90, 1, 0, 0)
    elif number == 3:
        glRotate(90, 0, 1, 0)
    elif number == 4:
        glRotate(270, 0, 1, 0)
    elif number == 5:
        glRotate(270, 1, 0, 0)
    elif number == 6:
        glRotate(180, 1, 0, 0)

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    )

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
    )

colors = (
    (1, 1, 1),
    (1, 1, 1),
    (1, 1, 1),
    (1, 1, 1),
    (1, 1, 1),
    )

colors_black = (
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    )

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),
    )

def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        x = 0
        for vertex in edge:
            x += 1
            glColor3fv(colors_black[x])
            glVertex3fv(vertices[vertex])
    glEnd()
    sides = (
        [Circles(0, 0, 1)],
        [Circles(-0.5, 0.5, 2), Circles(0.5, -0.5, 2)],
        [Circles(-0.5, 0.5, 3), Circles(0.5, -0.5, 3), 
        Circles(0, 0, 3)],
        [Circles(-0.5, -0.5, 4), Circles(0.5, 0.5, 4),
        Circles(-0.5, 0.5, 4), Circles(0.5, -0.5, 4)],
        [Circles(-0.5, -0.5, 5), Circles(0.5, 0.5, 5),
        Circles(-0.5, 0.5, 5), Circles(0.5, -0.5, 5),
        Circles(0, 0, 5)],
        [Circles(-0.5, -0.5, 6), Circles(0.5, 0.5, 6),
        Circles(-0.5, 0.5, 6), Circles(0.5, -0.5, 6),
        Circles(-0.5, 0, 6), Circles(0.5, 0, 6)],
    )
    for side in sides:
        k = 0
        for die in side:
            side[k].draw()
            k += 1

def main():
    pygame.init()
    display = (800, 600)
    
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(5, 2, 1, 1)
        Cube()
        pygame.display.flip()
        pygame.time.wait(1)

main()
