from OpenGL.GL import *

def MidpointCircle(xc, yc, r, color=(1.0, 1.0, 1.0)):
    x = 0
    y = r
    d = 1 - r

    glColor3f(*color)
    glBegin(GL_POINTS)
    _draw_circle_points(xc, yc, x, y)
    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1
        _draw_circle_points(xc, yc, x, y)
    glEnd()

def _draw_circle_points(xc, yc, x, y):
    glVertex2f(xc + x, yc + y)
    glVertex2f(xc - x, yc + y)
    glVertex2f(xc + x, yc - y)
    glVertex2f(xc - x, yc - y)
    glVertex2f(xc + y, yc + x)
    glVertex2f(xc - y, yc + x)
    glVertex2f(xc + y, yc - x)
    glVertex2f(xc - y, yc - x)
