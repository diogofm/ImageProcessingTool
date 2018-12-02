import imageio
import numpy as np
from math import *
import cv2


def _erosion(im, radius):
    struct_element = (cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (radius, radius)))

    sz = int(ceil(radius - 1 / 2))

    height, width = im.shape

    new_im = cv2.copyMakeBorder(im, sz, sz, sz, sz, cv2.BORDER_CONSTANT,
                                value=0)
    result = new_im.copy()

    imageio.imsave('teste.tif', new_im)

    for x in range(sz, height - sz):
        for y in range(sz, width - sz):
            elements_list = list()
            for i in range(struct_element.shape[0]):
                for j in range(struct_element.shape[1]):
                    if struct_element[i][j] == 1:
                        elements_list.append(new_im[x + i - sz][y + j - sz])
            result[x][y] = min(elements_list)

    return result


def _dilation(im, radius):
    struct_element = (cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (radius, radius)))

    sz = int(ceil(radius - 1 / 2))

    height, width = im.shape

    new_im = cv2.copyMakeBorder(im, sz, sz, sz, sz, cv2.BORDER_CONSTANT,
                                value=0)
    result = new_im.copy()

    for x in range(sz, height - sz):
        for y in range(sz, width - sz):
            elements_list = list()
            for i in range(struct_element.shape[0]):
                for j in range(struct_element.shape[1]):
                    if struct_element[i][j] == 1:
                        elements_list.append(new_im[x + i - sz][y + j - sz])
            result[x][y] = max(elements_list)

    return result


def erosion(im_name, im, radius):
    struct_element = (cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (radius, radius)))

    sz = int(ceil(radius - 1 / 2))

    height, width = im.shape

    new_im = cv2.copyMakeBorder(im, sz, sz, sz, sz, cv2.BORDER_CONSTANT,
                                value=0)
    result = new_im.copy()

    imageio.imsave('teste.tif', new_im)

    for x in range(sz, height - sz):
        for y in range(sz, width - sz):
            elements_list = list()
            for i in range(struct_element.shape[0]):
                for j in range(struct_element.shape[1]):
                    if struct_element[i][j] == 1:
                        elements_list.append(new_im[x + i - sz][y + j - sz])
            result[x][y] = min(elements_list)

    imageio.imsave('erosion.tif', result)


def dilation(im_name, im, radius):
    struct_element = (cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (radius, radius)))

    sz = int(ceil(radius - 1 / 2))

    height, width = im.shape

    new_im = cv2.copyMakeBorder(im, sz, sz, sz, sz, cv2.BORDER_CONSTANT,
                                value=0)
    result = new_im.copy()

    imageio.imsave('teste.tif', new_im)

    for x in range(sz, height - sz):
        for y in range(sz, width - sz):
            elements_list = list()
            for i in range(struct_element.shape[0]):
                for j in range(struct_element.shape[1]):
                    if struct_element[i][j] == 1:
                        elements_list.append(new_im[x + i - sz][y + j - sz])
            result[x][y] = max(elements_list)

    imageio.imsave('dilation.tif', result)


def gradient(im_name, im, radius):
    dilated = _dilation(im, radius)
    eroded = _erosion(im, radius)

    result = dilated - eroded

    imageio.imsave('gradient.tif', result)


# im = imageio.imread("Fig0937(a)(ckt_board_section).tif")
# erosion("Fig0937(a)(ckt_board_section).tif", im, 5)
# dilation("Fig0937(a)(ckt_board_section).tif", im, 5)

im = imageio.imread("Fig0939(a)(headCT-Vandy).tif")
gradient("Fig0939(a)(headCT-Vandy).tif", im, 3)
