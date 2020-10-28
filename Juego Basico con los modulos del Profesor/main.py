import random
from utils import *

def Colision_MT(x,y,x0,xf,h):
    if(x >= x0 and x <= xf):
        if(y <= h):
            return True
        else:
            return False
    else:
        return False

#inicia juego
pygame.init()

ancho = 1000
alto = 900
velocidadX = 10
velocidadY = 10
terminado = False

pantalla = pygame.display.set_mode( (ancho, alto), pygame.OPENGL )
scale = 1
width, height = 1000, 900

pygame.init()
#display_openGL(width, height, scale)
ventana = pygame.display.set_mode((width, height), pygame.OPENGL)
pygame.display.set_caption('JUEGO JOSH')

#Colo de fondo
glClearColor(11/255,30/255,48/255,1.0)
glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
glScalef(scale, scale, 30)
gluOrtho2D(-1 * width / 2, width / 2, -1 * height / 2, height / 2)
pygame.key.set_repeat(1,25)

#Personaje Principal
x, y = 0, -130
x, y = MovePersonaje1(x, y, 0, 0, 2, 20)
#Opstaculos
sizePiedra = 1
x2 = random.randint(-200, 500)
y2 = 400
x2, y2 = Movepiedra(x2, y2, 0, 0, sizePiedra, 0)

contador = 0
while not terminado:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminado = True

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        sx = 5
        sy = 0
        x, y = MovePersonaje1(x, y, sx, sy, 1,10)
    if keys[K_RIGHT]:
        sx = -5
        sy = 0
        x, y = MovePersonaje1(x, y, sx, sy, 1,10)
    if keys[K_UP]:
        sx = 0
        sy = 5
        x, y = MovePersonaje1(x, y, sx, sy, 1,10)
    if keys[K_DOWN]:
        sx = 0
        sy = -5
        x, y = MovePersonaje1(x, y, sx, sy, 1,10)
    #Colision
    x0 = x2 - 100
    xf = x2 + 10
    y0 = y2 - 10
    yf = y2 + 100
    yblock = y
    #Roca impacta con terminator
    if( x >= x0 and x <= xf and yblock == y0 ):
        despintarpiedra(x2,y2,1)
        sy = 0
        Movepiedra(x2, y2, 0, 0, sizePiedra, 0)
        print()
        print("***GAME OVER***")
        break
    else:
        sx = 0
        sy = -1
        x2, y2 = Movepiedra(x2, y2, sx, sy, sizePiedra, 0)

        #Roca reinicia su recorrido
        if(y2 <=  -250 ):
            x2 = random.randint(-200, 400)
            y2 = 400
            x2, y2 = Movepiedra(x2, y2, 0, 0, sizePiedra, 0)
            contador += 1
    if contador == 5:
       print()
       print("***GANASTE***")
       break

    pygame.display.flip()
pygame.quit()