from OpenGL.GL import *

def MidpointLine(x1, y1, x2, y2, color=(1.0, 1.0, 1.0)):
    glColor3f(*color)
    glBegin(GL_POINTS)

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx > dy:
        err = dx / 2.0
        while x != x2:
            glVertex2f(x, y)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            glVertex2f(x, y)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    glVertex2f(x, y)
    glEnd()
