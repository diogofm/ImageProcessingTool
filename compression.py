import imageio
import numpy as np
from math import *
from PIL import Image
from wavelets import *
import itertools as its
from re import sub


def encode(text):
    return sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1),text)


def decode(text):
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)),text)


def tolerance_normalize(im, tolerance):
    height, width, colors = im.shape

    for c in range(colors):
        for i in range(height):
            for j in range(width - 1):
                current_pixel = im[i][j][c]
                next_pixel = im[i][j + 1][c]
                if abs(int(current_pixel) - int(next_pixel)) < tolerance:
                    im[i][j + 1][c] = current_pixel


def decompress(im_name, haar_size, rgb):
    im_np = np.zeros((512, 512, 3), dtype=np.uint8)

    if rgb:
        for c in range(3):
            decompress_file = open(im_name + '.777' + str(c), 'r', encoding='utf-8')
            decompress_lines = decompress_file.readlines()

            idx = 0
            for decompress_line in decompress_lines:
                row = decode(decompress_line)[:-1]
                print(len(row))

                for i in range(len(row)):
                    im_np[idx][i][c] = ord(row[i])
                idx = idx + 1

        print("Inverse Haar...")
        inverse_haar_2D_rgb(im_name, im_np, haar_size)
        print("Inverse Haar DONE!")

        imageio.imwrite("post_processed_images/dec_" + im_name, im_np)


def compress(im_name, haar_size, tolerance, gain_or_loss):
    im = imageio.imread(im_name)

    print("Haar preprocessing...")
    haar_2D_rgb(im_name, im, haar_size)
    print("Haar preprocessing DONE!")

    im = imageio.imread("post_processed_images/haar_" + im_name)
    #
    print("Tolerance normalization...")
    tolerance_normalize(im, tolerance)
    print("Tolerance normalization DONE!")

    height, width, colors = im.shape
    for c in range(colors):
        compress_file = open(im_name + '.777' + str(c), 'w', encoding="utf-8")
        for i in range(height):
            row = ''
            for j in range(width):
                while chr(im[i][j][c]).isdigit():
                    if gain_or_loss:
                        im[i][j][c] = im[i][j][c] + 1
                    else:
                        im[i][j][c] = im[i][j][c] - 1
                row = row + chr(im[i][j][c])

            encoded_row = encode(row)

            compress_file.write(encoded_row)
            compress_file.write('\n')

        compress_file.close()


compress('Fig0637(a)(caster_stand_original).tif', 2, 5, False)
decompress('Fig0637(a)(caster_stand_original).tif', 2, True)
