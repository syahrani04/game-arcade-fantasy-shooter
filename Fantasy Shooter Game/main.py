from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GLUT import GLUT_BITMAP_HELVETICA_18
from classes import Fairy, MagicBullet, FlowerEnemy, Star
from circle import MidpointCircle
import time
import math
import random
from math import cos, sin


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

stars = []  
bullets = []
enemies = []
fairy = Fairy(400, 60)
score = 0
lives = 3
game_over = False
on_start_screen = True

move = {'left': False, 'right': False, 'up': False, 'down': False, 'space': False}
last_shot_time = 0


def init():
    glClearColor(0.6, 0.7, 0.95, 1.0)
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)

def draw_text(x, y, text):
    glColor3f(1, 1, 1)
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

def draw_background():
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.7, 1.0)
    glVertex2f(0, 0)
    glVertex2f(WINDOW_WIDTH, 0)
    glColor3f(0.4, 0.5, 0.9)
    glVertex2f(WINDOW_WIDTH, WINDOW_HEIGHT)
    glVertex2f(0, WINDOW_HEIGHT)
    glEnd()
    
def draw_info_panel():
    # Ganti warna latar putih transparan jadi warna lain (misal biru muda transparan)
    glColor4f(0.2, 0.5, 0.8, 0.6)  # contoh warna biru muda dengan transparansi 0.6
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glBegin(GL_QUADS)
    glVertex2f(10, 520)
    glVertex2f(160, 520)
    glVertex2f(160, 580)
    glVertex2f(10, 580)
    glEnd()
    glDisable(GL_BLEND)

    # Tulisan "score" dan "nyawa"
    glColor3f(0, 0, 0)
    draw_text(20, 565, "Score: ")
    draw_text(20, 545, "Nyawa: ")

    # Nilai score
    draw_text(100, 565, str(score))

    # Gambar hati berjajar
    for i in range(lives):
        draw_heart(100 + i * 15, 547, size=5.5)

    
def draw_heart(x, y, size=8, color=(1.0, 0.2, 0.3)):
    glColor3f(*color)
    glBegin(GL_POLYGON)
    for angle in range(0, 360, 1):
        rad = math.radians(angle)
        x_ = size * math.sin(rad) ** 3
        y_ = size * (13 * math.cos(rad) - 5 * math.cos(2 * rad)
                     - 2 * math.cos(3 * rad) - math.cos(4 * rad)) / 16
        glVertex2f(x + x_, y + y_)
    glEnd()
    

def draw_stars():
    for star in stars:
        star.draw()
        star.y -= 2
    stars[:] = [s for s in stars if s.y > -40]

def draw_bullets():
    for bullet in bullets:
        bullet.draw()
        bullet.move()
    bullets[:] = [b for b in bullets if b.y < WINDOW_HEIGHT]

def draw_enemies():
    global lives, game_over
    remaining = []
    for enemy in enemies:
        enemy.move()
        if enemy.y < 0:
            lives -= 1
            if lives <= 0:
                game_over = True
        enemy.draw()
        remaining.append(enemy)
    enemies[:] = remaining

def check_collisions():
    global score
    new_bullets = []
    for bullet in bullets: 
        hit = False
        for enemy in enemies:
            dx = bullet.x - enemy.x
            dy = bullet.y - enemy.y
            if dx * dx + dy * dy < 30 * 30:
                enemies.remove(enemy)
                score += 10
                MidpointCircle(enemy.x, enemy.y, 10, (1.0, 0.9, 0.0))
                hit = True
                break
        if not hit:
            new_bullets.append(bullet)
    bullets[:] = new_bullets

def fire_bullets():
    global bullets, last_shot_time
    if time.time() - last_shot_time > 0.2:
        x = fairy.x
        y = fairy.y + 20
        bullets.append(MagicBullet(x, y, (1.0, 1.0, 0.0)))
        bullets.append(MagicBullet(x - 10, y, (0.0, 1.0, 1.0)))
        bullets.append(MagicBullet(x + 10, y, (1.0, 0.0, 1.0)))
        last_shot_time = time.time()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_background()
    draw_stars()
    draw_info_panel()

    if on_start_screen:
        draw_text(270, 320, "FANTASY FAIRY SHOOTER")
        draw_text(290, 280, "Press SPACE to Start")
    elif game_over:
        center_x = WINDOW_WIDTH // 2
        draw_text(center_x - 55, 320, "GAME OVER")
        draw_text(center_x - 65, 290, f"Final Score: {score}")
        draw_text(center_x - 85, 260, "Press R to Restart")
    
    else:
        fairy.draw()
        draw_bullets()
        draw_enemies()
        check_collisions()
        draw_info_panel()

    glutSwapBuffers()

def timer(value):
    if not game_over and not on_start_screen:
        if move['left'] and fairy.x > 20:
            fairy.x -= 10
        if move['right'] and fairy.x < WINDOW_WIDTH - 20:
            fairy.x += 10
        if move['up'] and fairy.y < WINDOW_HEIGHT - 40:
            fairy.y += 10
        if move['down'] and fairy.y > 20:
            fairy.y -= 10
        if move['space']:
            fire_bullets()
        if random.randint(0, 5) == 0:
            stars.append(Star(random.randint(0, WINDOW_WIDTH), random.randint(0, 100)))
        if random.randint(0, 20) == 0:
            enemies.append(FlowerEnemy(random.randint(50, 750), WINDOW_HEIGHT))

    glutPostRedisplay()
    glutTimerFunc(33, timer, 0)

def keyboard_ascii(key, x, y):
    global on_start_screen, game_over
    if on_start_screen and key == b' ':
        on_start_screen = False
    elif key == b' ': move['space'] = True
    elif key == b'r' and game_over:
        reset_game()

def keyboard_ascii_up(key, x, y):
    if key == b' ': move['space'] = False

def keyboard(key, x, y):
    if key == GLUT_KEY_LEFT: move['left'] = True
    elif key == GLUT_KEY_RIGHT: move['right'] = True
    elif key == GLUT_KEY_UP: move['up'] = True
    elif key == GLUT_KEY_DOWN: move['down'] = True

def keyboard_up(key, x, y):
    if key == GLUT_KEY_LEFT: move['left'] = False
    elif key == GLUT_KEY_RIGHT: move['right'] = False
    elif key == GLUT_KEY_UP: move['up'] = False
    elif key == GLUT_KEY_DOWN: move['down'] = False

def reset_game():
    global enemies, bullets, stars, fairy, score, lives, game_over, on_start_screen
    enemies.clear()
    bullets.clear()
    stars.clear()
    fairy.x, fairy.y = 400, 60
    score = 0
    lives = 3
    game_over = False
    on_start_screen = True

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Fantasy Fairy Shooter")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard_ascii)
    glutKeyboardUpFunc(keyboard_ascii_up)
    glutSpecialFunc(keyboard)
    glutSpecialUpFunc(keyboard_up)
    glutTimerFunc(0, timer, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()