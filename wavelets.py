import imageio
import numpy as np
from math import *
from PIL import Image


def haar(data):
    w0 = 0.5
    w1 = -0.5
    s0 = 0.5
    s1 = 0.5

    temp = np.zeros(data.shape, dtype=np.float)

    h = data.shape[0] >> 1

    for i in range(h):
        k = i << 1
        temp[i] = data[k] * s0 + data[k + 1] * s1
        temp[i + h] = data[k] * w0 + data[k + 1] * w1

    for i in range(data.shape[0]):
        data[i] = temp[i]


def inverse_haar(data):
    w0 = 0.5
    w1 = -0.5
    s0 = 0.5
    s1 = 0.5

    temp = np.zeros(data.shape, dtype=np.float)

    h = data.shape[0] >> 1

    for i in range(h):
        k = i << 1
        temp[k] = (data[i] * s0 + data[i + h] * w0) / w0
        temp[k + 1] = (data[i] * s1 + data[i + h] * w1) / s0

    for i in range(data.shape[0]):
        data[i] = temp[i]


def inverse_haar_2D_component(im, iterations):
    rows, columns = im.shape

    row = np.zeros(rows)
    column = np.zeros(columns)

    for l in range(iterations):
        for j in range(columns):
            for i in range(row.shape[0]):
                column[i] = im[i][j]

            inverse_haar(column)

            for i in range(row.shape[0]):
                im[i][j] = column[i]

        for i in range(rows):
            for j in range(row.shape[0]):
                row[j] = im[i][j]

            inverse_haar(row)

            for j in range(row.shape[0]):
                im[i][j] = row[j]


def inverse_haar_2D_grayscale(im_name, im, iterations):
    rows, columns = im.shape

    row = np.zeros(rows)
    column = np.zeros(columns)

    for l in range(iterations):
        for j in range(columns):
            for i in range(row.shape[0]):
                column[i] = im[i][j]

            inverse_haar(column)

            for i in range(row.shape[0]):
                im[i][j] = column[i]

        for i in range(rows):
            for j in range(row.shape[0]):
                row[j] = im[i][j]

            inverse_haar(row)

            for j in range(row.shape[0]):
                im[i][j] = row[j]

    imageio.imwrite("post_processed_images/inverse_haar_" + im_name, im)


def haar_2D_component(im, iterations):
    rows, columns = im.shape

    for k in range(iterations):
        level = 1 << k

        level_columns = int(columns/level)
        level_rows = int(rows/level)

        row = np.zeros(level_rows)

        for i in range(level_rows):
            for j in range(row.shape[0]):
                row[j] = im[i][j]

            haar(row)

            for j in range(row.shape[0]):
                im[i][j] = row[j]

        column = np.zeros(level_columns)
        for j in range(level_columns):
            for i in range(column.shape[0]):
                column[i] = im[i][j]

            haar(column)

            for i in range(column.shape[0]):
                im[i][j] = column[i]


def haar_2D_grayscale(im_name, im, iterations):
    rows, columns = im.shape

    # row = np.zeros(rows)
    # column = np.zeros(columns)

    for k in range(iterations):
        level = 1 << k

        level_columns = int(columns/level)
        level_rows = int(rows/level)

        row = np.zeros(level_rows)

        for i in range(level_rows):
            for j in range(row.shape[0]):
                row[j] = im[i][j]

            haar(row)

            for j in range(row.shape[0]):
                im[i][j] = row[j]

        column = np.zeros(level_columns)
        for j in range(level_columns):
            for i in range(column.shape[0]):
                column[i] = im[i][j]

            haar(column)

            for i in range(column.shape[0]):
                im[i][j] = column[i]

    imageio.imwrite("post_processed_images/haar_" + im_name, im)


def haar_2D_rgb(im_name, im, iterations):
    rows, columns, colors = im.shape

    r = im[:, :, 0]
    g = im[:, :, 1]
    b = im[:, :, 2]

    haar_2D_component(r, iterations)
    haar_2D_component(g, iterations)
    haar_2D_component(b, iterations)

    image = Image.new('RGB', (im.shape[0], im.shape[1]))

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            image.putpixel((j, i), (r[i][j], g[i][j], b[i][j]))

    # for k in range(iterations):
    #     level = 1 << k
    #
    #     level_columns = int(columns/level)
    #     level_rows = int(rows/level)
    #
    #     for color in range(colors):
    #
    #         row = np.zeros(level_rows)
    #
    #         for i in range(level_rows):
    #             for j in range(row.shape[0]):
    #                 row[j] = im[i][j][color]
    #
    #             haar(row)
    #
    #             for j in range(row.shape[0]):
    #                 im[i][j][color] = row[j]
    #
    #         column = np.zeros(level_columns)
    #         for j in range(level_columns):
    #             for i in range(column.shape[0]):
    #                 column[i] = im[i][j][color]
    #
    #             haar(column)
    #
    #             for i in range(column.shape[0]):
    #                 im[i][j][color] = column[i]

    imageio.imwrite("post_processed_images/haarR_" + im_name, r)
    imageio.imwrite("post_processed_images/haarG_" + im_name, g)
    imageio.imwrite("post_processed_images/haarB_" + im_name, b)

    imageio.imwrite("post_processed_images/haar_" + im_name, im)
    image.save('haar.png', "PNG")


def inverse_haar_2D_rgb(im_name, im, iterations):
    rows, columns, colors = im.shape

    r = im[:, :, 0]
    g = im[:, :, 1]
    b = im[:, :, 2]

    inverse_haar_2D_component(r, iterations)
    inverse_haar_2D_component(g, iterations)
    inverse_haar_2D_component(b, iterations)

    image = Image.new('RGB', (im.shape[0], im.shape[1]))

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            image.putpixel((j, i), (r[i][j], g[i][j], b[i][j]))

    imageio.imwrite("post_processed_images/inverse_haarR_" + im_name, r)
    imageio.imwrite("post_processed_images/inverse_haarG_" + im_name, g)
    imageio.imwrite("post_processed_images/inverse_haarB_" + im_name, b)

    imageio.imwrite("post_processed_images/inverse_haar_" + im_name, im)
    image.save('inverse_haar.png', "PNG")
