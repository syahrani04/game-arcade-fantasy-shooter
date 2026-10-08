from circle import MidpointCircle
from line import MidpointLine
from OpenGL.GL import *
import random
import math
from math import cos, sin, pi

WINDOW_X = 800
WINDOW_Y = 600

class Star:
    def __init__(self, x, num):
        self.star_color = (random.uniform(0.7, 1), random.uniform(0.7, 1), 1.0)
        self.x = x
        self.y = WINDOW_Y
        self.num = num

    def draw(self):
        color = self.star_color
        MidpointCircle(self.x, self.y, 5, color)
        MidpointLine(self.x, self.y, self.x - 5, self.y - 5, color)
        MidpointLine(self.x, self.y, self.x + 5, self.y - 5, color)

class Fairy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_circle(self, cx, cy, r, color):
        glColor3f(*color)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(cx, cy)
        for i in range(36):
            angle = 2 * math.pi * i / 36
            glVertex2f(cx + r * math.cos(angle), cy + r * math.sin(angle))
        glEnd()

    def draw(self):
        # Sayap kiri atas
        self.draw_circle(self.x - 10, self.y + 8, 8, (0.7, 0.9, 1.0))  # biru langit cerah
        # Sayap kiri bawah
        self.draw_circle(self.x - 12, self.y - 2, 6, (0.7, 0.9, 1.0))

        # Sayap kanan atas
        self.draw_circle(self.x + 10, self.y + 8, 8, (0.7, 0.9, 1.0))
        # Sayap kanan bawah
        self.draw_circle(self.x + 12, self.y - 2, 6, (0.7, 0.9, 1.0))

        # Tubuh peri - bentuk oval memanjang
        glColor3f(0.95, 0.6, 0.9)  # pink cerah
        glBegin(GL_POLYGON)
        for i in range(36):
            angle = 2 * math.pi * i / 36
            glVertex2f(self.x + 5 * math.cos(angle), self.y + 12 * math.sin(angle))
        glEnd()

        # Kepala
        self.draw_circle(self.x, self.y + 15, 5, (1.0, 0.8, 0.9))  # warna kulit/fantasy head

        # Mahkota kecil
        self.draw_circle(self.x, self.y + 20, 2.2, (1.0, 0.85, 0.2))  # kuning cerah mahkota

class MagicBullet:
    def __init__(self, x, y, color=(1.0, 0.3, 0.5)):  # merah muda terang
        self.x = x
        self.y = y
        self.color = color

    def move(self):
        self.y += 12

    def draw(self):
        # Sayap kiri
        glColor3f(0.7, 0.9, 1.0)  # biru muda pastel
        glBegin(GL_TRIANGLES)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x - 10, self.y + 12)
        glVertex2f(self.x - 5, self.y + 6)
        glEnd()

        # Sayap kanan
        glBegin(GL_TRIANGLES)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + 10, self.y + 12)
        glVertex2f(self.x + 5, self.y + 6)
        glEnd()

        # Kepala
        glColor3f(1.0, 0.8, 0.6)  # peach
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(self.x, self.y + 8)
        for i in range(20):
            angle = i * 2 * math.pi / 20
            glVertex2f(self.x + math.cos(angle) * 3, self.y + 8 + math.sin(angle) * 3)
        glEnd()

        # Tubuh
        glColor3f(*self.color)  # merah muda neon
        glBegin(GL_POLYGON)
        glVertex2f(self.x, self.y + 6)
        glVertex2f(self.x - 2.5, self.y - 2)
        glVertex2f(self.x - 1.5, self.y - 10)
        glVertex2f(self.x + 1.5, self.y - 10)
        glVertex2f(self.x + 2.5, self.y - 2)
        glEnd()

        
class FlowerEnemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.choice(["flower", "star", "mushroom"])
        self.petal_color = (random.random(), random.random(), random.random())
        self.center_color = (1.0, 1.0, 0.5)

    def move(self):
        self.y -= 4

    def draw(self):
        if self.type == "flower":
            self.draw_flower()
        elif self.type == "star":
            self.draw_star()
        elif self.type == "mushroom":
            self.draw_mushroom()

    def draw_flower(self):
        # Kelopak bunga
        glColor3f(*self.petal_color)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(self.x, self.y)
        for i in range(9):
            angle = i * 2 * pi / 8
            glVertex2f(
                self.x + 18 * cos(angle),
                self.y + 18 * sin(angle)
            )
        glEnd()
        # Pusat bunga
        glColor3f(*self.center_color)
        glBegin(GL_POLYGON)
        for i in range(30):
            angle = i * 2 * pi / 30
            glVertex2f(
                self.x + 6 * cos(angle),
                self.y + 6 * sin(angle)
            )
        glEnd()

    def draw_star(self):
        glColor3f(*self.petal_color)
        spikes = 5
        outer_radius = 16
        inner_radius = 8
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(self.x, self.y)
        for i in range(spikes * 2 + 1):
            angle = i * pi / spikes
            r = outer_radius if i % 2 == 0 else inner_radius
            glVertex2f(self.x + r * cos(angle), self.y + r * sin(angle))
        glEnd()

    def draw_mushroom(self):
        # Topi jamur
        glColor3f(*self.petal_color)
        glBegin(GL_POLYGON)
        for i in range(20):
            angle = pi * i / 20
            glVertex2f(self.x + 15 * cos(angle), self.y + 10 * sin(angle))
        glEnd()

        # Batang jamur
        glColor3f(0.9, 0.8, 0.7)
        glBegin(GL_QUADS)
        glVertex2f(self.x - 4, self.y)
        glVertex2f(self.x + 4, self.y)
        glVertex2f(self.x + 3, self.y - 12)
        glVertex2f(self.x - 3, self.y - 12)
        glEnd()
        
        