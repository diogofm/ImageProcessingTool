from math import *


def rgb_to_cmy(r, g, b):
    return 255 - r, 255 - g, 255 - b


def rgb_to_hsi(r, g, b):
    i = (r + g + b)/3

    num = (((r-g) + (r - b))/2)
    den = ((((r - g) ** 2) + ((r - b) * (g - b))) ** 0.5)
    theta = degrees(acos(num/den))

    if b <= g:
        h = theta
    else:
        h = 360 - theta

    s = 1 - ((3/(r + g + b)) * min([r, g, b]))

    return h, s, i


def hsi_to_rgb(h, s, i):
    r, g, b = [0, 0, 0]
    if 0 <= h < 120:
        b = i * (1 - s)
        r = i * (1 + ((s * cos(radians(h)))/(cos(radians(60 - h)))))
        g = 3 * i - (r + b)

    elif 120 <= h < 240:
        r = i * (1 - s)
        g = i * (1 + ((s * cos(radians(h)))/(cos(radians(60 - h)))))
        b = 3 * i - (r + g)

    elif 240 <= h <= 360:
        h = h - 240
        g = i * (1 - s)
        b = i * (1 + ((s * cos(radians(h)))/(cos(radians(60 - h)))))
        r = 3 * i - (b + g)

    return r, g, b


def hsi_to_cmy(h, s, i):
    r, g, b = hsi_to_rgb(h, s, i)
    return rgb_to_cmy(r, g, b)


def cmy_to_rgb(c, m, y):
    return 255 - c, 255 - m, 255 - y


def cmy_to_hsi(c, m, y):
    r, g, b = cmy_to_rgb(c, m, y)
    return rgb_to_hsi(r, g, b)
