import pygame
from pygame.locals import *

from math import *

from OpenGL.GL import *
from OpenGL.GLU import *

from circles import *

faces_one = [
    [1, 6],
    [5, 2],
    [4, 3],
    ]

faces_two = [
    [1, 6],
    [5, 2],
    [4, 3],
    ]

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
        if number == 1:
            faces = faces_one
        elif number == 2:
            faces = faces_two
        sides = (
                [Circles(0, 0, 1, faces)],
                [Circles(-0.5, 0.5, 2, faces), Circles(0.5, -0.5, 2, faces)],
                [Circles(-0.5, 0.5, 3, faces), Circles(0.5, -0.5, 3, faces),
                    Circles(0, 0, 3, faces)],
                [Circles(-0.5, -0.5, 4, faces), Circles(0.5, 0.5, 4, faces),
                    Circles(-0.5, 0.5, 4, faces), Circles(0.5, -0.5, 4, faces)],
                [Circles(-0.5, -0.5, 5, faces), Circles(0.5, 0.5, 5, faces),
                    Circles(-0.5, 0.5, 5, faces), Circles(0.5, -0.5, 5, faces),
                    Circles(0, 0, 5, faces)],
                [Circles(-0.5, -0.5, 6, faces), Circles(0.5, 0.5, 6, faces),
                    Circles(-0.5, 0.5, 6, faces), Circles(0.5, -0.5, 6, faces),
                    Circles(-0.5, 0, 6, faces), Circles(0.5, 0, 6, faces)],
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

def swap(f, n, direction):
    if n == 1:
        faces_one[f][0], faces_one[f][1] = faces_one[f][1], faces_one[f][0]
        if direction == 'y':
            faces_one[0], faces_one[1] = faces_one[1], faces_one[0]
        elif direction == 'x':
            faces_one[0], faces_one[2] = faces_one[2], faces_one[0]
        return faces_one[0][0]
    elif n == 2:
        faces_two[f][0], faces_two[f][1] = faces_two[f][1], faces_two[f][0]
        if direction == 'y':
            faces_two[0], faces_two[1] = faces_two[1], faces_two[0]
        elif direction == 'x':
            faces_two[0], faces_two[2] = faces_two[2], faces_two[0]
        return faces_two[0][0]

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
