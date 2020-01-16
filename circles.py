import pygame
from pygame.locals import *

from math import *

from die import *

from OpenGL.GL import *
from OpenGL.GLU import *


class Circles:
    def __init__(self, posx, posy, face):
        self.posx = posx
        self.posy = posy
        self.face = face

    def draw(self, number):
        sides = 100
        radius = 0.20
        glPushMatrix()
        if number == 1:
            glTranslatef(-2, 0, 0)
        else:
            glTranslatef(2, 0, 0)
        face_placing(self.face)
        glBegin(GL_TRIANGLE_FAN)
        for i in range(sides):
            cosine = radius * cos(i*2*pi/sides)
            sine = radius * sin(i*2*pi/sides)
            glVertex3f(cosine + self.posx, sine + self.posy, 1.05)
            glColor3fv(colors_black[0])
        glEnd()
        glPopMatrix()


def face_placing(face):
    if face == 'av': #face avant
        pass
    elif face == 'ar': #face arriere
        glRotate(180, 1, 0, 0)
    elif face == 'ha': #face haut
        glRotate(270, 1, 0, 0)
    elif face == 'ba': #face bas
        glRotate(90, 1, 0, 0)
    elif face == 'ga': #face gauche
        glRotate(270, 0, 1, 0)
    elif face == 'dr': #face droite
        glRotate(90, 0, 1, 0)




colors_black = (
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        )
