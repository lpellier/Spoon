import pygame
from pygame.locals import *

from math import *

from OpenGL.GL import *
from OpenGL.GLU import *

from circles import *


class Die:
    def __init__(self,  number):
        self.number = number
        self.vertices = get_vertices(self.number)

    def draw(self, number):
        glBegin(GL_QUADS)
        for surface in surfaces:
            x = 0
            for vertex in surface:
                x += 1
                glColor3fv(colors[x])
                glVertex3fv(self.vertices[vertex])
        glEnd()
        glBegin(GL_LINES)
        for edge in edges:
            x = 0
            for vertex in edge:
                x += 1
                glColor3fv(colors_black[x])
                glVertex3fv(self.vertices[vertex])
        glEnd()
        face_un, face_de, face_tr = 1, 2, 3
        face_qu, face_ci, face_si = -3, -2, -1
        sides = (
                [Circles(0, 0, face_un)],
                [Circles(-0.5, 0.5, face_de), Circles(0.5, -0.5, face_de)],
                [Circles(-0.5, 0.5, face_tr), Circles(0.5, -0.5, face_tr),
                    Circles(0, 0, face_tr)],
                [Circles(-0.5, -0.5, face_qu), Circles(0.5, 0.5, face_qu),
                    Circles(-0.5, 0.5, face_qu), Circles(0.5, -0.5, face_qu)],
                [Circles(-0.5, -0.5, face_ci), Circles(0.5, 0.5, face_ci),
                    Circles(-0.5, 0.5, face_ci), Circles(0.5, -0.5, face_ci),
                    Circles(0, 0, face_ci)],
                [Circles(-0.5, -0.5, face_si), Circles(0.5, 0.5, face_si),
                    Circles(-0.5, 0.5, face_si), Circles(0.5, -0.5, face_si),
                    Circles(-0.5, 0, face_si), Circles(0.5, 0, face_si)],
                )
        for side in sides:
            for circle in range(len(side)):
                side[circle].draw(number)


def get_vertices(number):
    if number == 1:
        vertices = (
                (-1, -1, -1),
                (-1, 1, -1),
                (-3, 1, -1),
                (-3, -1, -1),
                (-1, -1, 1),
                (-1, 1, 1),
                (-3, -1, 1),
                (-3, 1, 1),
                )
    elif number == 2:
        vertices = (
                (3, -1, -1),
                (3, 1, -1),
                (1, 1, -1),
                (1, -1, -1),
                (3, -1, 1),
                (3, 1, 1),
                (1, -1, 1),
                (1, 1, 1),
                )
    return vertices


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
        )

surfaces = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6),
        )
