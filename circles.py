import pygame
from pygame.locals import *

from math import *

from die import *

from OpenGL.GL import *
from OpenGL.GLU import *


class Circles:
    def __init__(self, posx, posy, face, faces):
        self.posx = posx
        self.posy = posy
        self.face = face
        self.faces = faces

    def draw(self, number):
        sides = 100
        radius = 0.20
        glPushMatrix()
        if number == 1:
            glTranslatef(-2, 0, 0)
        else:
            glTranslatef(2, 0, 0)
        face_placing(self.face, self.faces)
        glBegin(GL_TRIANGLE_FAN)
        for i in range(sides):
            cosine = radius * cos(i*2*pi/sides)
            sine = radius * sin(i*2*pi/sides)
            glVertex3f(cosine + self.posx, sine + self.posy, 1.05)
            glColor3fv(colors_black[0])
        glEnd()
        glPopMatrix()


def face_placing(face, faces):
    for i in range(len(faces)):
        for j in range(len(faces[i])):
            if faces[i][j] == face:
                if i == 0 and j == 0: #face avant
                    pass
                elif i == 0 and j == 1: #face arriere
                    glRotate(180, 1, 0, 0)
                elif i == 1 and j == 0: #face haut
                    glRotate(270, 1, 0, 0)
                elif i == 1 and j == 1: #face bas
                    glRotate(90, 1, 0, 0)
                elif i == 2 and j == 0: #face gauche
                    glRotate(270, 0, 1, 0)
                elif i == 2 and j == 1: #face droite
                    glRotate(90, 0, 1, 0)
                return




colors_black = (
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        )
