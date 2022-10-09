from gl import Renderer, _color_, V2, V3
from textures import Texture
from obj import Obj

from shaders import flat, unlit, gourad, toon, glow, textureBlend, greyScale, normalMap

#################################

width = 1300
height = 866
depth = -10
black = _color_(0, 0, 0)
white = _color_(1, 1, 1)

rend = Renderer(width, height)
#rend.dirLight = V3(0, 0, 1)
rend.background = Texture("models/studio.bmp")
rend.glClearBackground()

#################################

rend.write("output.bmp")
