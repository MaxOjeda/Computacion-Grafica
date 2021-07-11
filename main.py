from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PIL.Image import open
import sys
import time

gifs = ['test/','test/','test/']
limits = [9,9,9]
indexs = [0,0,0]

cuad1= [(100, 100), (300, 100), (300, 300), (100, 300)]
cuad2= [(500, 100), (700, 100), (700, 300), (500, 300)]
cuad3= [(300, 400), (500, 400), (500, 600), (300, 600)]


colores = [(0.098,0.811,0.345), (0.882,0.717,0.117), (0.188,0.619,0.929)]
texture = [(1,0), (1,1), (0,1), (0, 0)]

window = 0                                             
width, height = 800, 700

vertex = 1
cuadrilatero = 0
index = 0
mode = 0

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw():
    global index
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2d(glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT))

    if mode == 0:
        draw_square_color(cuad1, colores[0])
        draw_square_color(cuad2, colores[1])
        draw_square_color(cuad3, colores[2])
    elif mode == 1:
                
        draw_square_image(cuad1, gifs[0] + str(indexs[0]) + ".jpg")
        draw_square_image(cuad2, gifs[1] + str(indexs[1]) + ".jpg")
        draw_square_image(cuad3, gifs[2] + str(indexs[2]) + ".jpg")

        for i in range(len(indexs)):
            indexs[i] += 1
            if indexs[i] > limits[i]:
                indexs[i] = 0

        time.sleep(0.2)
    glutSwapBuffers()


def init_glut():
    glutInit()                                             # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)                      # set window size
    glutInitWindowPosition(0, 0)                           # set window position
    window = glutCreateWindow("cp-project")              # create window with title
    glutDisplayFunc(draw)                               # set draw function callback
    glutKeyboardFunc(keyboard2)
    glutMouseFunc(mouse)
    glutIdleFunc(draw)                                     # draw all the time
    glutMainLoop()

def draw_square_color(vertices, color):
    glColor3fv(color)

    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex2fv(vertex)
    glEnd()

def draw_square_image(vertices, image):
    LoadTextures(image)
    glEnable(GL_TEXTURE_2D)

    glBegin(GL_QUADS)
    i = 0
    for vertex in vertices:
        glVertex2fv(vertex); glTexCoord2fv(texture[i])
        i+=1
    glEnd()

def mouse(button, state, x, y):
    h = glutGet(GLUT_WINDOW_HEIGHT)
    print("mouse handler: ", button, state, x, h - y)
    #print vertex
    if button == GLUT_LEFT_BUTTON:
        if vertex == 1:
            cuad1[0] = (x, h - y)
        elif vertex == 2:
            cuad1[1] = (x, h - y)
        elif vertex == 3:
            cuad1[2] = (x, h - y)
        elif vertex == 4:
            cuad1[3] = (x, h - y)
        elif vertex == 5:
            cuad2[0] = (x, h - y)
        elif vertex == 6:
            cuad2[1] = (x, h - y)
        elif vertex == 7:
            cuad2[2] = (x, h - y)
        elif vertex == 8:
            cuad2[3] = (x, h - y)
        elif vertex == 9:
            cuad3[0] = (x, h - y)
        elif vertex == 10:
            cuad3[1] = (x, h - y)
        elif vertex == 11:
            cuad3[2] = (x, h - y)
        elif vertex == 12:
            cuad3[3] = (x, h - y)

def keyboard2(key, foo, bar):
    global vertex
    global mode
    global images
    global cuadrilatero

    if key == as_8_bit('q'):
        sys.exit() 
    elif key == as_8_bit('1'):
        if cuadrilatero == 0:
            vertex = 1
        elif cuadrilatero == 1:
            vertex = 5
        else:
            vertex = 9
    elif key == as_8_bit('2'):
        if cuadrilatero == 0:
            vertex = 2
        elif cuadrilatero == 1:
            vertex = 6
        else:
            vertex = 10
    elif key == as_8_bit('3'):
        if cuadrilatero == 0:
            vertex = 3
        elif cuadrilatero == 1:
            vertex = 7
        else:
            vertex = 11
    elif key == as_8_bit('4'):
        if cuadrilatero == 0:
            vertex = 4
        elif cuadrilatero == 1:
            vertex = 8
        else:
            vertex = 12
    elif key == as_8_bit('\t'):
        if cuadrilatero == 2:
            cuadrilatero = 0
            vertex = 1
        elif cuadrilatero == 1:
            cuadrilatero += 1
            vertex = 9
        else:
            cuadrilatero += 1
            vertex = 5
        print(cuadrilatero)
    elif key == as_8_bit('t'):
        mode = 1
    elif key == as_8_bit('y'):
        mode = 0
    else:
        TimerCBOwner(key, 2000, 5)

def LoadTextures(image):
    #global texture
    image = open(image)

    ix = image.size[0]
    iy = image.size[1]
    image = image.tobytes("raw", "RGBX", 0, -1)

    # Create Texture
    glBindTexture(GL_TEXTURE_2D, glGenTextures(1))   # 2d texture (x and y size)

    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


def main():
    init_glut()


main()
