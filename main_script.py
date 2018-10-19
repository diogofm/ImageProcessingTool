import imageio, sys, os
from image_filters import *
from color_conversion import *
from color_filters import *


def run_day_one(EXPONENT, LOG, x_0_1, y_0_1, x_1_1, y_1_1, x_0_2, y_0_2, x_1_2, y_1_2, x_0_3, y_0_3, x_1_3, y_1_3):
    images_path_list = os.listdir('./images/')

    for image_file_name in images_path_list:
        im = imageio.imread('images/' + image_file_name)
        image_histogram(image_file_name, im)
        print("Histogram for " + image_file_name + " done.")
        negative(image_file_name, im.copy())
        print("Negative for " + image_file_name + " done.")
        logarithmic(image_file_name, im.copy(), LOG)
        print("Logarithmic for " + image_file_name + " done.")
        gamma_correction(image_file_name, im.copy(), EXPONENT)
        print("Gamma Correction for " + image_file_name + " done.")
        histogram_equalization(image_file_name, im.copy())
        print("Histogram Equalization for " + image_file_name + " done.")
        piecewise_linear(image_file_name, im.copy(),
                         x_0_1, y_0_1, x_1_1, y_1_1, x_0_2, y_0_2, x_1_2, y_1_2, x_0_3, y_0_3, x_1_3, y_1_3)
        print("Piecewise Linear for " + image_file_name + " done.")
        bit_layers(image_file_name, im)
        print("BitLayer for " + image_file_name + " done.")


def run_day_two(kernel_weighted, kernel_conv, boost_constant):
    images_path_list = os.listdir('./images/')

    for image_file_name in images_path_list:
        im = imageio.imread('images/' + image_file_name)
        image_histogram(image_file_name, im)
        print("Histogram for " + image_file_name + " done.")
        averaging(image_file_name, im.copy())
        print("Average filter for " + image_file_name + " done.")
        weighted_averaging(image_file_name, im.copy(), kernel_weighted)
        print("Weighted Average filter for " + image_file_name + " done.")
        print("Used Kernel:")
        print(kernel_weighted)
        median_filter(image_file_name, im.copy())
        print("Median filter for " + image_file_name + " done.")
        convolution(image_file_name, im.copy(), kernel_conv)
        print("Convolution filter for " + image_file_name + " done.")
        print("Used Kernel:")
        print(kernel_conv)
        laplacian(image_file_name, im.copy())
        print("Laplacian filter for " + image_file_name + " done.")
        sobel(image_file_name, im.copy())
        print("Sobel filter for " + image_file_name + " done.")
        highboost(image_file_name, im.copy(), boost_constant)
        print("Highboost filter for " + image_file_name + " done.")


def run_day_three_filters(q):
    images_path_list = os.listdir('./images/')

    for image_file_name in images_path_list:
        im = imageio.imread('images/' + image_file_name)
        image_histogram(image_file_name, im)
        print("Histogram for " + image_file_name + " done.")
        max_filter(image_file_name, im.copy())
        print("Max for " + image_file_name + " done.")
        min_filter(image_file_name, im.copy())
        print("Min for " + image_file_name + " done.")
        midpoint_filter(image_file_name, im.copy())
        print("Midpoint for " + image_file_name + " done.")
        geometric_filter(image_file_name, im.copy())
        print("Geometric for " + image_file_name + " done.")
        harmonic_filter(image_file_name, im.copy())
        print("Harmonic for " + image_file_name + " done.")
        contraharmonic_filter(image_file_name, im.copy(), q)
        print("Contra-Harmonic for " + image_file_name + " done.")


def run_day_three_fourier(rows, columns):
    images_path_list = os.listdir('./images/fourier_images/')

    for image_file_name in images_path_list:
        im = imageio.imread('images/fourier_images/' + image_file_name)
        # image_histogram(image_file_name, im)
        # print("Histogram for " + image_file_name + " done.")
        f = fourier(image_file_name, im.copy())
        print("Fourier for " + image_file_name + " done.")
        f_filtered = fourier_operation(f, rows, columns)
        inverse_fourier(f_filtered)


def run_day_four(r, g, b, c, m, y, h, s, i):
    print("RGB to CMY:")
    print(rgb_to_cmy(r, g, b))
    print("RGB to HSI:")
    print(rgb_to_hsi(r, g, b))
    print("CMY to RGB:")
    print(cmy_to_rgb(c, m, y))
    print("CMY to HSI:")
    print(cmy_to_hsi(c, m, y))
    print("HSI to RGB:")
    print(hsi_to_rgb(h, s, i))
    print("HSI to CMY:")
    print(hsi_to_cmy(h, s, i))


def run_day_five():
    images_path_list = os.listdir('./images/')
    tsh_list = [200, -1, 180]

    for image_file_name in images_path_list:
        im = imageio.imread('images/' + image_file_name)

        full_tresholding(image_file_name, im, tsh_list)
        brightness(image_file_name, im, 30)


if __name__ == '__main__':
    # run_day_one(0.4, (255/log(256)), 0, 0, 10, 10, 11, 11, 13, 100, 14, 101, 255, 255)

    # weighted_kernel = np.array([[1, 5, 1], [5, 1, 5], [1, 5, 1]])
    # conv_kernel = np.array([[0, 5, 0], [0, 5, 0], [0, 5, 0]])
    # highboost_constant = 2
    #
    # run_day_two(weighted_kernel, conv_kernel, highboost_constant)

    # run_day_three_filters(2)

    # run_day_three_fourier([401,402,403,404],[370,371,372])
    #
    # run_day_four(200, 100, 50, 200, 100, 50, 20, 0.571, 116)

    run_day_five()
