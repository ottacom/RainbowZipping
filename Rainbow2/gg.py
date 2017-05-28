from PIL import Image, ImageColor
from colorsys import rgb_to_hls, hls_to_rgb

IMAGE_SRC = 'coding.png'

def showme(img):
    """ use PIL standard display """
    img.show()

def h_dist(h1, h2):
    """ distance between color hues in angular space,
    where 1.0 == 0.0 (so distance must wrap around if > 1)"""
    return min(abs(h1+1-h2), abs(h1-h2), abs(h1-1-h2))

def rgb2hls(t):
    """ convert PIL-like RGB tuple (0 .. 255) to colorsys-like
    HSL tuple (0.0 .. 1.0) """
    r,g,b = t
    r /= 255.0
    g /= 255.0
    b /= 255.0
    return rgb_to_hls(r,g,b)

def hls2rgb(t):
    """ convert a colorsys-like HSL tuple (0.0 .. 1.0) to a
    PIL-like RGB tuple (0 .. 255) """
    r,g,b = hls_to_rgb(*t)
    r *= 255
    g *= 255
    b *= 255
    return (int(r),int(g),int(b))

def reload_img():
    global img, sizew, sizeh, maxsize, imgdata
    img = Image.open(IMAGE_SRC)
    sizew, sizeh = img.size
    maxsize = ((sizew/2)**2 + (sizeh/2)**2)**0.5
    imgdata = list(img.getdata())
