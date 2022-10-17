from gl import Renderer, _color_, V2, V3
from textures import Texture
from obj import Obj

from shaders import gourad, toon, glow, greyScale

#################################

width = 1300
height = 866
depth = -10
black = _color_(0, 0, 0)
white = _color_(1, 1, 1)

rend = Renderer(width, height)
#rend.dirLight = V3(0, 0, 1)
rend.background = Texture("models/background.bmp")
rend.glClearBackground()
#################################
rend.active_shader = gourad
rend.active_texture = Texture("models/maracasTX.bmp")
rend.glLoadModel("models/maraca.obj",
                 translate=V3(5, -5, -11),
                 scale=V3(0.1, 0.1, 0.1),
                 rotate=V3(0, 30, 5))
#################################
rend.active_shader = glow
rend.active_texture = Texture("models/yellowTX.bmp")
rend.glLoadModel("models/Trumpet.obj",
                 translate=V3(2, -3.5, -13),
                 scale=V3(4, 4, 4),
                 rotate=V3(0, -22, 70))
#################################
rend.active_shader = greyScale
rend.active_texture = Texture("models/drumTX.bmp")
rend.glLoadModel("models/drum.obj",
                 translate=V3(4.4, -3.5, -10),
                 scale=V3(1.4, 1.4, 1.4),
                 rotate=V3(5, -30, 0))
#################################
rend.active_shader = toon
rend.active_texture = Texture("models/CelloTX.bmp")
rend.glLoadModel("models/Cello.obj",
                 translate=V3(-7, -5, -11),
                 scale=V3(0.07, 0.07, 0.07),
                 rotate=V3(0, 50, 0))
#################################
rend.active_shader = greyScale
rend.active_texture = Texture("models/MicTX.bmp")
rend.glLoadModel("models/Mic.obj",
                 translate=V3(-1, -5.5, -11),
                 scale=V3(4, 4, 4),
                 rotate=V3(0, 0, 0))
#################################

rend.write("Proyecto.bmp")
