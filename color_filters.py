import imageio
import numpy as np
from math import *
from PIL import Image
import cv2


def red_tresholding(im_name, im, tsh):
    height = im.shape[0]
    width = im.shape[1]
    result = np.zeros((height, width, 3), np.uint8)

    for i in range(height):
        for j in range(width):
            result[i][j][1] = im[i][j][1]
            result[i][j][2] = im[i][j][2]
            if im[i][j][0] > tsh:
                result[i][j][0] = 255
    imageio.imwrite('post_processed_images/red_tsh_' + im_name, result)


def green_tresholding(im_name, im, tsh):
    height = im.shape[0]
    width = im.shape[1]
    result = np.zeros((height, width, 3), np.uint8)

    for i in range(height):
        for j in range(width):
            if im[i][j][1] > tsh:
                result[i][j][1] = 255
    imageio.imwrite('post_processed_images/green_tsh_' + im_name, result)


def blue_tresholding(im_name, im, tsh):
    height = im.shape[0]
    width = im.shape[1]
    result = np.zeros((height, width, 3), np.uint8)

    for i in range(height):
        for j in range(width):
            if im[i][j][2] > tsh:
                result[i][j][2] = 255
    imageio.imwrite('post_processed_images/blue_tsh_' + im_name, result)


def full_tresholding(im_name, im, tsh_list):
    height = im.shape[0]
    width = im.shape[1]
    result = np.zeros((height, width, 3), np.uint8)

    for i in range(height):
        for j in range(width):
            for tsh in tsh_list:
                channel = tsh_list.index(tsh)
                if tsh > 0:
                    if im[i][j][channel] > tsh:
                        result[i][j][channel] = 255
                else:
                    result[i][j][channel] = im[i][j][channel]
    imageio.imwrite('post_processed_images/full_tsh_' + im_name, result)


def brightness (im_name, im, br):
    height = im.shape[0]
    width = im.shape[1]
    result = np.zeros((height, width, 3), np.uint8)

    for i in range(height):
        for j in range(width):
            for z in range(im.shape[2]):
                b = im[i][j][z] + br
                if b > 255:
                    b = 255
                result[i][j][z] = b
    imageio.imwrite('post_processed_images/brightness_' + im_name, result)


def sepia(im_name, im):
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            r, g, b = im[i][j][0], im[i][j][1], im[i][j][2]
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            if tr > 255:
                r = 255
            else:
                r = tr

            if tg > 255:
                g = 255
            else:
                g = tg

            if tb > 255:
                b = 255
            else:
                b = tb

            im[i][j] = [r, g, b]

        imageio.imwrite('post_processed_images/sepia_' + im_name, im)


def chroma_key(input_img):
    output_img = Image.new("RGBA", input_img.size)

    tola, tolb = 200, 100
    for y in range(input_img.size[1]):
        for x in range(input_img.size[0]):
            p = list(input_img.getpixel((x, y)))
            d = int(sqrt(pow(p[0], 2) + pow((p[1] - 255), 2) + pow(p[2], 2)))
            if d > tola:
                d = 255
            elif (tolb < d):
                p[1] = p[1] - (255 - d)
                d = (d - tolb) * (255 / (tola - tolb))
            else:
                d = 0
            output_img.putpixel((x, y), (p[0], p[1], p[2], int(d)))

    output_img.save('chroma.png', "PNG")


def chroma_add_background(im_name, cut_image, background_image):
    for i in range(background_image.shape[0]):
        for j in range(background_image.shape[1]):
            if cut_image[i][j][3] == 255:
                background_image[i][j] = cut_image[i][j]

    imageio.imwrite('post_processed_images/chroma_' + im_name, background_image)

def ultimate_chroma(f, b):
    g = lambda f, b: np.copyto(f, b, 'no', np.logical_or(f == [0, 255, 0], f == [0, 255, 0]))

    g(f, b)

    cv2.imwrite("out.png", f)
